class Horario:
    def __init__(self, tipo_examen, fecha,hora):
        self._tipo_examen = tipo_examen
        self._fecha = fecha
        self._hora = hora

    @property
    def horario(self):
        return self._hora

    @property
    def fecha(self):
        return self._fecha

    def toStringHorario(self):
        return f"{self._fecha}",f"{self._tipo_examen}",f"{self._hora}"