#from televisores.marca import Marca
#from televisores.control import Control
from __future__ import annotations

class TV:
    _numTV = 0
    def __init__(self, marca: Marca, estado: bool):
        self._marca: Marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control: Control = None
        TV._numTV = TV._numTV + 1

    @classmethod
    def setNumTV(cls, numTeles):
        cls._numTV = numTeles


    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
                                    #subir o bajar canales
    def canalUp(self):
        cana = self._canal + 1
        self.setCanal(cana)
    
    def canalDown(self):
        cana = self._canal - 1
        self.setCanal(cana)
                                        #subir o bajar volumen
    def volumenUp(self):
        vol = self._volumen + 1
        self.setVolumen(vol)

    def volumenDown(self):
        vol = self.volumen - 1
        self.setVolumen(vol)

    def setMarca(self, marc: Marca):
        self._marca = marc
    def getMarca(self) -> Marca:
        return self._marca

    def setCanal(self, can):
        if self._estado == True and can >= 1 and can <= 120:
            self.canal = can
        
    def getCanal(self):
        return self._canal
        
    def setPrecio(self, prec):
        self._precio = prec
    def getPrecio(self):
        return self._precio
        
    def setVolumen(self, vol):
        if self._estado == True and vol >= 0 and vol <= 7:
            self._volumen = vol

    def getVolumen(self):
        return self._volumen
        
    def setControl(self, contr: Control):
        self._control = contr
    def getControl(self) -> Control:
        return self._control
    
