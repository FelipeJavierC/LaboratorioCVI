class Examen:
    def __init__(self,id,tipo,nombre_cliente,nombre_mascota,hora,precio,estado,resultado,apellido_paterno,apellido_materno,fecha):
        self._id = id
        self._tipo = tipo
        self._nombre_cliente = nombre_cliente
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._nombre_mascota = nombre_mascota
        self._hora = hora
        self._fecha = fecha
        self._precio = precio
        self._resultado = resultado
        self._estado = estado

    @property
    def tipo(self):
        return self._tipo

    @property
    def nombreCliente(self):
        return self._nombre_cliente

    @property
    def apellidoP(self):
        return self._apellido_paterno

    @property
    def apellidoM(self):
        return self._apellido_materno

    @property
    def mascota(self):
        return self._nombre_mascota

    @property
    def hora(self):
        return self._hora

    @property
    def fecha(self):
        return self._fecha

    @property
    def precio(self):
        return self._precio

    def toStringExamen(self):
        return f"{self._id}",f"{self._tipo}",f"{self._nombre_cliente}",f"{self._apellido_paterno}",f"{self._apellido_materno}",f"{self._nombre_mascota}",\
            f"{self._hora}",f"{self._fecha}",f"{self._precio}",f"{self._estado}",f"{self._resultado}"

    def cambiarEstado(self):
        self._estado = "True"


    def cambiarResultado(self,resultado):
        self._resultado = resultado

    @property
    def resultado(self):
        return self._resultado

    @property
    def estado(self):
        return self._estado