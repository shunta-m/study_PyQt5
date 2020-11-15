import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Timer')
        self.setGeometry(800, 50, 350, 350)
        self.UI()

    def UI(self):
        self.colorLabel = QLabel(self)
        self.colorLabel.resize(250, 250)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(40, 20)
        ######################buttons#####################
        btnstart = QPushButton("Start", self)
        btnstart.move(80, 300)
        btnstop = QPushButton("Stop", self)
        btnstop.move(190, 300)
        btnstart.clicked.connect(self.start)
        btnstop.clicked.connect(self.stop)
        #######################timer######################
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0

        # self.show()

    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("background-color:yellow")
            self.value = 1
        else:
            self.colorLabel.setStyleSheet("background-color:red")
            self.value = 0

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    window.show()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
