import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import pathlib
import FVA.record as rc
from FVAmanager import FVAmanager
from FVA.detect import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time
import random
import pandas as pd
from DB.DBmanager import *
import matplotlib.patches as patches
import matplotlib
import matlab


pitchcondition = 0 # 0: upper than pitch, 1: +- 70Hz

matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

cd = str(pathlib.Path(__file__).parent.absolute())
print(cd)
form_class = uic.loadUiType(cd+"\\FVAapp.ui")[0]

def countSetup(namefilter=None,timefilter=None):
   """
   Args:
      namefilter (list): [names]
      timefilter (list): [start, end] with "2023-10-03" style
   """
   def toymd(x):
      return x.split('T')[0] 
   counts = np.zeros((8,nF1,nF2))
   for x in result.values.tolist():
      if (namefilter is None) or (userDict.get(x[4],None) in namefilter):
         if (timefilter is None) or (timefilter[0]<=toymd(x[3]) and timefilter[0]<=toymd(x[3])):
            counts[vowels[x[2]]][int(x[1].split('_')[0])-1][int(x[1].split('_')[1].split('.')[0])-1] += 1
   
   return counts.transpose(1,2,0)

nF1, nF2    =   10, 10
result, users   =   getDB()
formants        =   pd.read_excel("DB/sounds.xlsx")
vowels          =   {'ㅏ':0,'ㅓ':1,'ㅗ':2,'ㅜ':3,'ㅡ':4,'ㅣ':5,'ㅐ':6,'ㅔ':7}
colors          =   ['red','green','orange','dodgerblue','deeppink','aqua','blueviolet','yellow']
counts          =   np.zeros((8,nF1,nF2))
userDict        =   {a[0]:a[1] for a in users.values.tolist()}

NameFilter = None#['정도일']
TimeFilter = None#['2023-09-27','2023-10-03']

board = countSetup(namefilter=NameFilter,timefilter=TimeFilter)

