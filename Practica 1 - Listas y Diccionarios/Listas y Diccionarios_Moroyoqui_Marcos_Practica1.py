import os
import time
opciones = ["[1]Comprar","[2]Ver Carrito","[3]Configuracion","[4]Registrarse","[5]Salir"]
productos = {"Madera Pino":150,"Clavos 1/2 ":30,"Pegamento ":45,"Taquetes ":20,"Lija Fina ":15,"Taladro Boch":450,"Torinillos ":45,"Chilillos ":65}
Names=["Madera Pino","Clavos 1/2 ","Pegamento ","Taquetes ","Lija Fina ","Taladro Boch","Torinillos ","Chilillos "]
Usuarios=[]
Userinfo=[]
Carrito={}
UsuarioActual=1;
Total=0

def RegistrarUsuario():
    print ("Bienvenidos a la tienda sin chiste\n")
    global Usuarios
    global Userinfo
    print("Desea registrarse\n1)Si\n2)No")
    Registrarse=int(input())
    if Registrarse==1:
        print("Introduzca el nombre de usuario: ")
        user=input()
        if (user in Usuarios):
            print("El usuario ya existe")
        else:
            print("Introduzca su password: ")
            password=input()
            print("Introduzca su ciudad de nacimiento : ")
            ciudad=input()
            print("Introduzca su estado de nacimiento: ")
            estado=input()
            print("Introduzca su mes de nacimiento con numero: ")
            mes=input()
            print("Introduzca su dia de nacimiento: ")
            dia=input()
            print("Introduzca su anio de nacimiento: ")
            anio=input()
            print("Introduzca los 12 digitos de su tarjeta: ")
            digitos=input()
            if len(digitos)<12:
                digitos=1597
            else:
                digitos= digitos[8]+digitos[9]+digitos[10]+digitos[11]
            print("Introduzca el mes de Expiracion: ")
            MesE=input()
            print("Introduzca los dos ultimos digitos del anio de expiracion: ")
            AnioE=input()
            print ("Seleccione el tipo de tarjeta: 1)Visa 2)Amex 3)Mastercard")
            Tarjeta=input()
            if Tarjeta==1:
                TT="VISA"
            elif Tarjeta==2:
                TT="AMEX"
            else:
                TT="MASTERCARD"
            Usuarios.append(user)
            users={"Password":password,"CD":ciudad,"Estado":estado,"Mes":mes,"Dia":dia,"Anio":anio,"Digitos":digitos,"MesExp":MesE,"AnioExp":AnioE,"Tarjeta":TT}
            Userinfo.append(users)
            menu()
    else:
        time.sleep(2)
        os.system("cls")
        menu()
    menu()

def MostrarInfo():
    print ("Bienvenidos a la tienda sin chiste\n")
    global Usuarios
    global Userinfo
    global UsuarioActual
    if len(Usuarios)>0:
        for x in Usuarios:
            print(Usuarios.index(x)+1,x)
        print("Que usuarios desea Utilizar: ")
        UsuarioActual=int(input())
        if(UsuarioActual>len(Usuarios)):
            menu()
        else:
            print("Inforamcion personal\n --------------------------------------------------------------------")
            print("Usuario: ",Usuarios[UsuarioActual-1])
            print("Ubicacion: ",Userinfo[UsuarioActual-1].get("CD"),Userinfo[UsuarioActual-1].get("Estado"))
            print("Fecha de nacimiento: ",Userinfo[UsuarioActual-1].get("Mes"),Userinfo[UsuarioActual-1].get("Dia"),Userinfo[UsuarioActual-1].get("Anio"))
            print("Metodo de Pago     \n ---------------------------------------------------------------------")
            print(Userinfo[UsuarioActual-1].get("Tarjeta"))
            print("XXXX XXXX XXXX", Userinfo[UsuarioActual-1].get("Digitos"))
            print("Fecha de Expiracion", Userinfo[UsuarioActual-1].get("MesExp"),"\\",Userinfo[UsuarioActual-1].get("AnioExp"))
    else:
        print("No existe ningun usuario registrado")
        time.sleep(2)
        os.system("cls")
        menu()
    


def menu():
    os.system("cls")
    print ("Bienvenidos a la tienda sin chiste\n")
    for i in opciones:
        print(i)
    opc=int(input())
    if opc==1:
        time.sleep(2)
        os.system("cls")
        Comprar()
    elif opc==2:
        time.sleep(2)
        os.system("cls")
        CarritoCompra()
    elif opc==3:
        time.sleep(2)
        os.system("cls")
        MostrarInfo()
        input("Pulse enter para volven al menu")
        time.sleep(2)
        os.system("cls")
        menu()
    elif opc==4:
        time.sleep(2)
        os.system("cls")
        RegistrarUsuario()
    else:
        pass
        

def Comprar():
    print ("Bienvenidos a la tienda sin chiste\n")
    num=0
    global productos
    global Carrito
    print("Producto\t","Precio")
    for x in productos:
        print("["+str(num+1)+"]"+x+"\t ", productos[x])
        num=num+1
    num=0
    print ("Introduzca el numero de objetos a comprar cantidad de productos")
    Objetos=int (input())
    for i in range (0,Objetos):
        print ("Introduzca el numero del objeto a comprar: ")
        Obj=int(input())
        if (Obj>8):
            Obj=1
        print("Introduza la cantidad del objeto a comprar: ")
        cantidad=int( input())
        Carrito[Names[Obj-1]]=cantidad
    opc=input("Introduzca 1 para proceder al carrito, introduzca cualquier otra tecla para salir al menu: ")
    if opc=="1":
        time.sleep(2)
        os.system("cls")
        CarritoCompra();
    else:
        time.sleep(2)
        os.system("cls")
        menu()
    menu()

def CarritoCompra():
    global Usuarios
    print ("Bienvenidos a la tienda sin chiste\n")
    print("Producto\t","Precio Unitario\t","Cantidad\t","Total")
    global Total
    Total=0
    for x in Carrito:
        print(x+"\t",productos[x],"\t\t\t" ,Carrito[x],"\t\t", productos[x]*Carrito[x])
        Total=Total+ productos[x]*Carrito[x]
    print("Total\t\t\t\t\t\t\t",Total)
    opc=input("Introduzca 1 para proceder a pagar, introduzca cualquier otra tecla para salir al menu: ")
    
    if opc=="1":
        if len(Usuarios)>0:
            time.sleep(2)
            os.system("cls")
            MostrarInfo()
            Pagar()
        else:
            print("Necesita Registrar Un Usuario Para Pagar, introduca 1 para registrar usuario cualquier otra letra para salir al menu")
            opc=input()
            if opc=="1":
                time.sleep(2)
                os.system("cls")
                RegistrarUsuario()
            else:
                time.sleep(2)
                os.system("cls")
                menu()       
    else:
        time.sleep(2)
        os.system("cls")
        menu()
    menu()
 

def Pagar():
    
    global UsuarioActual
    global Userinfo
    global Carrito
    print("Introduzca el password para pagar:")
    passwor=input()
    if passwor==Userinfo[UsuarioActual-1].get("Password"):
        print("Su Compra Se ha relizado Correctamente")
        Carrito.clear()
    else:
        print("Su password fue incorrecto")
    time.sleep(2)
    os.system("cls")
    menu()



menu()
