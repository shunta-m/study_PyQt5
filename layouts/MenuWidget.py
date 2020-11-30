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
        ####################ToolBar###################
        tb = self.addToolBar("My Toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon("icons/folder.png"), "New", self)
        tb.addAction(newTb)
        openTb = QAction(QIcon("icons/empty.png"), "Open", self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon("icons/save.png"), "Save", self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon("icons/exit.png"), "Exit", self)
        tb.addAction(exitTb)
        exitTb.triggered.connect(self.exitFunc)
        tb.actionTriggered.connect(self.btnFunc)
        self.show()

    def exitFunc(self):
        mbox = QMessageBox.information(self, "Information", "Are you sure to exit?", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def btnFunc(self, btn):
        if btn.text() == "New":
            print("You clicked New")
        elif btn.text() == "Open":
            print("You cliked Open")
        else:
            print("You clicked Save")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
