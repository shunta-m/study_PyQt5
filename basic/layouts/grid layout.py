import sys, itertools
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout()
        # btn1 = QPushButton("Button1")
        # btn2 = QPushButton("Button2")
        # btn3 = QPushButton("Button3")
        # btn4 = QPushButton("Button4")

        # self.gridLayout.addWidget(btn1, 0, 0)
        # self.gridLayout.addWidget(btn2, 0, 1)
        # self.gridLayout.addWidget(btn3, 1, 0)
        # self.gridLayout.addWidget(btn4, 1, 1)

        grid_index = itertools.product(range(3), range(3))
        for row, col in grid_index:
            btn = QPushButton(f"button{row}-{col}")
            btn.clicked.connect(self.clickMe)
            self.gridLayout.addWidget(btn, row, col)

        self.setLayout(self.gridLayout)
        self.show()

    def clickMe(self):
        buttonID = self.sender().text()
        print(f"You clicked {buttonID}")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
