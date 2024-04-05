from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView
import pyqtgraph as pg
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.exit_app.clicked.connect(self.button_clicked)
        self.countButton.clicked.connect(self.uiComponents)

        self.showGraphButton.hide()
        self.showGraphButton.clicked.connect(self.paintMyGraphic)

    def button_clicked(self):
        exit()

    def uiComponents(self):
        self.showGraphButton.show()

        dataset = pd.read_csv('Sources/Salary_Data.csv')
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        y_pred = regressor.predict(X_test)
        plt.scatter(X_train, y_train, color='red')
        plt.plot(X_train, regressor.predict(X_train),
                 color='blue')
        plt.title('Salary vs Experience (Training set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')

    def paintMyGraphic(self):
        plt.show()
        self.showGraphButton.hide()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
