class Mascota:

    def __init__(self,id,nombre,especie,raza,fecha_nacimiento,sexo,peso,tamaño):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._peso = peso
        self._tamaño = tamaño

    def toStringMascota(self):
        return f"{self._id}",f"{self._nombre}",f"{self._especie}",f"{self._raza}",f"{self._fecha_nacimiento}",f"{self._sexo}",f"{self._peso}",f"{self._tamaño}"

    @property
    def raza(self):
        return self._raza

    @property
    def fechaNacimiento(self):
        return self._fecha_nacimiento

    @property
    def sexo(self):
        return self._sexo

    @property
    def peso(self):
        return self._peso

    @property
    def tamaño(self):
        return self._tamaño

    @property
    def nombreM(self):
        return self._nombre

    @property
    def especie(self):
        return self._especie

    def cambiarPeso(self,peso):
        self._peso = peso

    def cambiarTamaño(self,tamaño):
        self._tamaño = tamaño