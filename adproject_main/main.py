import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import *

from player import Player
from howtoplay import HowToPlay
from nextMain import NextMain
from coinMain import CoinMain
from bustGame import BustGame, GameFinished

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.text = 0
        self.p = open("player.txt", "r")
        self.s = self.p.readlines()
        self.playerDic = dict()

        self.nowPlay = ""
        self.who() #player선택

        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(pal)

#플레이어 선택

    def who(self):
        for player_str in self.s:
            self.s = player_str.split()
            self.playerDic[self.s[0]] = int(self.s[1])

        self.playWindow = Player(self.playerDic)
        self.playWindow.show()

        self.playWindow.chBtn.clicked.connect(self.choosePlayer)
        self.playWindow.newStart.clicked.connect(self.newPlayer)
        self.playWindow.endBtn.clicked.connect(self.end)


    def choosePlayer(self):
        if self.playWindow.choose.text() not in self.playerDic:
            self.playWindow.warn.setStyleSheet('color:red')
            self.playWindow.warn.setText("플레이어를 찾을 수 없습니다!")
            self.playWindow.choose.setText("")

        else:
            self.nowPlay = self.playWindow.choose.text()
            self.text = int(self.playerDic[self.playWindow.choose.text()])
            self.playWindow.end_window()
            self.initUI()

    def newPlayer(self):
        if self.playWindow.newPlay.text() == "" or " " in self.playWindow.newPlay.text():
            self.playWindow.warn.setStyleSheet('color:red')
            self.playWindow.warn.setText("플레이어 이름을 비우거나 공백을 포함시킬 수 없습니다!")
            self.playWindow.newPlay.setText("")
        elif self.playWindow.newPlay.text() in self.playerDic:
            self.playWindow.warn.setStyleSheet('color:red')
            self.playWindow.warn.setText("이미 존재하는 플레이어 입니다!")
            self.playWindow.newPlay.setText("")
        else:
            self.playerDic[self.playWindow.newPlay.text()] = 100
            self.nowPlay = self.playWindow.newPlay.text()
            self.text = 100
            self.playWindow.end_window()
            self.initUI()

# 메인화면

    def initUI(self):
        #Button
        self.howtoplayButton = QPushButton('How to Play the Game?')
        self.startButton = QPushButton('Start Game!')
        self.pluscoinButton = QPushButton('see adv to get COIN!')
        self.endButton = QPushButton('End Game')

        #gamename image
        self.gnimgLabel = QLabel()
        self.setMinimumHeight(95)
        self.setMinimumWidth(200)
        pm = QPixmap('gamename.png')
        pm = pm.scaledToHeight(95)
        self.gnimgLabel.setPixmap(pm)

        #coin image
        self.cimgLabel = QLabel()
        self.setMinimumHeight(95)
        self.setMinimumWidth(95)
        pixmap = QPixmap('coin.png')
        pixmap = pixmap.scaledToHeight(75)
        self.cimgLabel.setPixmap(pixmap)

        #coin text
        self.cLabel = QLabel()
        font = self.cLabel.font()
        font.setPointSize(font.pointSize() + 10)
        self.cLabel.setFont(font)
        self.cLabel.setStyleSheet('color:white')
        self.cLabel.setText("X {} ".format(self.text))

        #main : grid / coint : coinBox/ button : buttonGrid
        self.grid = QGridLayout()
        self.coinBox = QHBoxLayout()

        self.coinBox.addWidget(self.gnimgLabel)
        self.coinBox.addStretch(1)
        self.coinBox.addWidget(self.cimgLabel)
        self.coinBox.addWidget(self.cLabel)

        self.buttonGrid = QGridLayout()

        self.grid.addLayout(self.coinBox, 0, 1)
        self.grid.addLayout(self.buttonGrid, 1, 0, 4, 0)

        self.buttonGrid.addWidget(self.howtoplayButton, 0, 0, 2, 2)
        self.buttonGrid.addWidget(self.startButton, 1, 0, 2, 2)
        self.buttonGrid.addWidget(self.pluscoinButton, 2, 0, 2, 2)
        self.buttonGrid.addWidget(self.endButton, 3, 0, 2, 2)

        #button을 눌렀을 때
        self.howtoplayButton.clicked.connect(self.howtoplay)
        self.startButton.clicked.connect(self.next)
        self.pluscoinButton.clicked.connect(self.coin)
        self.endButton.clicked.connect(self.end)

        self.setLayout(self.grid)
        self.setGeometry(500, 150, 900, 700)
        self.setWindowTitle('Main')
        self.show()

#게임설명창
    def howtoplay(self):
        self.playWindow = HowToPlay()
        self.playWindow.show()

#다음게임화면으로 넘어가기 위한 새로운창
    def next(self):
        self.newWindow = NextMain(self.text)
        self.newWindow.show()
        self.newWindow.coinBtn.clicked.connect(self.next_game)

#코인을 차감하기 위한 button click callback함수
    def next_game(self):
        if int(self.newWindow.coinLine.text()) < 0:
            self.newWindow.warn.setStyleSheet('color:red')
            self.newWindow.warn.setText("게임진행불가 : 코인부족")
        elif self.newWindow.coinHow < int(self.newWindow.coinLine.text()):
            self.newWindow.warn.setStyleSheet('color:red')
            self.newWindow.warn.setText("코인이 부족합니다!")
            self.newWindow.coinLine.clear()
        else:
            self.text = self.newWindow.coinHow - int(self.newWindow.coinLine.text())
            self.newWindow.end_game()
            self.cLabel.setStyleSheet('color:white')
            self.cLabel.setText("X {} ".format(self.text))

            #게임창으로 넘어가기
            self.gameWindow = BustGame(self.newWindow.coinLine.text())

        #exit버튼 눌렸을때 (게임결과창에서)
        self.gameWindow.gamefinish.exitGame.clicked.connect(self.exitClicked)

    def exitClicked(self):
        self.text += int(self.gameWindow.gamefinish.getResult_Coin())
        self.cLabel.setText("X {}".format(self.text))
        self.gameWindow.gamefinish.exit()
        self.gameWindow.exit()

#광고 시청후 coin++
    def coin(self):
        self.otherWindow = CoinMain()
        self.text += self.otherWindow.c
        self.cLabel.setStyleSheet('color:white')
        self.cLabel.setText("X {} ".format(self.text))

#플레이어와 코인을 파일에 저장한 후 게임을 종료
    def end(self):
        self.p = open("player.txt", "w")
        if self.nowPlay == "":
            for dic_py in self.playerDic:
                self.p.write(dic_py + " " + str(self.playerDic[dic_py]) + "\n")

        else:
            for each in self.playerDic:
                if each == self.nowPlay:
                    self.p.write(self.nowPlay + " " + str(self.text) + "\n")
                else:
                    self.p.write(each + " " + str(self.playerDic[each]) + "\n")
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())