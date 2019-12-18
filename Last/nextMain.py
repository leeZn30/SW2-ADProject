from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QCoreApplication

class NextMain(QWidget):
    def __init__(self, text):
        super().__init__()

        self.coinHow = text
        self.coinResult = 0
        self.resultLabel = QLabel("현재 보유 코인 : {} coin ".format(text))
        self.resultLabel.setStyleSheet('color:blue')
        self.warn = QLabel("")
        self.isend = False
        self.initUI(self.coinHow)

    def initUI(self, text):
        self.coinLabel = QLabel('몇 코인을 거시겠습니까?')
        self.coinLine = QLineEdit()
        self.coinBtn = QPushButton('CLICK!')


        vbox = QVBoxLayout()

        vWidgetBox = QHBoxLayout()
        vWidgetBoxT = QHBoxLayout()
        vWidgetBox.addWidget(self.coinLabel)
        vWidgetBoxT.addWidget(self.coinLine)
        vWidgetBoxT.addWidget(self.coinBtn)

        vbox.addWidget(self.resultLabel)
        vbox.addLayout(vWidgetBox)
        vbox.addLayout(vWidgetBoxT)
        vbox.addWidget(self.warn)
        #
        # self.coinBtn.clicked.connect(self.next_game)

        self.setLayout(vbox)
        self.setWindowTitle('howCoin?')
        self.setGeometry(850, 300, 150, 150)
    #
    # def next_game(self):
    #     if self.coinHow < int(self.coinLine.text()):
    #         self.warn.setStyleSheet('color:red')
    #         self.warn.setText("코인이 부족합니다!")
    #     else:
    #         self.coinResult = self.coinHow - int(self.coinLine.text())
    #         self.end_game()

    def end_game(self):
        self.deleteLater()