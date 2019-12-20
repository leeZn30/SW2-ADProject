from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import random

class BlackjackGame(QWidget):

    def __init__(self, coin):
        super().__init__()
        self.setWindowTitle("BlackJack Game")
        self.setGeometry(340, 150, 900, 400)
        self.setFixedSize(900, 400)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(0, 100, 0))
        self.setPalette(pal)
        self.interval = 100
        self.d_previous = 50
        self.u_previous = 50
        self.d_point = 0
        self.u_point = 0
        self.dealer_point = QLabel(self)
        self.user_point = QLabel(self)
        self.dealer = []
        self.user = []

        self.coin = int(coin)
        # coin
        self.coin_st = QLineEdit(self)
        self.coin_st.setPlaceholderText(str(int(self.coin)))
        self.coin_st.setGeometry(800, 30, 60, 30)
        self.coin_st.setReadOnly(True)
        self.coin_st.setAlignment(Qt.AlignRight)

        # dealer
        self.dealerCardDic = {str(x) + "_r.jpg" : x for x in range(1,12)}
        self.dealerCardList = list(self.dealerCardDic[str(x) + "_r.jpg"] for x in range(1, 10))
        self.first_dealerCardList = list(self.dealerCardDic.keys())

        # user
        self.userCardDic = {str(x) + ".jpg" : x for x in range(1,12)}
        self.userCardList = list(self.userCardDic[str(x) + ".jpg"] for x in range(1, 10))
        self.first_userCardList = list(self.userCardDic.keys())

        # dealer's first init
        self.dealer_lbl = QLabel(self)
        self.dealer_card = QPixmap("card_reverse.jpg")
        self.dealer_lbl.setGeometry(self.d_previous, 70, 60, 100)
        self.dealer_lbl.setPixmap(self.dealer_card)

        # dealer's second card
        d_lbl2 = QLabel(self)
        d_card2 = random.sample(self.dealerCardList, 1)[0]
        self.d_point += d_card2
        self.dealer.append(d_card2)
        d_card2 = QPixmap(str(d_card2) + "_r.jpg")
        d_lbl2.setGeometry(self.d_previous + self.interval, 70, 60, 100)
        self.d_previous = self.d_previous + self.interval
        d_lbl2.setPixmap(d_card2)

        self.startGame()
        self.gamefinish = GameFinished()

    def startGame(self):

        # user's first Card
        user_lbl = QLabel(self)
        user_card = random.sample(self.first_userCardList, 1)[0]
        self.u_point += self.userCardDic[user_card]
        self.user.append(self.userCardDic[user_card])
        user_card = QPixmap(user_card)
        user_lbl.setGeometry(self.u_previous, 230, 60, 100)
        user_lbl.setPixmap(user_card)
        self.showPoint()

        # user's second Card
        user_lbl2 = QLabel(self)
        user_card2 = random.sample(self.userCardList, 1)[0]
        self.u_point += user_card2
        self.user.append(user_card2)
        user_card2 = QPixmap(str(user_card2) + ".jpg")
        user_lbl2.setGeometry(self.u_previous + self.interval, 230, 60, 100)
        user_lbl2.setPixmap(user_card2)
        self.u_previous = self.u_previous + self.interval
        self.user_sum = sum(self.user)
        self.showPoint()

        # hit, stand button
        self.hitButton = QPushButton(self)
        self.hitButton.setText("Hit!")
        self.hitButton.setGeometry(800, 160, 50, 30)
        self.hitButton.clicked.connect(self.pushHit)

        self.standButton = QPushButton(self)
        self.standButton.setText("Stand")
        self.standButton.setGeometry(800, 210, 50,30)
        self.standButton.clicked.connect(self.playDealer)

        self.show()

    def pushHit(self):

        # user puts card
        u_lbl = QLabel(self)
        u_card = random.sample(self.userCardList, 1)[0]
        self.user.append(u_card)
        self.u_point += u_card
        u_card = QPixmap(str(u_card) + ".jpg")
        u_lbl.setGeometry(self.u_previous + self.interval, 230, 60, 100)
        u_lbl.setPixmap(u_card)
        self.u_previous = self.u_previous + self.interval
        self.user_sum = sum(self.user)
        self.user_to_21 = 21 - self.user_sum
        if self.user_sum > 21:
            self.hitButton.setDisabled(True)

        u_lbl.show()
        self.showPoint()
        self.userFinished()

    def playDealer(self):

        self.hitButton.setDisabled(True)

        self.dealer_sum = sum(self.dealer)
        self.dealer_to_21 = 21 - self.dealer_sum

        self.dealer_card = random.sample(self.first_dealerCardList, 1)[0]
        self.dealer.append(self.dealerCardDic[self.dealer_card])
        self.d_point += (self.dealerCardDic[self.dealer_card])
        self.dealer_card = QPixmap(self.dealer_card)

        self.dealer_lbl.setPixmap(self.dealer_card)
        self.showPoint()
        self.dealerFinished()

        # dealer puts card
        while self.dealer_sum <= 16:

            d_lbl = QLabel(self)
            d_card = random.sample(self.dealerCardList, 1)[0]
            self.dealer.append(d_card)
            self.d_point += d_card
            d_card = QPixmap(str(d_card) + "_r.jpg")
            d_lbl.setPixmap(d_card)
            d_lbl.setGeometry(self.d_previous + self.interval, 70, 60, 100)
            self.d_previous = self.d_previous + self.interval
            self.dealer_sum = sum(self.dealer)
            d_lbl.show()
            self.showPoint()

        self.dealerFinished()

    def showPoint(self):

        # showing dealer's point
        self.dealer_point.setText(str(self.d_point))
        self.dealer_point.setFont(QFont("times", 20))
        self.dealer_point.setStyleSheet("Color : white")

        if len(str(self.d_point)) == 1:
            self.dealer_point.setGeometry(71, 175, 60, 25)
        else:
            self.dealer_point.setGeometry(65, 175, 60, 25)

        # showing user's point
        self.user_point.setText(str(self.u_point))
        self.user_point.setFont(QFont("times", 20))
        self.user_point.setStyleSheet("Color : white")

        if len(str(self.u_point)) == 1:
            self.user_point.setGeometry(71, 335, 60, 25)
        else:
            self.user_point.setGeometry(65, 335, 60, 25)

        self.dealer_point.show()
        self.user_point.show()

    def userFinished(self):

        if self.user_sum > 21:
            self.gamefinish.setResultCoin("u_bust", self.coin)
            self.result_coin = int(self.gamefinish.coin * 1.5)
            self.hitButton.setDisabled(True)
            self.standButton.setDisabled(True)

        elif self.user_sum == 21:
            self.gamefinish.setResultCoin("u_blackjack", self.coin)
            self.hitButton.setDisabled(True)
            self.standButton.setDisabled(True)

    def dealerFinished(self):
        self.standButton.setDisabled(True)

        if self.user_sum == self.dealer_sum:
            self.gamefinish.setResultCoin("push", self.coin)
            self.hitButton.setDisabled(True)

        elif self.dealer_sum > 21:
            self.gamefinish.setResultCoin("d_bust", self.coin)
            self.hitButton.setDisabled(True)

        elif self.dealer_sum == 21:
            self.gamefinish.setResultCoin("d_blackjack", self.coin)
            self.hitButton.setDisabled(True)

        elif self.dealer_sum > self.user_sum:
            self.gamefinish.setResultCoin("d_win", self.coin)
            self.hitButton.setDisabled(True)

        elif self.dealer_sum < self.user_sum:
            self.gamefinish.setResultCoin("u_win", self.coin)
            self.hitButton.setDisabled(True)

    def exit(self):
        self.deleteLater()

