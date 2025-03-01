import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.setBrush(QtGui.QColor(QtCore.Qt.GlobalColor.red))
        painter.drawEllipse(100, 100, 200, 100)
        painter.setBrush(QtGui.QColor(QtCore.Qt.GlobalColor.blue))
        painter.drawEllipse(0, 0, 20, 20)
        # draw 3 green thick lines
        painter.setPen(QtGui.QPen(QtGui.QColor(QtCore.Qt.GlobalColor.green), 3))
        painter.drawLine(10, 10, 100, 100)
        painter.drawLine(10, 100, 100, 10)
        painter.drawLine(10, 10, 10, 100)
        painter.end()
        
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()