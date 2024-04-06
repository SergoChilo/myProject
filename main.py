from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
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

        # global value1, value2
        #
        # value1 = self.onChanged1(self.exchangeBox1.currentText())
        # value2 = self.onChanged2(self.exchangeBox2.currentText())

        ### Functional of buttons ================================================
        # print(value1)
        # print(value2)
    def button_clicked(self):
        exit()

    def onChanged1(self, text):
        print(text)

    def onChanged2(self, text):
        print(text)


    def buildModel(self):
        value1 = self.exchangeBox1.currentText()
        value2 = self.exchangeBox2.currentText()
        if value1 != value2:

            dataset = pd.read_csv(f'Sources/{value1}_{value2} Historical Data.csv')

            plt.scatter(dataset["Date"], dataset["Price"], color='red')
            plt.title('Changing AMD to USD')
            plt.xlabel('Data')
            plt.ylabel('AMD')
            self.buildButton.setText("Done")
            self.showGraphButton.show()
        else:
            pass
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
