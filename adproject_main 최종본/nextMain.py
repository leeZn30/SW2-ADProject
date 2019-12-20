from PyQt5.QtWidgets import *

class NextMain(QWidget):
    def __init__(self, text):
        super().__init__()

        self.resultLabel = QLabel("현재 보유 코인 : {} coin ".format(text))
        self.resultLabel.setStyleSheet('color:blue')
        self.warn = QLabel("")
        self.initUI()

    def initUI(self):
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

        self.setLayout(vbox)
        self.setWindowTitle('howCoin?')
        self.setGeometry(850, 300, 150, 150)

    def end_game(self):
        self.deleteLater()