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
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 305)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.radioB_normal = QRadioButton(self.centralwidget)
        self.radioB_normal.setObjectName(u"radioB_normal")
        self.radioB_normal.setGeometry(QRect(50, 10, 221, 41))
        self.radioB_hard = QRadioButton(self.centralwidget)
        self.radioB_hard.setObjectName(u"radioB_hard")
        self.radioB_hard.setGeometry(QRect(50, 60, 201, 31))
        self.radioB_extrahard = QRadioButton(self.centralwidget)
        self.radioB_extrahard.setObjectName(u"radioB_extrahard")
        self.radioB_extrahard.setGeometry(QRect(50, 100, 231, 31))
        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setGeometry(QRect(170, 150, 121, 31))
        self.textbox_password = QLineEdit(self.centralwidget)
        self.textbox_password.setObjectName(u"textbox_password")
        self.textbox_password.setGeometry(QRect(80, 190, 171, 41))
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(40, 150, 121, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 330, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioB_normal.setText(QCoreApplication.translate("MainWindow", u"generate  a normal strength password\n"
"(including 6 characters)", None))
        self.radioB_hard.setText(QCoreApplication.translate("MainWindow", u"generate hard strength password\n"
"(including 8 characters)", None))
        self.radioB_extrahard.setText(QCoreApplication.translate("MainWindow", u"generate extra hard strength password\n"
"(including 12 characters)", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u" Generate Password", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset Password", None))
    # retranslateUi

