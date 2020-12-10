from PyQt5.QtWidgets import *
import sys


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent=parent)
        self.setWindowTitle("My Employee")
        self.setGeometry(450, 150, 750, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        self.employee_list = QListWidget()
        self.btn_new = QPushButton("New")
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Delete")

    def layouts(self):
        ##################Layouts####################
        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_btn_layout = QHBoxLayout()
        ##################Adding child layouts to main layouts####################
        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_btn_layout)
        self.main_layout.addLayout(self.left_layout, 40)
        self.main_layout.addLayout(self.right_main_layout, 60)
        ##################adding widgets to layout####################
        self.right_top_layout.addWidget(self.employee_list)
        self.right_btn_layout.addWidget(self.btn_new)
        self.right_btn_layout.addWidget(self.btn_update)
        self.right_btn_layout.addWidget(self.btn_delete)
        ##################setting main window layout ####################
        self.setLayout(self.main_layout)


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
