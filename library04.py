from multimethod import multimethod
from PyQt6 import QtGui
from PyQt6.QtCore import Qt

# Clase Geometrica, metaclase

class Geometica:

    def __init__(self,painter:QtGui.QPainter, x, y):
        self.x = x
        self.y = y
        self.painter = painter
        print(f"Se ha creado una figura geometrica en la posicion ({self.x},{self.y}) ")
        
    
        
# Clase Circulo hereda de Geometrica

class Circulo(Geometica):
    
    def __init__(self,painter:QtGui.QPainter, x, y, radio):
        super().__init__(painter,x,y)    
        self.radio = radio
        
    @multimethod    
    def dibujar(self):
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)

    @multimethod    
    def dibujar(self, color:Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawEllipse(self.x-self.radio,self.y-self.radio,self.radio*2,self.radio*2)


# Clase Circulo hereda de Geometrica

class Cuadrado(Geometica):
    
    def __init__(self,painter:QtGui.QPainter, x, y, lado):
        super().__init__(painter,x,y)    
        self.lado = lado
        
    @multimethod    
    def dibujar(self, color:Qt.GlobalColor):
        self.painter.setBrush(color)
        self.painter.drawRect(self.x,self.y,self.lado,self.lado)

    @multimethod    
    def dibujar(self):
        self.painter.setBrush(self)
        self.painter.drawRect(self.x,self.y,self.lado,self.lado)
