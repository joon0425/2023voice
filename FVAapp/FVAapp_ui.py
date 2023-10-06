# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FVAapp.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2205, 1172)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 70, 791, 161))
        self.tabWidget.setStyleSheet(u"")
        self.rec = QWidget()
        self.rec.setObjectName(u"rec")
        self.record = QPushButton(self.rec)
        self.record.setObjectName(u"record")
        self.record.setGeometry(QRect(110, 30, 100, 100))
        self.play = QPushButton(self.rec)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(270, 30, 100, 100))
        self.pause = QPushButton(self.rec)
        self.pause.setObjectName(u"pause")
        self.pause.setGeometry(QRect(430, 30, 100, 100))
        self.stop = QPushButton(self.rec)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(590, 30, 100, 100))
        self.tabWidget.addTab(self.rec, "")
        self.file = QWidget()
        self.file.setObjectName(u"file")
        self.file.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.selectFile = QPushButton(self.file)
        self.selectFile.setObjectName(u"selectFile")
        self.selectFile.setGeometry(QRect(30, 30, 130, 30))
        self.selectFile.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.filepos = QLabel(self.file)
        self.filepos.setObjectName(u"filepos")
        self.filepos.setGeometry(QRect(30, 100, 741, 16))
        self.tabWidget.addTab(self.file, "")
        self.log = QLabel(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(50, 30, 801, 20))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(950, 70, 921, 301))
        self.lpclayout = QVBoxLayout(self.verticalLayoutWidget)
        self.lpclayout.setObjectName(u"lpclayout")
        self.lpclayout.setContentsMargins(0, 0, 0, 0)
        self.viewResult = QPushButton(self.centralwidget)
        self.viewResult.setObjectName(u"viewResult")
        self.viewResult.setGeometry(QRect(380, 250, 150, 24))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 430, 721, 531))
        self.MVPall_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.MVPall_layout.setObjectName(u"MVPall_layout")
        self.MVPall_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(950, 400, 621, 561))
        self.MVPone_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.MVPone_layout.setObjectName(u"MVPone_layout")
        self.MVPone_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(50, 430, 111, 531))
        self.label_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.FMFP = QTextBrowser(self.centralwidget)
        self.FMFP.setObjectName(u"FMFP")
        self.FMFP.setGeometry(QRect(50, 300, 791, 71))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.FMFP.setFont(font)
        self.F2 = QLabel(self.centralwidget)
        self.F2.setObjectName(u"F2")
        self.F2.setGeometry(QRect(150, 410, 701, 81))
        self.F1 = QLabel(self.centralwidget)
        self.F1.setObjectName(u"F1")
        self.F1.setGeometry(QRect(780, 430, 101, 471))
        self.MVPtitle = QLabel(self.centralwidget)
        self.MVPtitle.setObjectName(u"MVPtitle")
        self.MVPtitle.setGeometry(QRect(410, 940, 121, 16))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 399, 791, 31))
        self.frame.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(800, 430, 41, 531))
        self.frame_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.MVPresult = QTextBrowser(self.centralwidget)
        self.MVPresult.setObjectName(u"MVPresult")
        self.MVPresult.setGeometry(QRect(1570, 400, 300, 560))
        self.MVPresult.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.frame_2.raise_()
        self.tabWidget.raise_()
        self.log.raise_()
        self.verticalLayoutWidget.raise_()
        self.viewResult.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.FMFP.raise_()
        self.F2.raise_()
        self.F1.raise_()
        self.MVPtitle.raise_()
        self.MVPresult.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2205, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.record.setText("")
        self.play.setText("")
        self.pause.setText("")
        self.stop.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rec), QCoreApplication.translate("MainWindow", u"\ub179\uc74c", None))
        self.selectFile.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc120\ud0dd\ud558\uae30", None))
        self.filepos.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uacbd\ub85c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file), QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.viewResult.setText(QCoreApplication.translate("MainWindow", u"\uacb0\uacfc \ubcf4\uae30", None))
        self.FMFP.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:16pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p></body></html>", None))
        self.F2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.F1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.MVPtitle.setText(QCoreApplication.translate("MainWindow", u"MVPtitle", None))
    # retranslateUi

