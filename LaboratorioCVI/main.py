import csv

import InterfazInicioSesion
from Cliente import Cliente
from Examen import Examen
from Horario import Horario
from Mascota import Mascota
from Usuario import Usuario

cliente = Cliente
id = None
usuario = Usuario
usuarioedit = Usuario
horarios = []
examenes = []

def cargarDatosMascota(rut):
    with open('Mascotas.csv') as file:
        reader = csv.reader(file,delimiter=',')
        mascotas = []
        for row in reader:
            if len(row) != 0:
                datos = format(row[0])
                if rut == datos:
                    mascota = Mascota(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),format(row[7]))
                    mascotas.append(mascota)
    return mascotas

def borrarMascota(nombre):
    nombre = nombre.lower()
    with open('Mascotas.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                rut = format(row[0])
                name = format(row[1])
                name = name.lower()
                if id == rut and nombre == name:
                    break
            i += 1
    with open('Mascotas.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def borrarMascotas():
    with open('Mascotas.csv') as file:
        mascotas = []
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                rut = format(row[0])
                if id == rut:
                    mascotas.append(i)
            i += 1
    with open('Mascotas.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in mascotas:
                file.write(line)

def borrarUsuario():
    with open('Usuarios.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                rut = format(row[0])
                if usuarioedit.rut == rut:
                    break
            i += 1
    with open('Usuarios.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def borrarCliente():
    with open('Clientes.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                rut = format(row[0])
                if id == rut:
                    break
            i += 1
    with open('Clientes.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def cargarDatosCliente(rut,mascotas):
    global id
    id = rut
    with open('Clientes.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                datos = format(row[0])
                if rut == datos:
                    print ("Cliente Encontrado")
                    print("------------------------------")
                    global cliente
                    cliente = Cliente(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                      format(row[7]),format(row[8]),format(row[9]),mascotas)
                    return cliente
    return False

def BuscarMascota(nombre):
    nombre = nombre.lower()
    with open('Mascotas.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                rut = format(row[0])
                name = format(row[1])
                name = name.lower()
                if id == rut and nombre == name:
                    mascota = Mascota(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),format(row[7]))
                    return mascota
    return False

def guardarDatos(archivo,lista):
    with open(archivo,'a', newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(lista)

def crearMascota(nombre, especie, raza, fecha_nacimiento, sexo, peso, tamaño):
    mascota = Mascota(id, nombre, especie, raza, fecha_nacimiento, sexo, peso, tamaño)
    cliente.agregarMascotas(mascota)
    guardarDatos('Mascotas.csv',mascota.toStringMascota())

def crearCliente(rut, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, email, telefono, domicilio, clinica_derivado):
    mascotas = []
    global cliente
    global id
    id=rut
    cliente = Cliente(rut,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,email,telefono,domicilio,clinica_derivado,mascotas)
    guardarDatos('Clientes.csv', cliente.toStringCliente())

def crearExamen(nombres,apellidoP,apellidoM,mascota,tipo,fecha,hora,precio):
    global id
    examen = Examen(id,tipo,nombres,mascota,hora,precio,"False","",apellidoP,apellidoM,fecha)
    horario = Horario(tipo,fecha,hora)
    guardarDatos('Horario.csv', horario.toStringHorario())
    examenes.append(examen)
    horarios.append(horario)

def editarExamen(nombres,apellidoP,apellidoM,mascota,tipo,fecha,hora,precio,resultado,estado):
    global id
    examen = Examen(id,tipo,nombres,mascota,hora,precio,estado,resultado,apellidoP,apellidoM,fecha)
    horario = Horario(tipo,fecha,hora)
    guardarDatos('Horario.csv', horario.toStringHorario())
    guardarDatos('Examenes.csv', examen.toStringExamen())


def borrarHorario(hora,fecha):
    with open('Horario.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                date = format(row[0])
                hour = format(row[2])
                if date == fecha and hour == hora:
                    break
            i += 1
    with open('Horario.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def borrarExamen(hora,fecha):
    with open('Examenes.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                date = format(row[7])
                hour = format(row[6])
                if date == fecha and hour == hora:
                    break
            i += 1
    with open('Examenes.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def borrarHorarios():
    for x in horarios:
        with open('Horario.csv') as file:
            reader = csv.reader(file, delimiter=',')
            i = 0
            for row in reader:
                if len(row) != 0:
                    fecha = format(row[0])
                    hora = format(row[2])
                    if x.fecha == fecha and x.horario == hora:
                        break
                i += 1
        with open('Horario.csv', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for number, line in enumerate(lines):
                if number not in [i]:
                    file.write(line)

def cargarDatosUsuario(email,contraseña):
    global usuario
    with open('Usuarios.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                emails = format(row[1])
                contraseñas = format(row[2])
                if email == emails and contraseña == contraseñas:
                    usuario = Usuario(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                      format(row[7]),format(row[8]))
                    return usuario
    return False

def buscarUsuario(rut):
    global usuarioedit
    with open('Usuarios.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                datos = format(row[0])
                if rut == datos:
                    usuarioedit = Usuario(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                      format(row[7]),format(row[8]))
                    return usuarioedit
    return False

def verifDispo(tipo_examen,fecha):
    horario = ["9:00","10:30","12:00","15:00","16:30"]
    with open('Horario.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if len(row) != 0:
                tipo = format(row[1])
                date = format(row[0])
                if tipo_examen == tipo and fecha == date:
                    for i in horario:
                        if i == format(row[2]):
                            horario.remove(i)
    return horario

def descuento(precio):
    mascotas = []
    descuento=0
    for i in examenes:
        mascotas.append(i.mascota)
    if len(mascotas)>1:
        for j in range(len(mascotas)):
            if j != 0:
                if mascotas[0] != mascotas[j]:
                    print(precio)
                    descuento += precio*0.2
                    break
    if cliente.clinica_derivado == "Clinica CVI":
        descuento += precio*0.7

    return descuento

def guardarExamenes():
    for i in examenes:
        guardarDatos('Examenes.csv', i.toStringExamen())

def cargarDatosExamen():
    with open('Examenes.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                ids = format(row[0])
                if id == ids:
                    print("Examen encontrado")
                    print("------------------------------")
                    examen = Examen(format(row[0]),format(row[1]),format(row[2]),format(row[5]),format(row[6]),format(row[8]),format(row[9]),
                                    format(row[10]),format(row[3]),format(row[4]),format(row[7]))
                    examenes.append(examen)

def buscarExamen(hora,fecha):
    with open('Examenes.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                hour = format(row[6])
                date = format(row[7])
                if hour == hora and date == fecha:
                    print("Examen encontrado")
                    print("------------------------------")
                    examen = Examen(format(row[0]),format(row[1]),format(row[2]),format(row[5]),format(row[6]),format(row[8]),format(row[9]),
                                    format(row[10]),format(row[3]),format(row[4]),format(row[7]))
                    return examen
    return Examen


def crearUsuario(rut,email,clave,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,cargo):
    usuario = Usuario(rut,email,clave,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,cargo)
    guardarDatos('Usuarios.csv',usuario.toStringUsuario())

def Ventana():
    InterfazInicioSesion.InicioSesion().mostrar()

def main():
    Ventana()

if __name__ == '__main__':
    main()