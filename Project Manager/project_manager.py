import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("Project Manager")
        self.setWindowIcon(QIcon(r"icons/icon.ico"))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.ui()
        self.show()

    def ui(self):
        self.set_toolbar()

    def set_toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ##################Toolbar Button####################
        #################Add Product######################
        self.add_product = QAction(QIcon(r"icons/add.png"), "Add Product", self)
        self.tb.addAction(self.add_product)
        self.tb.addSeparator()
        ####################Add Member######################
        self.add_member = QAction(QIcon(r"icons/users.png"), "Add Members", self)
        self.tb.addAction(self.add_member)
        self.tb.addSeparator()
        #######################Sell Product############################
        self.sell_product = QAction(QIcon(r"icons/sell.png"), "Sell Product", self)
        self.tb.addAction(self.sell_product)
        self.tb.addSeparator()


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
