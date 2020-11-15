import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")

        # hbox.addStretch()  # 空白を追加する、引数はint, 引く数がなければ最大値の空白
        hbox.addWidget(button1, alignment=Qt.AlignBottom)
        hbox.addWidget(button2, alignment=(Qt.AlignBottom | Qt.AlignLeft))
        # hbox.addStretch()
        hbox.addWidget(button3)
        self.setLayout(hbox)

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
