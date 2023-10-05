import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from FVAmanager import FVAmanager
import numpy as np
from FVA.detect import *

#Matplotlib 전용 Widget Class 선언
class MplWidget(QWidget):
    Layout = None
    canvas = None
    
    def __init__(self,Layout:QVBoxLayout,parent=None):
        QWidget.__init__(self,parent)
        self.canvas = FigureCanvas(Figure())
        self.Layout = QVBoxLayout()
        self.Layout.addWidget(self.canvas)
        self.setLayout(self.Layout)
    
    def drawjust(self,fm:FVAmanager):
        self.canvas.figure.clear()
        ax = self.canvas.figure.subplots()
        ax.plot([1,2,3],[1,2,3])
        self.canvas.draw()
        
    def drawLpc(self,fm:FVAmanager):
        
        self.canvas.figure.clear()
        ax = self.canvas.figure.subplots()
        
        x, y = fm.SSA.get_spectrum()[:2]
        lpcspec = fm.getlpcspec()
        loglpcspec = fm.to_db(lpcspec)
        logy = fm.to_db(y)
        
        bias = logy.mean() - loglpcspec.mean()
        
        ax.plot(x[::],y[::],c='lightskyblue',lw=1,alpha=1,label='FFT')
        ax.plot(np.linspace(0,fm.SSA.sr/2.,len(loglpcspec)),loglpcspec+bias,label='LPC',color='green')
        f_result,i_result = formant_detect(lpcspec,fm.df0,1)
        ax.plot(f_result,loglpcspec[i_result]+bias,"o",c='r',label='formants',mew=4,ms=4)
        ax.set_xlim([0,8000])
        ax.legend()
        
        print(loglpcspec)
        
        self.canvas.draw()
        