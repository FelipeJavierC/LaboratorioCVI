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


    def agregarMascotas(self,mascota):
        self._mascotas.append(mascota)

    @property
    def rut(self):
        return self._rut

    @property
    def nombres(self):
        return self._nombres

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @property
    def genero(self):
        return self._genero

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @property
    def domicilio(self):
        return self._domicilio

    @property
    def nombreCompleto(self):
        return f"{self._nombres} {self._apellido_paterno} {self._apellido_materno}"

    @property
    def mascotas(self):
        return self._mascotas

    def cambiarEmail(self, email):
        self._email = email

    def cambiarTelefono(self,telefono):
        self._telefono = telefono

    def cambiarDomicilio(self,domicilio):
        self._domicilio = domicilio

    def cambiarDerivado(self,clinica_derivado):
        self._clinica_derivado = clinica_derivado

    @property
    def clinica_derivado(self):
        return self._clinica_derivado