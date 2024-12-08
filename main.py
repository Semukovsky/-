import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import QRect, Qt

class Canvas(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.yellow, 2)
        painter.setPen(pen)
        for x, y, diameter in self.circles:
            painter.drawEllipse(QRect(x, y, diameter, diameter)) #fffff

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        old_canvas = self.findChild(QtWidgets.QFrame, "canvas")
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setGeometry(old_canvas.geometry())
        old_canvas.deleteLater()
        self.button.clicked.connect(self.canvas.add_circle)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
