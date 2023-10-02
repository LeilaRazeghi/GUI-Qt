import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import urllib.request
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.save_location=QLineEdit()
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_browse.clicked.connect(self.browse_File)

    def browse_File(self):
        save_file = QFileDialog.getSaveFileName(self, caption ="save file as" , filter ="All File(*.*)")
        self.save_location.setText(save_file)
        
    def download(self):
        url = self.ui.url.text()
        save_location = self.ui.savelocation.text()

        try:
            urllib.request.urlretrieve(url, save_location , self.progress)
        except Exception:
            QMessageBox.information(self , "Warning" , "Download is failed")
            return

        QMessageBox.information(self , "Information" , "Download is complete")
        self.ui.progressBar.setValue(0)
        self.ui.url.setText("")
        self.ui.savelocation.setText("")

    def progress(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar *100 / totalsize
            self.ui.progressBar.setValue(int(percent))


app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.setWindowTitle("Pydownloader")
mainwindow.show()

app.exec()