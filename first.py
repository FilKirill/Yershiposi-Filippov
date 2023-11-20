import sys
import random as rr
import io
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPainterPath

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.qp = QPainter()
        self.setGeometry(300, 300, 1000, 1000)
        self.pushButton.clicked.connect(self.drawf)

    def paintEvent(self, event):
        if self.flag:
            # Создаем объект QPainter для рисования

            # Начинаем процесс рисования
            self.qp.begin(self)
            self.draw(self.qp)
            # Завершаем рисование
            self.qp.end()

    def create_color(self):
        r = 255
        g = 255
        b = 0
        return r, g, b

    def draw(self, qp):
        n = rr.randint(20, 808)
        x1 = rr.randint(20, 800)
        y1 = rr.randint(20, 500)
        color = self.create_color()
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x1, y1, n, n)

    def drawf(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