class GameFinished(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Result")
        self.setGeometry(340, 600, 900, 400)
        self.setFixedSize(900, 400)
        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(105, 55, 105))
        self.setPalette(pal)
        self.coin = 0
        self.result_coin = 0

        hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        hbox4 = QHBoxLayout()

        vbox = QVBoxLayout()

        self.result_lbl = QLabel(self)
        self.exitGame = QPushButton()
        self.exitGame.setText("Exit")
        self.coin_state = QLabel(self)

        hbox1.addWidget(self.result_lbl)
        self.hbox2.addWidget(self.coin_state)
        hbox4.addWidget(self.exitGame)
        vbox.addLayout(hbox1)
        vbox.addLayout(self.hbox2)
        vbox.addLayout(hbox4)
        self.setLayout(vbox)

        self.result = ""

    def setResultCoin(self, result, coin):
        self.result = result
        self.coin = coin
        self.gameFinished(self.result)


    def gameFinished(self, result):
        self.result_coin = 0

        if result == "u_bust":
            self.result_lbl.setText("You're Bust!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("-" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin -= int(self.coin * 0.5)
            self.show()

        elif result == "u_blackjack":
            self.result_lbl.setText("You hit BlackJack!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("+" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin += int(self.coin * 1.5)
            self.show()

        elif result == "push":
            self.result_lbl.setText("Push! Draw!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("+" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.coin_state.setText(str(int(self.coin)))
            self.result_coin = self.coin
            self.show()

        elif result == "d_bust":
            self.result_lbl.setText("Dealer is Bust!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("+" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin += int(self.coin * 1.5)
            self.show()

        elif result == "d_blackjack":
            self.result_lbl.setText("Dealer hits BlackJack!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("-" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin -= int(self.coin * 0.5)
            self.show()

        elif result == "d_win":
            self.result_lbl.setText("Dealer is closer to 21!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("-" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin -= int(self.coin * 0.5)
            self.show()

        elif result == "u_win":
            self.result_lbl.setText("You are closer to 21!")
            self.result_lbl.setFont(QFont("times", 50))
            self.result_lbl.setStyleSheet("Color : black")
            self.coin_state.setText("+" + str(int(self.coin * 1.5)))
            self.coin_state.setFont(QFont("times", 30))
            self.coin_state.setStyleSheet("Color : black")
            self.result_coin += int(self.coin * 1.5)
            self.show()

    def getResult_Coin(self):
        return self.result_coin

    def exit(self):
        self.deleteLater()
