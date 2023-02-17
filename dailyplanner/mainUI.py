# -*- coding: utf-8 -*-
#
# ░░░░░░░░░░░▄███▄▄▄░░░░░░░░
# ░░░░░░░▄▄▄██▀▀▀▀███▄░░░░░░
# ░░░░░▄▀▀░░░░░░░░░░░▀█░░░░░
# ░░▄▄▀░░░░░░░░░░░░░░░▀█░░░░
# ░░█░░░░░▀▄░░▄▀░░░░░░░░█░░░
# ░░▐██▄░░▀▄▀▀▄▀░░▄██▀░▐▌░░░
# ░░█▀█░▀░░░▀▀░░░▀░█▀░░▐▌░░░
# ░░█░░▀▐░░░░░░░░▌▀░░░░░█░░░
# ░█░░░░░░░░░░░░░░░░░░░█░░░░
# ░░█░░▀▄░░░░▄▀░░░░░░░░█░░░░
# ░░█░░░░░░░░░░░▄▄░░░░█░░░░░
# ░░░█▀██▀▀▀▀██▀░░░░░░█░░░░░
# ░░░█░░▀████▀░░░░░░░█░░░░░░
# ░░░░█░░░░░░░░░░░░▄█░░░░░░░
# ░░░░░██░░░░░█▄▄▀▀░█░░░░░░░
# ░░░░░░▀▀█▀▀▀▀░░░░░░█░░░░░░
# ░░░░░░░█░░░░░░░░░░░░█░░░░░
# yee~

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import datetime
from qt_material import *

import sys
from pathlib import Path

p = str(Path(__file__).parent)


