import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # (x_pos, y_pos, width, height), posは左上の座標
        self.setGeometry(150, 250, 550, 250)
        self.setWindowTitle("This is our Window's Title")

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())