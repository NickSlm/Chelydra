from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PIL import ImageGrab
import win32gui 

class Overlay(QMainWindow):
    def __init__(self,win_info):
        super().__init__()
        self.win_info = win_info
        self.init_window()

    def init_window(self):
        self.setGeometry(self.win_info.win_x, self.win_info.win_y, self.win_info.win_width, self.win_info.win_height)
        self.setWindowOpacity(.10)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_F5:
            self.close()