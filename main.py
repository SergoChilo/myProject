from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


def clicked():
    print("Clicked")


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.myButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        exit()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
