from datetime import date
from datetime import datetime

class MetodoDePago:
    def __init__(self, Tipo):
        if Tipo:
            self.tipo="Credito"
        else:
            self.tipo="Debito"
        
        self.Cvv=""
        self.tarjetaNum=""
        self.titular=""
        self.mes=0
        self.Anio=0
    def CambiarTitular(self, Nombre=""):
        self.titular=Nombre
    def CambiarCvv(self, nim=""):
        self.Cvv=nim
    



MEtodosDePago=[]
Tipos=["[1]Debito\n[Cualquier otra tecla]Credito"]
menu=["[1]Registrar Metodo de Pago","[2]Mostrar informacion","[3]Cambiar Informacion","[Cualquier otra tecla]Salir"]

def menus():
    global menu
    for x in menu:
        print(x)
    opcion=input("Introduca la accion a realizar ")
    if opcion=="1":
        RegistrarUsuario()
    elif opcion=="2":
        MostrarUsuario()
    elif opcion=="3":
        CambiarInfo()
    else:
        exit()
        
    

def RegistrarUsuario():
    
    global MEtodosDePago
    global Tipos
    for x in Tipos:
        print (x)
    tip=input("Selecciona el metodo de Pago: ")
    Usuario=MetodoDePago(tip)
    Usuario.Titular=input("Introduzca el nombre de titular: ")
    anio=input("Introduza el anio de expiracion: ")
    today=date.today()
    today.year
    if today.year<int(anio):
        Usuario.Anio=today.year
    else:
        Usuario.Anio=anio
    Mes=input("Introduza el mes de expiracion con numeros: ")
    if int(Mes)<today.month or int (Mes)>12:
        Usuario.mes=today.month
    else:
        Usuario.mes=Mes
    Usuario.tarjetaNum=input("Introduzca los 12 numeros: ")
    Usuario.Cvv=input("Introduzca los 3 numeros de atras: ")
    MEtodosDePago.append(Usuario)
    menus()

def MostrarUsuario():
    global MEtodosDePago
    for x in MEtodosDePago:
        print(MEtodosDePago.index(x)+1,x.Titular)
    num=input("introduzca el numero del metodo de pago a seleccionar: ")
    if num>str(len(MEtodosDePago)) or num<str(1):
        num=0
        print ("Nombre: "+ MEtodosDePago[num].Titular)
        print ("Tipo de Tarjeta: "+ MEtodosDePago[num].tipo)
        print ("Numero de Tarjeta: "+ MEtodosDePago[num].tarjetaNum)
        print ("Cvv: "+ MEtodosDePago[num].Cvv)
        print ("Expiracion: "+ str(MEtodosDePago[num].mes) +"/"+str(MEtodosDePago[num].Anio))
        menus()
    else:
        num=int(num)-1
        print ("Nombre: "+ MEtodosDePago[num].Titular)
        print ("Tipo de Tarjeta: "+ MEtodosDePago[num].tipo)
        print ("Numero de Tarjeta: "+ MEtodosDePago[num].tarjetaNum)
        print ("Cvv: "+ MEtodosDePago[num].Cvv)
        print ("Expiracion: "+ str(MEtodosDePago[num].mes) +"/"+str(MEtodosDePago[num].Anio))
        menus()

def CambiarInfo():
    global MEtodosDePago
    for x in MEtodosDePago:
        print(MEtodosDePago.index(x)+1,x.Titular)
    num=input("introduzca el numero del metodo de pago a seleccionar: ")
    if num>str(len(MEtodosDePago)) or num<str(1):
        num=0
        print("[1]Cambiar Titular\n[2]Cambiar Cvv")
        opt=input("Seleccione su accion: ")
        if opt=="1":
            MEtodosDePago[num].CambiarTitular(input("Introduzca el nombre del titular: "))
        else:
            MEtodosDePago[num].CambiarCvv(input("Introduzca el Cvv: "))
        menus()
    else:
        num=int(num)-1
        print("[1]Cambiar Titular\n[Cualquier otra tecla]Cambiar Cvv")
        opt=input("Seleccione su accion: ")
        if opt=="1":
            MEtodosDePago[num].CambiarTitular(input("Introduzca el nombre del titular: "))
        else:
            MEtodosDePago[num].CambiarCvv(input("Introduzca el Cvv: "))
        menus()
        


    



menus()
    
    
    
