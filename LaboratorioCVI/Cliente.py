class Cliente:

    def __init__(self,rut,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,email,telefono,domicilio,clinica_derivado,mascotas):
        self._nombres = nombres
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._genero = genero
        self._fecha_nacimiento = fecha_nacimiento
        self._rut = rut
        self._email = email
        self._telefono = telefono
        self._domicilio = domicilio
        self._clinica_derivado = clinica_derivado
        self._mascotas = mascotas


    def toStringCliente(self):
        lista = [f"{self._rut}",f"{self._nombres}",f"{self._apellido_paterno}",f"{self._apellido_materno}",
                 f"{self._genero}",f"{self._fecha_nacimiento}",f"{self._email}",f"{self._telefono}",f"{self._domicilio}",f"{self._clinica_derivado}"]
        return lista


    def agregarMascotas(self,mascotasAdd):
        for i in mascotasAdd:
            self._mascotas.append(i)
        return self._mascotas

    @property
    def nombres(self):
        return self._nombres

    @property
    def clinica_derivado(self):
        return self._clinica_derivado