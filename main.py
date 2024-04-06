from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # upload our main interface
        uic.loadUi('untitled.ui', self)

        ### CONNECTIONS ==========================================================
        self.exit_app.clicked.connect(self.button_clicked)
        self.buildButton.clicked.connect(self.buildModel)
        self.showGraphButton.clicked.connect(self.paintMyGraphic)

        ### Buttons behavior (visible(default) / Hidden) =========================
        self.showGraphButton.hide()

        ### Combo Boxes behavior
        self.exchangeBox1.activated[str].connect(self.onChanged1)
        self.exchangeBox2.activated[str].connect(self.onChanged2)



        ### Functional of buttons ================================================

    def button_clicked(self):
        exit()
    def onChanged1(self, text):
        pass
    def onChanged2(self, text):
        pass


    def buildModel(self):
        value1 = self.exchangeBox1.currentText()
        value2 = self.exchangeBox2.currentText()
        if value1 == "AUD" and value2 == "AMD":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("WARNING!!!")
            msg.setText("We don't have this data yet")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
        elif value1 != value2:
            dataset = pd.read_csv(f'Sources/{value1}_{value2} Historical Data.csv')
            plt.scatter(dataset["Date"], dataset["Price"], color='red')
            plt.title(f'Changing {value1} to {value2}')
            plt.xlabel('Data')
            plt.ylabel(f'{value1}')
            self.buildButton.setText("Done")
            self.showGraphButton.show()

        elif value1 == value2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("WARNING!!!")
            msg.setText("You can't use same value")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
    def paintMyGraphic(self):
        plt.show()
        self.showGraphButton.hide()
        self.buildButton.setText("Build model")

    ### Functional of Combo Boxes ================================================


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
