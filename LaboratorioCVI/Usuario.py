class Usuario:

    def __init__(self,rut,email,clave,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,cargo):
        self._email = email
        self._clave = clave
        self._nombres = nombres
        self._apellido_materno = apellido_materno
        self._apellido_paterno = apellido_paterno
        self._genero = genero
        self._fecha_nacimiento = fecha_nacimiento
        self._rut = rut
        self._cargo = cargo
    @property
    def email(self):
        return self._email
    @property
    def clave(self):
        return self._clave

    def toStringUsuario(self):
        return f"{self._rut}",f"{self._email}",f"{self._clave}",f"{self._nombres}",f"{self._apellido_paterno}",f"{self._apellido_materno}",\
            f"{self._genero}",f"{self._fecha_nacimiento}",f"{self._cargo}"