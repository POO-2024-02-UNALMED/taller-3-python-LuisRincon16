from marca import Marca
from control import Control

class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca: Marca = marca
        self._estado: bool = estado
        self._canal: int = 1
        self._precio: int = 500
        self._volumen: int = 1
        self._control: Control
        self.tvCreados()

    @classmethod
    def tvCreados(cls):
        cls.numTV = cls.numTV + 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def setMarca(self, marc: Marca):
        self._marca = marc
    def getMarca(self):
        return self._marca

    def setCanal(self, can):
        self._canal = can
    def getCanal(self):
        return self._canal
        
    def setPrecio(self, prec):
        self._precio = prec
    def getPrecio(self):
        return self._precio
        
    def setVolumen(self, vol):
        self._volumen = vol
    def getVolumen(self):
        return self._volumen
        
    def setControl(self, contr: Control):
        self._control = contr
    def getControl(self):
        return self._control
    
