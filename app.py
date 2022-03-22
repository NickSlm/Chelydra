from screeninfo import get_monitors
from PyQt5.QtWidgets import QApplication
from dataClass import WindowInfo
from overlay import Overlay
import sys
import keyboard

def main():
    win_info = WindowInfo()
    # Get monitor size
    for m in get_monitors():
        win_info.win_x,win_info.win_y,win_info.win_width,win_info.win_height = m.x,m.y,m.width,m.height
    app = QApplication(sys.argv)
    window = Overlay(win_info)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()