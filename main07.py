import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QTimer
import library05
import urllib.request

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(800, 800)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.leer_json()

    def leer_json(self):
        with urllib.request.urlopen("http://localhost:8000/figuras_random") as url:
            data = json.load(url)
            print(data)
            for figura in data:
                self.dibuja_figura(figura)

    def dibuja_figura(self,json_fig):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        if json_fig["nombre"] == "circulo":
            figura=library05.Circulo(painter,json_fig["x"],json_fig["y"],json_fig["medida"])
            figura.dibujar()
        elif json_fig["nombre"] == 'cuadrado':
            figura=library05.Cuadrado(painter,json_fig["x"],json_fig["y"],json_fig["medida"])
            figura.dibujar()
        else:
            print("No se reconoce la figura {}".format(json_fig))
        painter.end()      
        self.label.setPixmap(canvas)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()