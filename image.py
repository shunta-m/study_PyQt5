import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from pathlib import Path

image_path = (r"./images/pip image.png")


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('using Labels')
        self.setGeometry(50, 50, 500, 500)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(image_path))
        self.image.move(150, 50)
        self.image.resize(100, 100)
        removeButton = QPushButton("Remove", self)
        removeButton.move(150, 220)
        showButton = QPushButton("Show", self)
        showButton.move(260, 220)

        removeButton.clicked.connect(self.removeImg)
        showButton.clicked.connect(self.showImg)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
