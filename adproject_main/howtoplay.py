from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

class HowToPlay(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()

        self.playLabel = QLabel()
        self.setMinimumHeight(650)
        self.setMinimumWidth(650)
        pixmap = QPixmap('10656700518.5.20190611002904.jpg')
        pixmap = pixmap.scaledToHeight(650)
        self.playLabel.setPixmap(pixmap)

        self.close_Btn = QPushButton("CLOSE")

        self.close_Btn.clicked.connect(self.end_window)

        self.grid.addWidget(self.playLabel, 0, 0, 8, 2)
        self.grid.addWidget(self.close_Btn, 8, 0, 1, 2)

        self.setLayout(self.grid)
        self.setWindowTitle('how To play Game?')
        self.setGeometry(620, 170, 650, 650)
        self.show()

    def end_window(self):
        self.deleteLater()