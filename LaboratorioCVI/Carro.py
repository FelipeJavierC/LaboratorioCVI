class Carro:
    def __init__(self,examenes):
        self._subtotal = 0
        self._descuento = 0
        self._total = 0
        self._examenes = examenes

    def getSubtotal(self):
        for i in self._examenes:
            self._subtotal += int(i.precio)
        return self._subtotal

    def getdescuento(self,clinica):
        if len(self._examenes)>2:
            self._descuento += self._subtotal * 0.2
        if clinica == "Clinica Veterinaria":
            self._descuento += self._subtotal * 0.7
        return self._descuento

    def getTotal(self):
        self._total = self._subtotal - self._descuento
        return self._total

    @property
    def examenes(self):
        return self._examenes