import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal andVartical Box Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(buttonLayout)

        topLayout.setContentsMargins(100, 20, 20, 20)  # left, top, right, bottom
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)
        buttonLayout.setContentsMargins(150, 10, 150, 10)
        buttonLayout.addWidget(btn1)
        buttonLayout.addWidget(btn2)

        self.setLayout(mainLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
