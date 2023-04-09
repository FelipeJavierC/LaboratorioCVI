import csv
from Usuario import Usuario
from Cliente import Cliente
from Mascota import Mascota
from Examen import Examen
from Carro import Carro
from Horario import Horario

nombresM = []
especiesM = []
horario1 = Horario("Examen De Sangre")
horario2 = Horario("Secuenciamiento De Muestras Biologicas")
horario3 = Horario("Radiografia")
horario4 = Horario("Scanner Y Ecografia")

def borrarExamen(id,tipo):
    with open('Examenes.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                ids = format(row[0])
                tipos = format(row[1])
                if id == ids and tipo == tipos:
                    break
            i += 1
    with open('Examenes.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def borrarMascotas(dato):
    with open('Mascotas.csv') as file:
        reader = csv.reader(file, delimiter=',')
        i = 0
        for row in reader:
            if len(row) != 0:
                datos = format(row[0])
                if dato == datos:
                    break
            i += 1
    with open('Mascotas.csv','r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for number,line in enumerate(lines):
            if number not in [i]:
                file.write(line)

def guardarDatos(archivo,lista):
    with open(archivo,'a', newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(lista)

def cargarDatosExamen(id,tipo):
    with open('Examenes.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                ids = format(row[0])
                tipos = format(row[1])
                if id == ids and tipo == tipos:
                    print("Examen encontrado")
                    print("------------------------------")
                    examen = Examen(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                    format(row[7]),format(row[8]),format(row[9]))
                    return examen
    return False

def cargarDatosUsuario(email,contraseña):
    with open('Usuarios.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                emails = format(row[1])
                contraseñas = format(row[2])
                if email == emails and contraseña == contraseñas:
                    print ("Sesion Iniciada")
                    print("------------------------------")
                    usuario = Usuario(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                      format(row[7]),format(row[8]))
                    return usuario
    return False

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

def cargarDatosCliente(rut,mascotas):
    with open('Clientes.csv') as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            if len(row) != 0:
                datos = format(row[0])
                if rut == datos:
                    print ("Cliente Encontrado")
                    print("------------------------------")
                    cliente = Cliente(format(row[0]),format(row[1]),format(row[2]),format(row[3]),format(row[4]),format(row[5]),format(row[6]),
                                      format(row[7]),format(row[8]),format(row[9]),mascotas)
                    return cliente
    return False

def editarExamen():
    print("PorFavor Ingresar Los Siguientes Datos: ")
    print("---------------------------------------------------")
    id = input("Id(Rut): ")
    tipo = input("Tipo De Examen: ")
    examen = cargarDatosExamen(id,tipo)
    if examen == False:
        print("Examen No Encontrado")
    else:
        input("Enter Para Cambiar Estado A Finalizado")
        examen.cambiarEstado()
        print("Ingrese Resultado:")
        resultado = input()
        examen.cambiarResultado(resultado)
        borrarExamen(id,tipo)
        guardarDatos('Examenes.csv',examen.toStringExamen())

def buscarExamen():
    print("PorFavor Ingresar Los Siguientes Datos: ")
    print("---------------------------------------------------")
    id = input("Id(Rut): ")
    tipo = input("Tipo De Examen: ")
    examen = cargarDatosExamen(id,tipo)
    if examen == False:
        print("Examen No Encontrado")
    else:
        if examen.estado() == "True":
            print("Estado: Terminado")
            print(f"Resultado: {examen.resultado()}")
            input("Enter Para Imprimir")
            borrarExamen(id, tipo)
        else:
            print("Estado: En Proceso")
            input("Enter Para Volver Al Menu Principal")

def crearUsuario():
    print("[Crear Usuario]".center(50, "-"))
    print("PorFavor Ingresar Los Siguientes Datos Del Usuario:")
    print("---------------------------------------------------")
    nombres = input("Nombres: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    genero = input("Genero: ")
    fecha_nacimiento = input("Fecha De Nacimiento(00/00/0000): ")
    rut = input("Rut(00.000.000-0): ")
    email = input("Email: ")
    clave = input("Contraseña: ")
    cargo = input("Cargo: ")
    print("------------------------------")
    input("Enter Para Agregar Cliente")
    print("------------------------------")
    input("Enter Para Guardar Datos")
    print("------------------------------")
    usuario = Usuario(rut,email,clave,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,cargo)
    guardarDatos('Usuarios.csv',usuario.toStringUsuario())

def inicioSesion():
    print("[Iniciar Sesion]".center(50, "-"))
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    usuario = cargarDatosUsuario(email,contraseña)
    if usuario == False:
        print("---------------------------------------------------------")
        input("Email No Reconocido. Enter Para Volver Al Menu Principal.")
    else:
        menuGestioUsuario()

def menuGestioUsuario():
    print("[Gestion De Usuario]".center(50, "-"))
    while True:
        print("1.Crear Usuario")
        print("2.Editar Examen")
        opcion = int(input())

        if opcion == 1:
            crearUsuario()
            break
        elif opcion == 2:
            editarExamen()
            break
        else:
            print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
            print("--------------------------------------------------------")

def menuCarrito(carro):
    print("[Carro De Compras]".center(50, "-"))
    examenes = carro.examenes
    for j in examenes:
        print(f"Producto: {j.tipo} ")
        print(f"Cantidad: {j.cantidad}")
        print(f"Precio: {j.precio} ")
        print("------------------------------")
    print(f"Subtotal: {carro.getSubtotal()} ")
    print(f"Descuento: {carro.getdescuento()} ")
    print(f"Total: {carro.getTotal()}")
    print("------------------------------")
    input("Enter Para Proceder Al Pago")
    print("------------------------------")
    for i in examenes:
        guardarDatos('Examenes.csv',i.toStringExamen())
    nombresM.clear()
    especiesM.clear()

def agendarExamen(id,nombres):
    examenes = []
    while True:
        while True:
            print("Examenes".center(50,"-"))
            print("Seleccione Tipo De Examen: ")
            print("---------------------------")
            print("1.Examen De Sangre [25.000]")
            print("2.Secuenciamiento De Muestras Biologicas [20.000]")
            print("3.Radiografia [40.000]")
            print("4.Scanner Y Ecografia [30.000]")
            opcion = int(input())
            cantidad = int(input("Ingrese Cantidad: "))
            if opcion == 1:
                tipo_examen = "Examen De Sangre"
                precioExamen = 25000 * cantidad
                break
            elif opcion == 2:
                tipo_examen = "Secuenciamiento De Muestras Biologicas"
                precioExamen = 20000 * cantidad
                break
            elif opcion == 3:
                tipo_examen = "Radiografia"
                precioExamen = 40000 * cantidad
                break
            elif opcion == 4:
                tipo_examen = "Scanner Y Ecografia"
                precioExamen = 30000 * cantidad
                break
            else:
                print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                print("--------------------------------------------------------")

        print("Seleccione Horario: ")
        print("Disponibles: ")
        if tipo_examen == "Examen De Sangre":
            while True:
                horario1.desplegarhorario()
                if len(horario1.horasDisponibles()) > 0:
                    opcion = int(input())
                else:
                    break
                if 0 < opcion <= len(horario1.horasDisponibles()):
                    hora = horario1.asignarHora(opcion)
                    examen = Examen(id, tipo_examen, nombres, nombresM, especiesM, hora, precioExamen,cantidad,"False","")
                else:
                    print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                    print("--------------------------------------------------------")
                break
        elif tipo_examen == "Secuenciamiento De Muestras Biologicas":
            while True:
                horario2.desplegarhorario()
                if len(horario2.horasDisponibles())>0:
                    opcion = int(input())
                else:
                    break
                if 0<opcion<=len(horario2.horasDisponibles()):
                    hora = horario2.asignarHora(opcion)
                    examen = Examen(id, tipo_examen, nombres, nombresM, especiesM, hora, precioExamen,cantidad,"False","")
                else:
                    print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                    print("--------------------------------------------------------")
                break
        elif tipo_examen == "Radiografia":
            while True:
                horario3.desplegarhorario()
                if len(horario3.horasDisponibles()) > 0:
                    opcion = int(input())
                else:
                    break
                if 0 < opcion <= len(horario3.horasDisponibles()):
                    hora = horario3.asignarHora(opcion)
                    examen = Examen(id, tipo_examen, nombres, nombresM, especiesM, hora, precioExamen,cantidad,"False","")
                else:
                    print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                    print("--------------------------------------------------------")
                break
        elif tipo_examen == "Scanner Y Ecografia":
            while True:
                horario4.desplegarhorario()
                if len(horario4.horasDisponibles()) > 0:
                    opcion = int(input())
                else:
                    break
                if 0 < opcion <= len(horario4.horasDisponibles()):
                    hora = horario4.asignarHora(opcion)
                    examen = Examen(id, tipo_examen, nombres, nombresM, especiesM, hora, precioExamen, cantidad,"False","")
                else:
                    print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                    print("--------------------------------------------------------")
                break
        examenes.append(examen)
        print("Examen Agregado Al Carrito")
        print("Desea Agregar Otro Examen")
        print("1.Si")
        print("2.no")
        opcion = int(input())
        if opcion == 2:
            precioExamen = 0
            break
    carro = Carro(examenes)
    return carro

def crearMascota(rut):
    mascotas = []
    numeroMascota = int(input("Ingrese Numero De Mascotas: "))
    for i in range(numeroMascota):
        print(f"[Mascota {i+1}]".center(50,"-"))
        print("PorFavor Ingresar Los Siguientes Datos De La Mascota:")
        print("-----------------------------------------------------")
        nombre = input("Nombre: ")
        especie = input("Especie: ")
        raza = input("Raza: ")
        fecha_nacimiento = input("Fecha De Nacimiento: ")
        sexo = input("Sexo: ")
        peso = input("Peso(kg): ")
        tamaño = input("Tamaño(cm): ")
        id = rut
        print("------------------------------")
        input(f"Enter Para Agregar Mascota {i+1}")
        print("------------------------------")
        mascota = Mascota(id, nombre, especie, raza, fecha_nacimiento, sexo, peso, tamaño)
        guardarDatos('Mascotas.csv',mascota.toStringMascota())
        mascotas.append(mascota)
        nombresM.append(nombre)
        especiesM.append(especie)

    return mascotas

def buscarCliente():
    print("[Buscar Cliente]".center(50,"-"))
    print("PorFavor Ingresar Rut Del Cliente:")
    print("---------------------------------------------------")
    rut = input("Rut: ")
    mascotas = cargarDatosMascota(rut)
    cliente = cargarDatosCliente(rut,mascotas)
    if cliente == False:
        print("Cliente No Encontrado")
    else:
        while True:
            print("1.Agregar Mascota")
            print("2.Eliminar Mascota")
            print("3.Mantener Mascota")
            opcion = int(input())

            if opcion == 1:
                mascotasAdd = crearMascota(rut)
                mascotas = cliente.agregarMascotas(mascotasAdd)
                print("Sus Mascotas Son: ")
                for i in mascotas:
                    print(i.nombre)
                    nombresM.append(i.nombre)
                    especiesM.append(i.especie)
                break
            elif opcion == 2:
                print("Ingrese Nombre De La mascota a Eliminar")
                print("---------------------------------------------------")
                nombre = input()
                j=0
                for i in mascotas:
                    if nombre == i.nombre:
                        del mascotas[j]
                    j+=1
                borrarMascotas(nombre)
                print("Sus Mascotas Son: ")
                for i in mascotas:
                    print(i.nombre)
                    nombresM.append(i.nombre)
                    especiesM.append(i.especie)
                break
            elif opcion == 3:
                print("Sus Mascotas Son: ")
                for i in mascotas:
                    print(i.nombre)
                    nombresM.append(i.nombre)
                    especiesM.append(i.especie)
                break
            else:
                print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                print("--------------------------------------------------------")
        carro = agendarExamen(rut,cliente.nombres)
        menuCarrito(carro)

def crearCliente():
    print("[Crear Cliente]".center(50,"-"))
    print("PorFavor Ingresar Los Siguientes Datos Del Cliente:")
    print("---------------------------------------------------")
    nombres = input("Nombres: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    genero = input("Genero: ")
    fecha_nacimiento = input("Fecha De Nacimiento(00/00/0000): ")
    rut = input("Rut(00.000.000-0): ")
    email = input("Email: ")
    telefono = input("Telefono(+56 9 0000 0000): ")
    domicilio = input("Domicilio: ")
    clinica_derivado = input("Clinica De Derivacion: ")
    print("------------------------------")
    input("Enter Para Agregar Cliente")
    print("------------------------------")
    mascotas = crearMascota(rut)
    print("------------------------------")
    input("Enter Para Guardar Datos")
    print("------------------------------")
    cliente = Cliente(rut,nombres,apellido_paterno,apellido_materno,genero,fecha_nacimiento,email,telefono,domicilio,clinica_derivado,mascotas)
    guardarDatos('Clientes.csv',cliente.toStringCliente())
    carro = agendarExamen(rut,nombres)
    menuCarrito(carro)

def menuAgendarExamen():
    print("[Cliente]".center(50,"-"))
    while True:
        print("1.Buscar Cliente")
        print("2.Crear Cliente")
        opcion = int(input())

        if opcion == 1:
            buscarCliente()
            break
        elif opcion == 2:
            crearCliente()
            break
        else:
            print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
            print("--------------------------------------------------------")

def menuPrincipal():
    while True:
        print("[Laboratorio CVI]".center(50,"-"))

        while True:
            print("1.Agendar Examen")
            print("2.Gestion De Usuario")
            print("3.Buscar Examen")
            opcion = int(input())


            if opcion == 1:
                menuAgendarExamen()
                break
            elif opcion == 2:
                inicioSesion()
                break
            elif opcion == 3:
                buscarExamen()
                break
            else:
                print("Opcion Ingresada No valida. PorFavor Ingresar De Nuevo.")
                print("--------------------------------------------------------")

def main():
    menuPrincipal()
if __name__ == '__main__':
    main()