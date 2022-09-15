import os
import datetime
import sys
import time
from tqdm import tqdm
from time import sleep


reservaciones = {} #ID_RESERVACION(FOLIO), ID_SALA, ID_USUARIO, TURNO , FECHA_RESERVACION,NOMBRE DEL EVENTO
salas = {} #ID_SALA, CUPO, NOMBRE DE SALA,
usuarios = {} # ID_USUARIO, NOMBRE DE USUARIO,

id_usuario = 0
lista = [] #lista para guardar los id de los usuarios generados en automatico


#ANIMACION DE CREACION DE USUARIO
def animation_create():
    numero = 100
    print("\n Creando Usuario")
    for i in tqdm(range(numero)):
        sleep(0.01)

#ANIMACION DE CERRADO DE PROGRAMA
def animation_exit():
        sys.stdout.write('\rSaliendo.')
        time.sleep(0.2)
        sys.stdout.write('\rSaliendo..')
        time.sleep(0.2)
        sys.stdout.write('\rSaliendo...')
        time.sleep(0.2)
        sys.stdout.write('\rSaliendo....')
        time.sleep(0.2)
        sys.stdout.write('\rPrograma Cerrado!\n')


while True:

    option = input("___Menú de opciones___ \n 1. Reservar una sala \n 2. Cambiar nombre de la reservacion \n 3. Consulta de reservaciones \n" +
                    " 4. Registrar nuevo cliente \n 5. Registrar una sala \n 6. Salir \n")

##################### RESERVAR UNA SALA ######################
    if option == "1":#Alumno: Curiel Muñiz Luis Angel, Matrícula: 1822626
        if not salas:
            print("\n No existe una sala. \n Favor de registrar una sala")
        else:
            while True:
                id_client = input("Ingrese su id: ")
                #VALIDAMOS QUE EL USUARIO NO OMITA EL CAMPO
                if id_client == "":
                    print("El campo no puede quedar vacío")
                    continue
                else:
                    if id_client not in usuarios.keys():
                        print ("No estás registrado como cliente, Favor de registrarse")
                        break
                    else:
                        try:
                            while True:
                                fecha_reserva = input("Ingresa una fecha de reservación, con el formato dd/mm/aaaa")
                                if fecha_reserva == "":
                                    print("El campo no puede quedar vacío")
                                    continue
                                else:
                                    fecha_actual = datetime.date.today()
                                    # GUARDAR EL DICCIONARIO CON EL FOLIO UNICO COMO LLAVE, NOMBRE del evento  llamarlo ,fecha,el turno como lista
                                    fecha_reserva = datetime.datetime.strptime(fecha_reserva, "%d/%m/%Y").date()

                                    if fecha_reserva < fecha_actual + datetime.timedelta(days =+ 2):
                                        print("Debes hacer una reservación con dos o más días de anticipación")
                                    else:
                                        while True:
                                            turno = input("Ingrese el turno que desea(Matutino, Vespertino,Nocturno)")
                                            turno = turno.title()
                                            if turno == "":
                                                print("NO se puede omitir el dato!")
                                                continue
                                            else:
                                                print("SOLAMENTE DEJE ESTE PRINT PARA QUE NO QUEDARA VACIO EL BLOQUE DE CODIGO")

                        except Exception:
                                    print ("Debe ingresar una fecha con el formato dd/mm/aaaa(Ejemplo 04/04/1999)")


###################### EDITAR NOMBRE DE EVENTO ######################
    elif option=="2": #Alumno: Pérez Estrada Lucero Alhelí, Matrícula: 1963004
        while True:
            id_reserva = input("Ingresa tu id de reserva")
            if id_reserva=="":
                print("No se puede dejar vacio")
                continue
            else:
                break
        if id_reserva not in reservaciones.values():
            print("No existen reservas con ese id")
            break
        else:
            nombre_evento = input("Ingrese el nombre deseado")
            reservas={1:["lola","123","22/02/2002"],2:["lolo","456","23/03/2004"]}
            reservas[id_reserva][0] = nombre_evento
            print (reservas.get(1))
        pass


###################### CONSULTAR RESERVACIONES EXISTENTES PARA UNA FECHA ESPECIFICA ######################
    elif option == "3":#Alumno: López Monsivais Oscar Luis, Matrícula: 1996378
        turno_sala = ()
        fecha_pre = input("Fecha deseada a consultar (dd/mm/aaaa): \n")
        fecha_for = datetime.datetime.strptime(fecha_pre, "%d/%m/%Y").date()

        if not reservaciones in fecha_for:
            print("No hay reservaciones que consultar")


###################### REGISTRAR UN CLIENTE ######################
    elif option == "4":#Alumno: Vargas Cepeda Angel Barkiel, Matrícula: 23447
        while True:
            nombre = input("Ingresa tu nombre: ")
            if nombre == "":
                print("Debe ingresar un nombre")
                continue
            else:
                id_usuario +=1
                lista.append(id_usuario)
                max = lista[0];
                for x in lista:
                    if x > max:
                        max = x
                        id_usuario = max
                usuarios[id_usuario] = nombre
                animation_create()
                print(f"Su nombre es: {nombre}, y su clave es: {id_usuario}")
                break
                #print(usuarios[1])


###################### REGISTRAR UNA SALA ######################
    elif option == "5":#Alumno: López Monsivais Oscar Luis, Matrícula: 1996378
        turno_sala = ()
        print("SOLAMENTE ESTA PARA NO DEJAR EL BLOQUE DE CODIGO VACIO")


###################### SALIR ######################
    elif option == "6":#Alumno: Curiel Muñiz Luis Angel, Matrícula: 1822626
        animation_exit()
        break
    else: print('Por favor ingrese una opción disponible del menú')