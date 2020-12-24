import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread
import pyqtgraph as pg
import itertools


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("Plotter")
        self.setGeometry(450, 150, 800, 500)

        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.plot1 = pg.PlotWidget(QWidget(self))
        self.plot2 = pg.PlotWidget(QWidget(self))
        self.plot3 = pg.PlotWidget(QWidget(self))
        self.plot4 = pg.PlotWidget(QWidget(self))
        self.btn1 = QPushButton()
        self.btn2 = QPushButton()

    def layouts(self):
        main_layout = QVBoxLayout()
        graph_layout = QGridLayout()
        graph_layout.addWidget(self.plot1, 0, 0)
        graph_layout.addWidget(self.plot2, 0, 1)
        graph_layout.addWidget(self.plot3, 1, 0)
        graph_layout.addWidget(self.plot4, 1, 1)

        main_layout.addLayout(graph_layout)
        main_layout.addWidget(self.btn1)
        main_layout.addWidget(self.btn2)
        self.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
