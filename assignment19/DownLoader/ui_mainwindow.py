# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(295, 388)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_browse = QPushButton(self.centralwidget)
        self.btn_browse.setObjectName(u"btn_browse")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_browse.sizePolicy().hasHeightForWidth())
        self.btn_browse.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.btn_browse.setFont(font)
        self.btn_browse.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(235, 235, 235);")

        self.verticalLayout.addWidget(self.btn_browse)

        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.url.sizePolicy().hasHeightForWidth())
        self.url.setSizePolicy(sizePolicy1)
        self.url.setFont(font)
        self.url.setAutoFillBackground(False)
        self.url.setStyleSheet(u"background-color: rgb(236, 236, 236);")

        self.verticalLayout.addWidget(self.url)

        self.savelocation = QLineEdit(self.centralwidget)
        self.savelocation.setObjectName(u"savelocation")
        sizePolicy1.setHeightForWidth(self.savelocation.sizePolicy().hasHeightForWidth())
        self.savelocation.setSizePolicy(sizePolicy1)
        self.savelocation.setFont(font)
        self.savelocation.setAutoFillBackground(False)
        self.savelocation.setStyleSheet(u"background-color: rgb(231, 231, 231);")

        self.verticalLayout.addWidget(self.savelocation)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.progressBar)

        self.btn_download = QPushButton(self.centralwidget)
        self.btn_download.setObjectName(u"btn_download")
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        self.btn_download.setFont(font)
        self.btn_download.setAutoFillBackground(False)
        self.btn_download.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(85, 170, 0);")

        self.verticalLayout.addWidget(self.btn_download)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 295, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.savelocation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File save ", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"download", None))
    # retranslateUi

