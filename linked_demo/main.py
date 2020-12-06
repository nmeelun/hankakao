from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from allpage.home import *
from allpage.item_up import *
from allpage.receipt import *
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.home = Home()
        self.itemup = ItemUp()
        self.receipt = Receipt()
        self.startHome()

    def startHome(self):
        self.home.setupUi(self)
        self.home.retranslateUi(self)
        self.home.btn_start.clicked.connect(self.startItemUp)
        self.show()

    def startItemUp(self):
        self.itemup.setupUi(self)
        self.itemup.retranslateUi(self)
        self.itemup.btn_hankakao.clicked.connect(self.startReceipt)
        self.show()

    def startReceipt(self):
        self.receipt.setupUi(self)
        self.receipt.retranslateUi(self)
        self.receipt.btn_close.clicked.connect(self.startHome)
        self.receipt.btn_close.clicked.connect(lambda:self.remove_file())
        self.show()

    def remove_file(self):
        os.remove("data_file.json")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())