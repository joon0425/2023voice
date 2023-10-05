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

cd = str(pathlib.Path(__file__).parent.absolute())
print(cd)
form_class = uic.loadUiType(cd+"\\FVAapp.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    filename  = cd.rstrip('FVAapp')+'FVA\\target_sounds\\recorded.wav'
    player    = QMediaPlayer()
    playlist  = QMediaPlaylist()
    isplaying = False
    playpaused= False
    FM        = FVAmanager(filename)
    lpcfig       = None
    lpccanvas    = None
    lpcaxes      = None
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.filepos.setText(self.filename)
        
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
    
    def f_ViewResult(self):
        self.log.setText("f_ViewResult() : ViewResult clicked")
        self.FM = FVAmanager(self.filename)
        self.ViewLpc()
    
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