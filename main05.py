import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QTimer
import library05

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.leer_json()

    def leer_json(self):
        with open('figuras.json') as file:
            data = json.load(file)
            for figura in data['geometricas']:
                self.dibuja_figura(figura)

    def dibuja_figura(self,json_fig):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        if 'circulo' in json_fig:
            cir=json_fig["circulo"]
            figura=library05.Circulo(painter,cir["x"],cir["y"],cir["radio"])
            figura.dibujar()
        elif 'cuadrado' in json_fig:
            cuad=json_fig["cuadrado"]
            figura=library05.Cuadrado(painter,cuad["x"],cuad["y"],cuad["lado"])
            figura.dibujar()
        else:
            print("No se reconoce la figura {}".format(json_fig))
        painter.end()      
        self.label.setPixmap(canvas)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()