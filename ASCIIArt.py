from ascii_art import ASCIIArt, ASCIIPicture
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from pathlib import Path
from PIL import Image

p = str(Path(__file__).parent)


class ASCIIArtWin(QMainWindow):
    def __init__(self, parent=None):
        super(ASCIIArtWin, self).__init__(parent)
        self.resize(900, 600)
        self.setWindowTitle("ASCII Arts")
        self.origin_pixmap = Image.new("RGBA", (1, 1))
        self.ascii_pixmap = Image.new("RGBA", (1, 1))
        self.origin_img = QLabel(self)
        self.ascii_img = QLabel(self)
        self.path = ""
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.file = QMenu(self.menuBar)
        self.file.setTitle("文件")
        self.open = QAction(self.file)
        self.open.setText("打开")
        self.open.setShortcut("⌘O")
        self.open.triggered.connect(self.open_)
        self.file.addAction(self.open)
        self.save = QAction(self.file)
        self.save.setText("保存")
        self.save.setShortcut("⌘S")
        self.file.addAction(self.save)
        self.save_as = QAction(self.file)
        self.save_as.setText("另存为")
        self.save_as.setShortcut("⇧⌘S")
        self.file.addAction(self.save_as)
        self.menuBar.addMenu(self.file)
        self.curve = QSlider(self)
        self.curve.valueChanged.connect(self.curve_)
        self.curve.setMinimum(0)
        self.curve.setValue(20)
        self.curve.setMaximum(50)
        self.curve.setSingleStep(1)
        self.curve.setOrientation(Qt.Horizontal)
        self.changed = False
        self.timer = QBasicTimer()
        self.timer.start(1, self)

    def timerEvent(self, event: QTimerEvent) -> None:
        if self.changed:
            self.origin_pixmap = Image.open(self.path)
            picture = ASCIIArt(self.path, 5).draw_color_ascii(curve=self.curve.value() / 10)
            self.ascii_pixmap = ASCIIPicture(picture).img
            self.resizeEvent(QResizeEvent)
            self.changed = False

    def open_(self):
        self.path = str(QFileDialog.getOpenFileName(self, "打开文件", p, "静态图片文件 (*.png *.jpg *.jpeg)")[0])
        self.changed = True

    def curve_(self):
        if not self.path == "":
            self.changed = True

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.curve.setGeometry(5, self.height() - 25, int(self.width() / 3), 20)
        self.origin_img.setGeometry(0, 0, int(self.width() / 2),
                                    int(self.height() / 2))
        self.ascii_img.setGeometry(int(self.width() / 2), 0, int(self.width() / 2),
                                   int(self.height() / 2))
        self.origin_img.setPixmap(self.origin_pixmap.resize((self.origin_img.width(), 
                                                             self.origin_img.height())).toqpixmap())
        self.ascii_img.setPixmap(self.ascii_pixmap.resize((self.ascii_img.width(),
                                                           self.ascii_img.height())).toqpixmap())


app = QApplication()
yee = ASCIIArtWin()
yee.show()
app.exec()
