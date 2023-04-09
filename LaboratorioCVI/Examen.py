class Examen:
    def __init__(self,id,tipo,nombre_cliente,nombre_mascota,especie_mascota,hora,precio,cantidad,estado,resultado):
        self._id = id
        self._tipo = tipo
        self._nombre_cliente = nombre_cliente
        self._nombre_mascota = nombre_mascota
        self._especie_mascota = especie_mascota
        self._hora = hora
        self._precio = precio
        self._cantidad = cantidad
        self._resultado = resultado
        self._estado = estado

    def devolverPrecio(self):
        return self._precio

    def devolverTipo(self):
        return self._tipo

    def devolverCantidad(self):
        return self._cantidad

    @property
    def tipo(self):
        return self._tipo

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    def toStringExamen(self):
        return f"{self._id}",f"{self._tipo}",f"{self._nombre_cliente}",f"{self._nombre_mascota}",f"{self._especie_mascota}",\
            f"{self._hora}",f"{self._precio}",f"{self._cantidad}",f"{self._estado}",f"{self._resultado}"

    def cambiarEstado(self):
        self._estado = "True"


    def cambiarResultado(self,resultado):
        self._resultado = resultado

    def resultado(self):
        return self._resultado

    def estado(self):
        return self._estado