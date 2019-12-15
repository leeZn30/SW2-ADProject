from PyQt5.QtWidgets import *
import pytube
import cv2
from PyQt5.QtCore import QCoreApplication

class CoinMain(QWidget):
    def __init__(self):
        super().__init__()
        self.downloadV()

    def downloadV(self):
        pl = pytube.YouTube("https://www.youtube.com/watch?v=kALFxV9EvZM&list=WL&index=2&t=0s")
        video = pl.streams.all()

        parent_dir = "/home/user/PycharmProjects/untitled/소프2ad"
        video[0].download(parent_dir)

        self.video_true()

    def video_true(self):
        global end
        end = False
        cap = cv2.VideoCapture('[국민대학교] 미래교육을 Kreate하다.mp4')
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("get CoiN!", frame)
                if cv2.waitKey(3) > 0:
                    break
            else:
                end = True
                cap.release()
                cv2.destroyAllWindows()
                self.c = 20
                break

    def initUI(self):
        QCoreApplication.instance().quit()
