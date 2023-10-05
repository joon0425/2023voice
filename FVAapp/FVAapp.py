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

cd = str(pathlib.Path(__file__).parent.absolute())
print(cd)
form_class = uic.loadUiType(cd+"/FVAapp.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    filename  = cd.rstrip('FVAapp')+'FVA\\target_sounds\\recorded.wav'
    player    = QMediaPlayer()
    playlist  = QMediaPlaylist()
    isplaying = False
    playpaused= False
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.record.clicked.connect(self.f_record)
        self.play.clicked.connect(self.f_play)
        self.pause.clicked.connect(self.f_pause)
        self.stop.clicked.connect(self.f_stop)
        
        self.record.setIcon(QIcon(QPixmap(cd+'/icons/record.tif')))
        self.record.setIconSize(QSize(58,58))
        self.play.setIcon(QIcon(QPixmap(cd+'/icons/play.tif')))
        self.play.setIconSize(QSize(58,58))
        self.pause.setIcon(QIcon(QPixmap(cd+'/icons/pause.tif')))
        self.pause.setIconSize(QSize(58,58))
        self.stop.setIcon(QIcon(QPixmap(cd+'/icons/stop.tif')))
        self.stop.setIconSize(QSize(58,58))
        
        def handle_state_changed(state):
            if state==QMediaPlayer.PlayingState:
                self.isplaying=True
            elif state==QMediaPlayer.StoppedState:
                self.isplaying=False
        self.player.stateChanged.connect(handle_state_changed)
        
        

    def f_record(self):
        print("record Clicked")
        if self.isplaying or rc.recording:
            self.REC_stopFunc()
        self.recording = True
        rc.start()
        
    def f_play(self):
        print("play Clicked")
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
        print("pause Clicked")
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
        print("stop Clicked")
        self.REC_stopFunc()
      
    def REC_stopFunc(self):
        self.playpaused = False
        if rc.recording:
            rc.stop()
        if self.isplaying:
            self.player.stop()

        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()