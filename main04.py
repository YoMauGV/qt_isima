import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
import library05

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
        cir=library05.Circulo(painter,10,10,10)
        cir.dibujar()
        cir2=library05.Circulo(painter,200,20,20)
        cir2.dibujar(Qt.GlobalColor.red)
        cuad=library05.Cuadrado(painter,200,200,50)
        cuad.dibujar(Qt.GlobalColor.blue)
        
        painter.end()
        
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()