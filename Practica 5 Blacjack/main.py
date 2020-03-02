from BlackJ import *
import colorama
import os

colorama.init()

DineroIncial=15000

def Menu():
    global DineroIncial
    if DineroIncial<=0:
        print("No tienes Dinero Para Seguir Jugando")
        print("Le debes al casino", abs(DineroIncial))
        input("Introduce cualquier tecla para Salir")
        exit()
    print("Bienvenido Al Casino Cetys")
    print("[1]Jugar\n[Cualquier otra cosa]Salir")
    x=input("Introduzca la accion a realizar: ")
    if x=="1":
        Game=Juego()
        Game.SetUp(DineroIncial)
        os.system("cls")
        Game.BucleJuego()

        DineroIncial=Game.Jugador1.Dinero
        Menu()
    else:
        exit()

Menu()