class Event(QFrame):
    def __init__(self, parent=None):
        super(Event, self).__init__(parent)
        self.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self)
        self.title.setStyleSheet("font:20px")

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.title.setGeometry(4, 2, self.width() - 8, 20)

    def setColor(self, rgb: str):
        self.setStyleSheet("background-color:" + rgb)

    def setTitle(self, title: str):
        self.title.setText(title)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.resize(w, h)
        self.setWindowTitle("规划器主页")
        self.setMinimumSize(400, 200)
        apply_stylesheet(self, "dark_red.xml")
        self.timeAxisView = QScrollArea(self)
        self.timeAxisWidget = QWidget(self)
        self.timeAxisView.setWidget(self.timeAxisWidget)
        self.timeAxis = QProgressBar(self.timeAxisWidget)
        self.timeAxis.setMinimum(0)
        self.timeAxis.setMaximum(86399)
        self.timeAxis.setOrientation(Qt.Vertical)
        self.timeAxis.setInvertedAppearance(True)
        self.timeScaleSlider = QScrollBar(self)
        self.timeScaleSlider.setOrientation(Qt.Horizontal)
        self.timeScaleSlider.setRange(0, 4)
        self.timeScaleSlider.valueChanged.connect(self.scaleEvent)
        self.timeScaleLabel = QLabel(self)
        self.h1 = QLabel(self.timeAxisWidget)
        self.h1.setText("__01:00")
        self.h1.setStyleSheet("font:10px")
        self.h1.setAlignment(Qt.AlignBottom)
        self.h2 = QLabel(self.timeAxisWidget)
        self.h2.setText("__02:00")
        self.h2.setStyleSheet("font:10px")
        self.h2.setAlignment(Qt.AlignBottom)
        self.h3 = QLabel(self.timeAxisWidget)
        self.h3.setText("__03:00")
        self.h3.setStyleSheet("font:10px")
        self.h3.setAlignment(Qt.AlignBottom)
        self.h4 = QLabel(self.timeAxisWidget)
        self.h4.setText("__04:00")
        self.h4.setStyleSheet("font:10px")
        self.h4.setAlignment(Qt.AlignBottom)
        self.h5 = QLabel(self.timeAxisWidget)
        self.h5.setText("__05:00")
        self.h5.setStyleSheet("font:10px")
        self.h5.setAlignment(Qt.AlignBottom)
        self.h6 = QLabel(self.timeAxisWidget)
        self.h6.setText("__06:00")
        self.h6.setStyleSheet("font:10px")
        self.h6.setAlignment(Qt.AlignBottom)
        self.h7 = QLabel(self.timeAxisWidget)
        self.h7.setText("__07:00")
        self.h7.setStyleSheet("font:10px")
        self.h7.setAlignment(Qt.AlignBottom)
        self.h8 = QLabel(self.timeAxisWidget)
        self.h8.setText("__08:00")
        self.h8.setStyleSheet("font:10px")
        self.h8.setAlignment(Qt.AlignBottom)
        self.h9 = QLabel(self.timeAxisWidget)
        self.h9.setText("__09:00")
        self.h9.setStyleSheet("font:10px")
        self.h9.setAlignment(Qt.AlignBottom)
        self.h10 = QLabel(self.timeAxisWidget)
        self.h10.setText("__10:00")
        self.h10.setStyleSheet("font:10px")
        self.h10.setAlignment(Qt.AlignBottom)
        self.h11 = QLabel(self.timeAxisWidget)
        self.h11.setText("__11:00")
        self.h11.setStyleSheet("font:10px")
        self.h11.setAlignment(Qt.AlignBottom)
        self.h12 = QLabel(self.timeAxisWidget)
        self.h12.setText("__12:00")
        self.h12.setStyleSheet("font:10px")
        self.h12.setAlignment(Qt.AlignBottom)
        self.h13 = QLabel(self.timeAxisWidget)
        self.h13.setText("__13:00")
        self.h13.setStyleSheet("font:10px")
        self.h13.setAlignment(Qt.AlignBottom)
        self.h14 = QLabel(self.timeAxisWidget)
        self.h14.setText("__14:00")
        self.h14.setStyleSheet("font:10px")
        self.h14.setAlignment(Qt.AlignBottom)
        self.h15 = QLabel(self.timeAxisWidget)
        self.h15.setText("__15:00")
        self.h15.setStyleSheet("font:10px")
        self.h15.setAlignment(Qt.AlignBottom)
        self.h16 = QLabel(self.timeAxisWidget)
        self.h16.setText("__16:00")
        self.h16.setStyleSheet("font:10px")
        self.h16.setAlignment(Qt.AlignBottom)
        self.h17 = QLabel(self.timeAxisWidget)
        self.h17.setText("__17:00")
        self.h17.setStyleSheet("font:10px")
        self.h17.setAlignment(Qt.AlignBottom)
        self.h18 = QLabel(self.timeAxisWidget)
        self.h18.setText("__18:00")
        self.h18.setStyleSheet("font:10px")
        self.h18.setAlignment(Qt.AlignBottom)
        self.h19 = QLabel(self.timeAxisWidget)
        self.h19.setText("__19:00")
        self.h19.setStyleSheet("font:10px")
        self.h19.setAlignment(Qt.AlignBottom)
        self.h20 = QLabel(self.timeAxisWidget)
        self.h20.setText("__20:00")
        self.h20.setStyleSheet("font:10px")
        self.h20.setAlignment(Qt.AlignBottom)
        self.h21 = QLabel(self.timeAxisWidget)
        self.h21.setText("__21:00")
        self.h21.setStyleSheet("font:10px")
        self.h21.setAlignment(Qt.AlignBottom)
        self.h22 = QLabel(self.timeAxisWidget)
        self.h22.setText("__22:00")
        self.h22.setStyleSheet("font:10px")
        self.h22.setAlignment(Qt.AlignBottom)
        self.h23 = QLabel(self.timeAxisWidget)
        self.h23.setText("__23:00")
        self.h23.setStyleSheet("font:10px")
        self.h23.setAlignment(Qt.AlignBottom)
        self.h24 = QLabel(self.timeAxisWidget)
        self.h24.setText("__24:00")
        self.h24.setStyleSheet("font:10px")
        self.h24.setAlignment(Qt.AlignBottom)
        self.currentTime = QFrame(self.timeAxisWidget)
        self.currentTime.setFrameShape(QFrame.HLine)
        self.currentTimeLabel = QLabel(self.timeAxisWidget)
        self.currentTimeLabel.setStyleSheet("font:10px")
        self.currentTimeLabel.setAlignment(Qt.AlignRight)
        self.timer = QBasicTimer()
        self.timer.start(1, self)

    def timerEvent(self, event: QTimerEvent) -> None:
        self.timeAxis.setValue(int(datetime.datetime.now().second) + int(datetime.datetime.now().minute * 60) +
                               int(datetime.datetime.now().hour * 3600))
        self.currentTime.setGeometry(0, int(int(self.timeAxisWidget.height() / 24) * 24 / 86400 *
                                            self.timeAxis.value()),
                                     self.timeAxisWidget.width(), 2)
        self.currentTimeLabel.setGeometry(0, int(int(self.timeAxisWidget.height() / 24) * 24 / 86400 *
                                                 self.timeAxis.value() - 10),
                                          self.timeAxisWidget.width(), 10)
        if int(datetime.datetime.now().hour) < 10:
            self.currentTimeLabel.setText("0" + str(datetime.datetime.now().hour) +
                                          ":" + str(datetime.datetime.now().minute))
        else:
            self.currentTimeLabel.setText(str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))

    def scaleEvent(self):
        if self.timeScaleSlider.value() == 4:
            self.timeAxisWidget.setGeometry(0, 0, int(self.width() * 2 / 3) - 10, int(self.height() * 2 / 3))
            self.timeScaleLabel.setText("比例尺：天")
        elif self.timeScaleSlider.value() == 3:
            self.timeAxisWidget.setGeometry(0, 0, int(self.width() * 2 / 3) - 10, int(self.height() * 4 / 3))
            self.timeScaleLabel.setText("比例尺：1/2天")
        elif self.timeScaleSlider.value() == 2:
            self.timeAxisWidget.setGeometry(0, 0, int(self.width() * 2 / 3) - 10, int(self.height() * 8 / 3))
            self.timeScaleLabel.setText("比例尺：1/4天")
        elif self.timeScaleSlider.value() == 1:
            self.timeAxisWidget.setGeometry(0, 0, int(self.width() * 2 / 3) - 10, int(self.height() * 24 / 3))
            self.timeScaleLabel.setText("比例尺：时")
        elif self.timeScaleSlider.value() == 0:
            self.timeAxisWidget.setGeometry(0, 0, int(self.width() * 2 / 3) - 10, int(self.height() * 48 / 3))
            self.timeScaleLabel.setText("比例尺：1/2时")
        self.timeAxis.setGeometry(0, 0, 5, int(self.timeAxisWidget.height() / 24) * 24)
        self.h1.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 0 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h2.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 1 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h3.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 2 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h4.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 3 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h5.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 4 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h6.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 5 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h7.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 6 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h8.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 7 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h9.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 8 + 1, 100,
                            int(self.timeAxisWidget.height() / 24))
        self.h10.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 9 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h11.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 10 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h12.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 11 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h13.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 12 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h14.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 13 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h15.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 14 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h16.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 15 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h17.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 16 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h18.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 17 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h19.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 18 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h20.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 19 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h21.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 20 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h22.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 21 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h23.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 22 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))
        self.h24.setGeometry(5, int(self.timeAxisWidget.height() / 24) * 23 + 1, 100,
                             int(self.timeAxisWidget.height() / 24))

    def showEvent(self, event: QShowEvent) -> None:
        self.timeScaleSlider.setValue(2)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.timeAxisView.setGeometry(0, 0, int(self.width() * 2 / 3), int(self.height() * 2 / 3))
        self.timeScaleSlider.setGeometry(int(self.width() * 2 / 3) - 40 - int(self.width() * 2 / 12), 0,
                                         int(self.width() * 2 / 12) + 20, 20)
        self.timeScaleLabel.setGeometry(int(self.width() * 2 / 3) - 40 - int(self.width() * 2 / 12), 20, 150, 20)
        self.scaleEvent()


app = QApplication(sys.argv)
desktop = app.instance()
screenRect = desktop.screens()[0].size()
w = screenRect.width()
h = screenRect.height()
root = UI()
root.show()
app.exec()