def get_Findex(FM:FVAmanager):
    
    def softmax(x): # numpy array!!
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def probability(a):
        sum = a.sum()
        return a/sum
    
    fm  =   FM.FR_formants()
    fp  =   FM.FR_pitch()
    dellist = []
    for i,x in enumerate(fm):
        if pitchcondition == 0 and x <= fp: dellist.append(i)
        elif pitchcondition == 1 and x < fp + 70 and x > fp - 70: dellist.append(i)
    for i in dellist:
        del fm[i]

    F1 = [float(formants[i+1][0]) for i in range(10)]
    F2 = [float(formants[i+1][1]) for i in range(10)]
    logF1 = np.log10(np.array(F1))
    logF2 = np.log10(np.array(F2))
    nwF1 = np.log10(np.array([fm[0]]))[0]
    nwF2 = np.log10(np.array([fm[1]]))[0]
    nwF1in  = -1
    nwF1v   = 987654321.
    nwF2in  = -1
    nwF2v   = 987654321.
    for i in range(10):
        if nwF1v> abs(logF1[i]-nwF1):
            nwF1v = abs(logF1[i]-nwF1)
            nwF1in= i
        if nwF2v> abs(logF2[i]-nwF2):
            nwF2v = abs(logF2[i]-nwF2)
            nwF2in= i
            
    a = np.array(board[nwF1in][nwF2in])
    b = probability(a)
    a = softmax(a)

    precision = 1
    pairs_a = [[round(a[i]*100,precision),list(vowels.keys())[i]] for i in range(len(vowels.items()))]
    pairs_b = [[round(b[i]*100,precision),list(vowels.keys())[i]] for i in range(len(vowels.items()))]
    pairs_b = sorted(pairs_b,key=lambda x:x[0],reverse=True)
    
    return pairs_b, [nwF1in, nwF2in], fp, fm
    
    
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    filename    =   cd.rstrip('FVAapp')+'FVA\\target_sounds\\recorded.wav'
    player      =   QMediaPlayer()
    playlist    =   QMediaPlaylist()
    isplaying   =   False
    playpaused  =   False
    FM          =   FVAmanager(filename)
    
    lpcfig      =   None
    lpccanvas   =   None
    lpcaxes     =   None
    
    MAfig       =   None
    MAcanvas    =   None
    MAaxes      =   None
    
    MOfig       =   None
    MOcanvas    =   None
    MOaxes      =   None
    
    Lfig        =   None
    Lcanvas     =   None
    Laxes       =   None
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.filepos.setText(self.filename)
        
        self.setWindowTitle("FVA application v1.0")
        
        self.record.clicked.connect(self.f_record)
        self.play.clicked.connect(self.f_play)
        self.pause.clicked.connect(self.f_pause)
        self.stop.clicked.connect(self.f_stop)
        self.selectFile.clicked.connect(self.f_FileLoad)
        self.viewResult.clicked.connect(self.f_ViewResult)
        
        self.record.setIcon(QIcon(QPixmap(cd+'/icons/record.tif')))
        self.record.setIconSize(QSize(98,98))
        self.play.setIcon(QIcon(QPixmap(cd+'/icons/play.tif')))
        self.play.setIconSize(QSize(98,98))
        self.pause.setIcon(QIcon(QPixmap(cd+'/icons/pause.tif')))
        self.pause.setIconSize(QSize(98,98))
        self.stop.setIcon(QIcon(QPixmap(cd+'/icons/stop.tif')))
        self.stop.setIconSize(QSize(98,98))
        
        def handle_state_changed(state):
            if state==QMediaPlayer.PlayingState:
                self.isplaying=True
            elif state==QMediaPlayer.StoppedState:
                self.isplaying=False
        self.player.stateChanged.connect(handle_state_changed)
        
        self.lpcfig = plt.Figure()
        self.lpccanvas = FigureCanvas(self.lpcfig)
        self.lpclayout.addWidget(self.lpccanvas)
        
        self.MAfig = plt.Figure()
        self.MAcanvas = FigureCanvas(self.MAfig)
        self.MVPall_layout.addWidget(self.MAcanvas)
        
        self.MOfig = plt.Figure()
        self.MOcanvas = FigureCanvas(self.MOfig)
        self.MVPone_layout.addWidget(self.MOcanvas)
        
        self.Lfig = plt.Figure()
        self.Lcanvas = FigureCanvas(self.Lfig)
        self.label_layout.addWidget(self.Lcanvas)
        
        self.f1pixmap = QPixmap(cd+'\\F1axis.png')
        self.F1.setPixmap(self.f1pixmap)
        self.F1.setScaledContents(True)
        self.F1.setGeometry(QRect(720,469,100,466))
        
        self.f2pixmap = QPixmap(cd+'\\F2axis.png')
        self.F2.setPixmap(self.f2pixmap)
        self.F2.setScaledContents(True)
        self.F2.setGeometry(QRect(142,415,590,79))
        
        self.mvppixmap = QPixmap(cd+'\\MVPtitle.png')
        self.MVPtitle.setPixmap(self.mvppixmap)
        self.MVPtitle.setScaledContents(True)
        self.MVPtitle.setGeometry(QRect(190,908,510,53))
        
        self.ViewLabel()
        self.initMVP()
        
    def ViewLpc(self):
        if self.lpcaxes is not None:
            self.lpcaxes.cla()
            self.lpcaxes.set_visible(False)
            
        self.lpcaxes = self.lpcfig.subplots(1,1)
        
        x, y = self.FM.SSA.get_spectrum()[:2]
        lpcspec = self.FM.getlpcspec()
        loglpcspec = self.FM.to_db(lpcspec)
        logy = self.FM.to_db(y)
        
        bias = logy.mean() - loglpcspec.mean()
        
        self.lpcaxes.plot(x[::],logy[::],c='lightskyblue',lw=1,alpha=1,label='FFT')
        self.lpcaxes.plot(np.linspace(0,self.FM.SSA.sr/2.,len(loglpcspec)),loglpcspec+bias,label='LPC',color='green')
        f_result,i_result = formant_detect(lpcspec,self.FM.df0,1)
        self.lpcaxes.plot(f_result,loglpcspec[i_result]+bias,"o",c='r',label='formants',mew=4,ms=4)
        self.lpcaxes.set_xlim([0,8000])
        self.lpcaxes.legend()
        
        self.lpccanvas.draw()
        
        print(lpcspec)
    def ViewLabel(self):
        if self.Laxes is not None:
            self.Laxes.cla()
            self.Laxes.set_visible(False)
            
        self.Laxes = self.Lfig.subplots(1,1)
        axes = []
        labels = []
        for i,vowel in enumerate(vowels.keys()):
            self.Laxes.xaxis.set_visible(False)
            self.Laxes.yaxis.set_visible(False)
            self.Laxes.axis('off')
            axes.append(self.Laxes.scatter([],[],s=150,c=colors[i],marker='o',label=vowel))
            labels.append(vowel)
            
        self.Laxes.legend(axes,labels,fontsize=12,bbox_to_anchor=(1.1,0.8))
        self.Lcanvas.draw()      
    def initMVP(self,draw=True):
        if self.MAaxes is not None:
            for x in self.MAaxes.flatten():
                x.cla()
                x.set_visible(False)
        
        self.MAaxes = self.MAfig.subplots(nF1,nF2)

        for i in range(nF1):
            for q in range(nF2):
                self.MAaxes[i][nF2-q-1].set_aspect('equal', adjustable='box')
                self.MAaxes[i][nF2-q-1].xaxis.set_visible(False)
                self.MAaxes[i][nF2-q-1].yaxis.set_visible(False)
                self.MAaxes[i][nF2-q-1].axis('off')
                if q<nF2:
                    if board[i][q].sum()!=0 and i + nF2 - q - 1 < 15:
                        self.MAaxes[i][nF2-q-1].pie(np.array(board[i][q]),colors=colors,radius=1.3)
        if draw:self.MAcanvas.draw() 
    def ViewMVP(self):
        self.initMVP(draw=False)
        
        if self.MOaxes is not None:
            self.MOaxes.cla()
            self.MOaxes.set_visible(False)
        
        self.MOaxes = self.MOfig.subplots(1,1)
        
        res, Findex, fp, fm = get_Findex(self.FM)
        self.FMFP.clear()
        self.FMFP.append(' ')
        self.FMFP.append(f'Pitch : {round(fp,1)}Hz')
        self.FMFP.append(f'Formants : {", ".join(str(round(e,1))+"Hz" for e in fm[:4])}')
        sorted(Findex)
        
        self.MAaxes[Findex[0]][nF2-Findex[1]-1].add_patch(patches.Rectangle(
            (-1.25, -1.25),                   # (x, y)
            2.5, 2.5,                     # width, height
            edgecolor = 'black',
            facecolor = 'white',
            fill=False,
            linewidth=5.,
        ))
        
        self.MAcanvas.draw()
        
        self.MVPresult.clear()
        self.MVPresult.setAlignment(Qt.AlignCenter)
        self.MVPresult.append(' ')
        self.MVPresult.append('인공지능이 분석한 결과, 이 소리는')
        _size = len(res)
        print(res)
        for i,x in enumerate(res):
            if x[0] < 5.:
                _size=i
                break
        for i,x in enumerate(res[:_size]):
            if i==_size-1: self.MVPresult.append(f'{x[1]} 모음과 {x[0]}%')
            else: self.MVPresult.append(f'{x[1]} 모음과 {x[0]}%, ')
        self.MVPresult.append('가까운 소리입니다.')
        
        pairs = [[board[Findex[0]][Findex[1]][i],x,colors[i]] for i,x in enumerate(vowels.keys())]
        for i,x in enumerate(pairs):
            if x[0]<5.:
                pairs[i][1]=""
        
        def func(pct):
            return "" if pct<5. else f"{pct:.1f}%"
        
        pairs.reverse()
        
        self.MOaxes.pie(np.array(pairs).transpose((1,0))[0],colors=np.array(pairs).transpose((1,0))[2],labels=np.array(pairs).transpose((1,0))[1],autopct=lambda pct: func(pct),
                        textprops={'fontsize': 22},radius=1.2, counterclock=False, shadow=True)
        
        self.MOcanvas.draw()
    def f_ViewResult(self):
        self.log.setText("f_ViewResult() : ViewResult clicked")
        self.FM = FVAmanager(self.filename)
        self.ViewLpc()
        self.ViewMVP()
        self.ViewLabel()
    def f_record(self):
        self.log.setText("f_record() : record clicked")
        if self.isplaying or rc.recording:
            self.REC_stopFunc()
        self.recording = True
        rc.start()
        self.filename=cd.rstrip('FVAapp')+'FVA\\target_sounds\\recorded.wav'
    def f_play(self):
        self.log.setText("f_play() : play clicked")
        if self.isplaying or rc.recording:
            self.REC_stopFunc()
        self.isplaying = True
        self.playpaused = False
        
        url = QUrl.fromLocalFile(self.filename)
        print(self.filename)
        self.playlist.clear()
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        
        self.player.setPlaylist(self.playlist)
        self.player.play()
    def f_pause(self):
        self.log.setText("f_pause() : pause clicked")
        if rc.recording and not rc.pausing:
            rc.pause()
        elif rc.recording and rc.pausing:
            rc.resume()
        elif self.isplaying and not self.playpaused:
            self.player.pause()
            self.playpaused = True
        elif self.isplaying and self.playpaused:
            self.player.play()
            self.playpaused = False
    def f_stop(self):
        self.log.setText("f_stop() : stop clicked")
        self.REC_stopFunc()
    def REC_stopFunc(self):
        self.playpaused = False
        if rc.recording:
            rc.stop()
        if self.isplaying:
            self.player.stop()
    def f_FileLoad(self):
        fname=QFileDialog.getOpenFileName(self)
        
        if fname[0] and fname[0][-3:]=="wav":
            self.log.setText('f_FileLoad() : file load successed')
            self.filename=fname[0]
            self.filepos.setText(self.filename)
        else:
            self.log.setText('f_FileLoad() : file load failed')
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()