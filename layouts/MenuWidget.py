import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        ###################Main Menu ################
        menuber = self.menuBar()
        file = menuber.addMenu("File")
        edit = menuber.addMenu("Edit")
        code = menuber.addMenu("Code")
        help_ = menuber.addMenu("Help")
        ###################Sub Menu ################
        new = QAction("New Project", self)
        file.addAction(new)
        new.setShortcut("Ctrl+0")
        open_ = QAction("Open", self)
        file.addAction(open_)
        exit_ = QAction("Exit", self)
        # exit_.setIcon(QIcon("icons/exit.png"))
        exit_.triggered.connect(self.exitFunc)
        file.addAction(exit_)
        self.show()

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Information", "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
