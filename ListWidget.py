import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ListWidget')
        self.setGeometry(800, 50, 500, 500)
        self.UI()

    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        self.listwidget = QListWidget(self)
        self.listwidget.move(100, 80)
        ##########################################################
        list1 = ["Batman", "Superman", "Spiderman"]
        self.listwidget.addItems(list1)
        self.listwidget.addItem("Heman")

        # for number in range(5, 11):
        #     self.listwidget.addItem(str(number))
        ##########################################################
        btnAdd = QPushButton("Add", self)
        btnAdd.move(360, 80)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete = QPushButton("Delete", self)
        btnDelete.move(360, 110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet = QPushButton("Get", self)
        btnGet.move(360, 140)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.move(360, 170)
        btnDeleteAll.clicked.connect(self.funcDelete_All)

        self.show()

    def funcAdd(self):
        val = self.addRecord.text()
        self.listwidget.addItem(val)
        self.addRecord.clear()

    def funcDelete(self):
        idx = self.listwidget.currentRow()
        self.listwidget.takeItem(idx)

    def funcGet(self):
        try:
            val = self.listwidget.currentItem().text()
            print(val)
        except AttributeError:
            print("listwidget has no items")

    def funcDelete_All(self):
        self.listwidget.clear()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
