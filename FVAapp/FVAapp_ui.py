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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 90, 691, 161))
        self.tabWidget.setStyleSheet(u"")
        self.rec = QWidget()
        self.rec.setObjectName(u"rec")
        self.record = QPushButton(self.rec)
        self.record.setObjectName(u"record")
        self.record.setGeometry(QRect(50, 30, 100, 100))
        self.play = QPushButton(self.rec)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(210, 30, 100, 100))
        self.pause = QPushButton(self.rec)
        self.pause.setObjectName(u"pause")
        self.pause.setGeometry(QRect(370, 30, 100, 100))
        self.stop = QPushButton(self.rec)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(530, 30, 100, 100))
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
        self.log.setGeometry(QRect(50, 20, 801, 20))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(790, 70, 721, 281))
        self.lpclayout = QVBoxLayout(self.verticalLayoutWidget)
        self.lpclayout.setObjectName(u"lpclayout")
        self.lpclayout.setContentsMargins(0, 0, 0, 0)
        self.viewResult = QPushButton(self.centralwidget)
        self.viewResult.setObjectName(u"viewResult")
        self.viewResult.setGeometry(QRect(315, 280, 150, 24))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(210, 370, 721, 661))
        self.MVPall_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.MVPall_layout.setObjectName(u"MVPall_layout")
        self.MVPall_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(950, 370, 721, 661))
        self.MVPone_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.MVPone_layout.setObjectName(u"MVPone_layout")
        self.MVPone_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(50, 370, 161, 661))
        self.label_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.label_layout.setObjectName(u"label_layout")
        self.label_layout.setContentsMargins(0, 0, 0, 0)
        self.fmfp = QLabel(self.centralwidget)
        self.fmfp.setObjectName(u"fmfp")
        self.fmfp.setGeometry(QRect(50, 60, 691, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


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
        self.fmfp.setText(QCoreApplication.translate("MainWindow", u"(Pitch, Formants)", None))
    # retranslateUi

