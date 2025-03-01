from multimethod import multimethod
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
class Circulo:
    def __init__(self,painter:QtGui.QPainter, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio
        self.painter = painter
        print(f"Se ha creado un círculo en la posición ({self.x},{self.y}) con radio {self.radio}")
        
    @multimethod
    def dibujar(self):
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)
    
    @multimethod    
    def dibujar(self, color:Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)
        
