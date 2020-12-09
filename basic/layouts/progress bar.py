import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

count = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ProgressBar Widget")
        self.setGeometry(350, 150, 500, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressBar = QProgressBar()
        btnStart = QPushButton("Start")
        btnStop = QPushButton("Stop")
        btnStart.clicked.connect(self.timerStart)
        btnStop.clicked.connect(self.timerStop)

        vbox.addWidget(self.progressBar)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)
        hbox.addStretch()

        self.setLayout(vbox)
        self.timer = QTimer()
        self.timer.timeout.connect(self.runProgressBar)
        self.show()

    def timerStart(self):
        global count
        count = 0
        self.timer.start(10)

    def timerStop(self):
        self.timer.stop()

    def runProgressBar(self):
        global count
        count += 1
        self.progressBar.setValue(count)
        self.progressBar.setRange(0, 100)
        if count == self.progressBar.maximum():
            self.timer.stop()
            QMessageBox.information(self, "Information", "progressBar finish")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
