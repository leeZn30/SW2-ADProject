from bustGame import BustGame

from PyQt5.QtWidgets import QWidget

class gameFinished(QWidget):

    def __init__(self, result):

        if result == "u_bust":
            return