import sys
import random as rr
from PyQt5.QtGui import QPainter, QColor

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from name import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r = rr.randint(0, 255)
        g = rr.randint(0, 255)
        b = rr.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(x1, y1, n, n)

    def drawf(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())