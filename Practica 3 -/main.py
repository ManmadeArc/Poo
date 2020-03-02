from Reproductor import*
import os

AppMusica=App()
List=["[1]Agregar/Quitar Canciones\n","[2]Ver Canciones\n","[3]Listas De Reproduccion\n","[4]Play\n","[5]Reproduciendo Actualmente\n","[Cualquier Otra Tecla]Salir"]
def MenuPrincipal():
    global List
    global AppMusica
    print("Bienvenido Al Reproductor de Musica Que Desea Hacer")
    for i in List:
        print (i)
    x=input("Introduzca el numero de la accion a Realizar: ")
    os.system("cls")
    if x=="1":
        AgregarQuitarCanciones()
    elif x=="2":
        print("ID","Artista","Titulo","Duracion")
        AppMusica.mostrarCanciones()
        x=input("Presion 1 si desea reproducir alguna cancion:")
        if x=="1":
            os.system("cls")
            AppMusica.reproducirCancion()
    elif x=="3":
        MenuListasDeReproduccion()
    elif x=="4":
        if len(AppMusica.TodasLasCanciones)>0:
            AppMusica.MusicaAppRep.play()
        else:
            print("Necesitas Agregar Canciones Para Reproducir Algo")
    elif x=="5":
        ReproduciendoActualmente()
    else:
        exit()
    os.system("cls")
    MenuPrincipal()


def AgregarQuitarCanciones():
    global AppMusica
    print("[1]Agregar Canciones\n[2]Remover Canciones\n[Cualquier otra tecla]Volver Al Menu")
    opc=input("Introduzca su opcion: ")
    os.system("cls")
    if opc=="1":
        AppMusica.agregarCancion()
        
    elif opc=="2":
        AppMusica.removerCancion()
        AppMusica.MusicaAppRep.cancionAct=0
        
    else:
        MenuPrincipal()
    os.system("cls")
    AgregarQuitarCanciones()


def MenuListasDeReproduccion():
    global AppMusica
    print("[1]Mostrar Listas\n[2]Editar Listas\n[3]Crear Lista\n[4]Eliminar Lista\n[5]Reproducir Lista\n[Cualquier otra tecla]Volver Al Menu Principal")
    x=input("Seleccione la opcion a Realizar: ")
    os.system("cls")
    if x=="1":
        print("ID","Nombre","Numero De Canciones")
        AppMusica.mostrarListas()

        z=(input("Introduce la ID de la lista para ver sus canciones, si no introduce : -1 "))
        if int(z)==-1:
            MenuListasDeReproduccion()
        elif int(z)>=0 and int(z)<len(AppMusica.ListasDeReproduccion):
            for w in AppMusica.ListasDeReproduccion[int(z)].Canciones:
                print(AppMusica.ListasDeReproduccion[int(z)].Canciones.index(w),w.Title,w.Artista,w.Longitud)
            input("Introduzca Cualquier Cosa Para Volver Al Menu")
        else:
            MenuListasDeReproduccion()
        os.system("cls")
        MenuListasDeReproduccion()
        
    elif x=="2":
        MenuEditarListas()
    elif x=="3":
        AppMusica.agregarLista(input("Introduzca un nombre para la playlist: "))
    elif x=="4":
        AppMusica.removerLista()
        AppMusica.MusicaAppRep.ListaDeReproduccionActual=AppMusica.TodasLasCanciones
        AppMusica.MusicaAppRep.Titulo="Todas Las Canciones"
    elif x=="5":
        AppMusica.reproducirLista()
    else:
        MenuPrincipal()
    os.system("cls")
    MenuListasDeReproduccion()

def MenuEditarListas():
    global AppMusica
    print("[1]Agregar a Lista\n[2]Remover De Lista\n[Cualquier otra tecla]Volver Al Menu Prnicipal")
    x=input("Seleccione la opcion a Realizar: ")
    os.system("cls")
    if x=="1":
        AppMusica.agregarALista()
    elif x=="2":
        AppMusica.removerDeLista()
    else:
        MenuListasDeReproduccion()
    os.system("cls")
    MenuEditarListas()

def ReproduciendoActualmente():
    global AppMusica

    if len(AppMusica.MusicaAppRep.ListaDeReproduccionActual)>0:
        print ("Lista De Reproduccion:",AppMusica.MusicaAppRep.Titulo) if AppMusica.MusicaAppRep.ListaDeReproduccionActual==AppMusica.TodasLasCanciones else print()
        print ("Estado Actual: Reproduciendo") if AppMusica.MusicaAppRep.reproduciendo else print ("Estado Actual: Pausado")
        print("Cancion Actual:",AppMusica.MusicaAppRep.ListaDeReproduccionActual[AppMusica.MusicaAppRep.cancionAct].Title) if AppMusica.MusicaAppRep.ListaDeReproduccionActual==AppMusica.TodasLasCanciones else print("Cancion Actual:",AppMusica.MusicaAppRep.ListaDeReproduccionActual[AppMusica.MusicaAppRep.cancionAct].Title)
        print("Duracion:",AppMusica.MusicaAppRep.ListaDeReproduccionActual[AppMusica.MusicaAppRep.cancionAct].Longitud,"Minutos")
        print("0 ----------------------------",str(AppMusica.MusicaAppRep.ListaDeReproduccionActual[AppMusica.MusicaAppRep.cancionAct].Longitud))
        print("")
        print("        |<    ||    >|         ") if AppMusica.MusicaAppRep.reproduciendo else print("        |<    >    >|         ")
    else:
        print("No Existen Canciones")
    print("[1]Pausar\n[2]Siguiente Cancion\n[3]Cancion Anterior\n[Cualquier otra tecla]Volver al Menu") if AppMusica.MusicaAppRep.reproduciendo else print("[1]Reproducir\n[2]Siguiente Cancion\n[3]Cancion Anterior\n[Cualquier otra tecla]Volver al Menu")
    x=(input("Introduzca la accion a realizar: "))
    os.system("cls")
    if x=="1":
        AppMusica.MusicaAppRep.pause() if AppMusica.MusicaAppRep.reproduciendo else AppMusica.MusicaAppRep.play()
    elif x=="2":
        AppMusica.MusicaAppRep.siguientePista()
    elif x=="3":
        AppMusica.MusicaAppRep.anteriorPista()
    else:
        MenuPrincipal()
    os.system("cls")
    ReproduciendoActualmente()


os.system("cls")
MenuPrincipal()