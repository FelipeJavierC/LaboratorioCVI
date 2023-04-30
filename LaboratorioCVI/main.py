import csv

import InterfazMenuCliente
from Cliente import Cliente
from Mascota import Mascota

cliente = Cliente
id = None

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


def Ventana():
    InterfazMenuCliente.MenuCliente().mostrar()
def main():
    Ventana()

if __name__ == '__main__':
    main()