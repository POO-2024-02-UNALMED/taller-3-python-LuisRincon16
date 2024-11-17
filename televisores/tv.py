from marca import Marca
from control import Control

class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca: Marca = marca
        self._estado: bool = estado
        self._canal: int = 1
        self._precio: int = 500
        self._volumen: int = 1
        self._control: Control = None
        TV.tvCreados()

    @classmethod
    def tvCreados(cls):
        cls._numTV = cls._numTV + 1

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
    def getMarca(self):
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
    def getControl(self):
        return self._control
    
