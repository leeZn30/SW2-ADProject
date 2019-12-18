from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton, QTextEdit, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QColor

class Player(QWidget):
    def __init__(self, dic):
        super().__init__()
        self.play = dic
        self.img = QLabel()

        pal = QPalette()
        pal.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(pal)

        self.initUI()

    def initUI(self):
        self.list = QTextEdit()

        if len(self.play) != 0:
            self.playTxt = ''''''
            for x in self.play:
                self.playTxt += "Player : " + x + " , Coin : "  + str(self.play[x]) + "\n"
            self.list.setText(self.playTxt)

        else:
            pass

        self.list.setReadOnly(True)

        self.setMinimumHeight(250)
        self.setMinimumWidth(700)
        pixmap = QPixmap('gamerule.png')
        pixmap = pixmap.scaledToHeight(700)
        self.img.setPixmap(pixmap)

        self.choose = QLineEdit()
        self.chBtn = QPushButton("choose")

        self.newPlay = QLineEdit()
        self.newStart = QPushButton("new Play")

        self.warn = QLabel("")

        self.endBtn = QPushButton("CLOSE")

        self.grid = QGridLayout()

        self.grid.addWidget(self.list, 0, 0, 13, 2)
        self.grid.addWidget(self.warn, 13, 0, 1, 2)
        self.grid.addWidget(self.choose, 14, 0, 1, 1)
        self.grid.addWidget(self.chBtn, 14, 1, 1, 1)
        self.grid.addWidget(self.newPlay, 15, 0, 1, 1)
        self.grid.addWidget(self.newStart, 15, 1, 1, 1)
        self.grid.addWidget(self.endBtn, 16, 0, 1, 2)

        self.setLayout(self.grid)
        self.setWindowTitle("Choose Player!")
        self.setGeometry(700, 250, 600, 500)

    def end_window(self):
        self.deleteLater()