from Clases import *
import os


def Menu():
    os.system("cls")
    print("Bienvenido a la Creacion De CURPS")
    print("[1]Consultar\n[Cualquier cosa]Salir")
    x = input("Seleccione la opcion a realizar: ")
    if x == "1":
        CrearUsuario()
    else:
        exit()


def CrearUsuario():
    TempUser=Usuario
    os.system("cls")
    Name = input("Introduzca su nombre: ")
    Apellido_P = input("Introduzca su apellido Paterno: ")
    Apellido_M = input("Introduzca su apellido Materno: ")
    opc = input(("[1]Hombre\n[Cualquier otra cosa]Mujer\n" +
                 "Seleccione su sexo: "))
    if opc == "1":
        sexo = True
    else:
        sexo = False
    Dia = input("Introduzca su dia de nacimiento en 2 digitos. Ej: 02 : ")
    Mes = input("Introduzca su mes de nacimiento en 2 digitos. Ej: 05 : ")
    Anio = input("Introduzca su año de nacimiento en 4 digitos. Ej: 1945 : ")
    Estado = input("Introduzca estado de nacimiento. Ej: Baja California ")
    try:
        TempUser = Usuario(Dia, Mes, Anio, Name, Apellido_P,
                           Apellido_M, sexo, Estado)
    except:
        print("Algun parametro fue introducido de manera incorrecta")
        input("Presiona enter para continuar: ")
        Menu()
    print("Tu Curp Es :", TempUser.GetCurp())
    print("Selecicona tu accion")
    opc = input("[1]Guardar\n[Cualquier otra cosa]Volver al menu")
    if opc == "1":
        TempUser.Save_User()
        input("Presiona enter para continuar")
    Menu()


Menu()
