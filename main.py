import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_figures()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_figures(self):
        x = randint(50, 600)
        y = randint(50, 600)
        d = randint(20, 200)
        self.qp.setBrush(QColor(randint(0,256), randint(0,256), randint(0,256)))
        self.qp.drawEllipse(x - d, y - d, d * 2, d * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())