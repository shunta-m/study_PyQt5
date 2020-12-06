import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FIle Dialogs")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileButton = QPushButton("Open File")
        fontbutton = QPushButton("Change Font")
        colorButton = QPushButton("Change Color")

        fileButton.clicked.connect(self.openFile)
        fontbutton.clicked.connect(self.changeFont)
        colorButton.clicked.connect(self.changeColor)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addWidget(fontbutton)
        hbox.addWidget(colorButton)
        hbox.addStretch()
        self.setLayout(vbox)
        self.show()

    def openFile(self):
        url, _ = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;*txt;;*py")
        print(url)
        with open(url, "r") as f:
            content = f.read()
            self.editor.setText(content)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        # self.editor.setStyleSheet(f"QWidget {{ background-color: {color.name()}}}")
        print(color, color.name())
        self.editor.setTextColor(color)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
