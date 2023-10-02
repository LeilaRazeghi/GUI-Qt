import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.db= Database()
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_title= self.ui.tb_new_task_title.text()
        new_description= self.ui.tb_new_task_description.toPlainText()
        #feedback= self.db.add_new_tasks(new_title, new_description)

        if self.ui.radioButton_low.isChecked()== True:
            priority= "low"
        elif self.ui.radioButton_high.isChecked()== True:
            priority= "high"
        new_date_time= self.ui.date_time_box.text()
        

        if new_title !="":
            feedback=self.db.add_new_tasks(new_title, new_description, priority, new_date_time)
            if feedback == True:
               for i in reversed(range(self.ui.gl_tasks.count())):
                   self.ui.gl_tasks.itemAt(i).widget().setParent(None)
               self.read_from_database()
            else:
                msg_box= QMessageBox()
                msg_box.setText("something wrong has happened!")
                msg_box.exec_()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setText("")

        else:
            msg_box= QMessageBox()
            msg_box.setText("enter title")
            msg_box.exec_()                                                         
    
    def remove(self, id):
        feedback=self.db.remove_task(id)
        if feedback==True:
            for i in reversed(range(self.ui.gl_tasks.count())):
                self.ui.gl_tasks.itemAt(i).widget().setParent(None)
            self.read_from_database()
        else:
            msg_box= QMessageBox()
            msg_box.setText("something wrong has happened!")
            msg_box.exec_()

    def read_from_database(self):
        tasks= self.db.get_tasks()
        for i in range(len(tasks)):
            new_checkbox= QCheckBox()
            new_label= QLabel()
            new_btn= QPushButton()

            if tasks[i][3]==1:
                new_checkbox.setChecked(True)
            else:
                new_checkbox.setChecked(False)

            new_label.setText(tasks[i][1])
            if tasks[i][3]=="high":
                new_label.setStyleSheet("background-color:lightblue")
            elif tasks[i][3]=="low":
                new_label.setStyleSheet("background-color:white")

            new_btn.setText("❌")

            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_btn, i, 2)

            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][0]))
            new_btn.clicked.connect(partial(self.remove, tasks[i][0]))

            tooltip_text=f"<p>{tasks[i][0]}</p><p>{tasks[i][2]}</p><p>{tasks[i][3]}</p>"
            new_label.setToolTip(tooltip_text)
            new_label.show()
       
if __name__== "__main__":
    app= QApplication(sys.argv)

    main_window= MainWindow()
    main_window.show()

    app.exec()