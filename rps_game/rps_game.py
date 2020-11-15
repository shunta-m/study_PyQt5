import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)

computerScore = 0
playerScore = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rock Paper Scissors Game')
        self.setGeometry(800, 50, 500, 500)
        self.UI()

    def UI(self):
        #########################Scores####################
        self.scoreComputerText = QLabel("Computer Score : ", self)
        self.scoreComputerText.setFont(textFont)
        self.scoreComputerText.move(30, 20)
        self.scorePlayerText = QLabel("Your Score : ", self)
        self.scorePlayerText.setFont(textFont)
        self.scorePlayerText.move(330, 20)
        #########################Images####################
        self.imameComputer = QLabel(self)
        self.imameComputer.setPixmap(QPixmap(r"./images/rock.png"))
        self.imameComputer.move(50, 100)

        self.imamePlayer = QLabel(self)
        self.imamePlayer.setPixmap(QPixmap(r"./images/rock.png"))
        self.imamePlayer.move(330, 100)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap(r"./images/game.png"))
        self.imageGame.move(230, 160)
        #########################Buttons####################
        btnStart = QPushButton("Start", self)
        btnStart.setFont(buttonFont)
        btnStart.move(180, 250)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.setFont(buttonFont)
        btnStop.move(270, 250)
        btnStop.clicked.connect(self.stop)
        #########################Timer####################

        self.timer = QTimer(self)
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer = randint(1, 3)
        if self.rndComputer == 1:
            self.imameComputer.setPixmap(QPixmap(r"./images/rock.png"))
        elif self.rndComputer == 2:
            self.imameComputer.setPixmap(QPixmap(r"./images/paper.png"))
        else:
            self.imameComputer.setPixmap(QPixmap(r"./images/scissors.png"))

        self.rndPlayer = randint(1, 3)
        if self.rndPlayer == 1:
            self.imamePlayer.setPixmap(QPixmap(r"./images/rock.png"))
        elif self.rndPlayer == 2:
            self.imamePlayer.setPixmap(QPixmap(r"./images/paper.png"))
        else:
            self.imamePlayer.setPixmap(QPixmap(r"./images/scissors.png"))

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == self.rndPlayer:
            mbox = QMessageBox.information(self, "information", "Draw Game")
        elif self.rndComputer == 1 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(playerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(computerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(computerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "information", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(computerScore))

        self.scorePlayerText.adjustSize()
        self.scoreComputerText.adjustSize()


        if computerScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, "information", "Game over")
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
