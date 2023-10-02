# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(229, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        font = QFont()
        font.setPointSize(16)
        self.tb_new_task_title.setFont(font)

        self.horizontalLayout.addWidget(self.tb_new_task_title)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(20)
        self.btn_new_task.setFont(font1)
        self.btn_new_task.setStyleSheet(u"background-color:white")

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.date_time_box = QDateTimeEdit(self.centralwidget)
        self.date_time_box.setObjectName(u"date_time_box")
        self.date_time_box.setDate(QDate(2023, 9, 7))
        self.date_time_box.setTime(QTime(12, 0, 0))

        self.verticalLayout_3.addWidget(self.date_time_box)

        self.priority_box = QLineEdit(self.centralwidget)
        self.priority_box.setObjectName(u"priority_box")
        self.priority_box.setStyleSheet(u"border:no-border")
        self.priority_box.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.priority_box)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_low = QRadioButton(self.centralwidget)
        self.radioButton_low.setObjectName(u"radioButton_low")
        font2 = QFont()
        font2.setKerning(True)
        self.radioButton_low.setFont(font2)
        self.radioButton_low.setStyleSheet(u"background-color:white;")
        self.radioButton_low.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_low)

        self.radioButton_high = QRadioButton(self.centralwidget)
        self.radioButton_high.setObjectName(u"radioButton_high")
        self.radioButton_high.setStyleSheet(u"background-color:lightblue")

        self.horizontalLayout_3.addWidget(self.radioButton_high)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.tb_new_task_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 229, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tb_new_task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter task here", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.priority_box.setText(QCoreApplication.translate("MainWindow", u"Priority:", None))
        self.radioButton_low.setText(QCoreApplication.translate("MainWindow", u"low", None))
        self.radioButton_high.setText(QCoreApplication.translate("MainWindow", u"high", None))
        self.tb_new_task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter description here", None))
    # retranslateUi

