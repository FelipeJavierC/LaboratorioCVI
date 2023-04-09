class Horario:
    def __init__(self,tipo_examen):
        self._tipo_examen = tipo_examen
        self._horas = ["9:00","10:00","11:00","12:00","15:00","16:00"]
        self._horasDisponibles = self._horas

    def desplegarhorario(self):
        i=0
        for h in self._horasDisponibles:
            i+=1
            print(f"{i}. {h}")
        if len(self._horasDisponibles)==0:
            print("No Hay Disponibilidad")
    def asignarHora(self,posicion):
        print("Hora Agregada")
        return self._horasDisponibles.pop(posicion-1)

    def horasDisponibles(self):
        return self._horasDisponibles

    def toStringHorario(self):
        return f"{self._tipo_examen}"f"{self._horas}",f"{self._horasDisponibles}"