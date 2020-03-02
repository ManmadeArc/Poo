import random
import os

class Cancion():
    def __init__(self, artista,Titulo):
        self.Artista=artista
        self.Title=Titulo
        self.Longitud=random.randint(1,5)
class ListasDeReproduccion():
    def __init__(self,Title, Canciones):
        self.Title=Title
        self.Canciones=Canciones



class App():
    def __init__(self):
        self.TodasLasCanciones=[]
        self.ListasDeReproduccion=[]
        self.MusicaAppRep=Reproductor(self.TodasLasCanciones)

    def mostrarCanciones(self):
        for x in self.TodasLasCanciones:
            print (self.TodasLasCanciones.index(x), x.Artista, x.Title, x.Longitud)
    def mostrarListas(self):
        for x in self.ListasDeReproduccion:
            print(self.ListasDeReproduccion.index(x), x.Title, len(x.Canciones))
    def agregarLista(self,Nombre):
        Lista=[]
        if len(self.TodasLasCanciones)>0:
            x=int(input("Introduzca el numero de Canciones a Agregar: "))
            print("El numero de canciones Seleccionadas es Invalidos") if x<=0 else ("Agregando",x,"Canciones")
            for i in range(0,x):
                self.mostrarCanciones()
                x=int(input("Introduzca el numero de cancion a agregar:"))
                Lista.append(self.TodasLasCanciones[x])
                os.system("cls")
            w=ListasDeReproduccion(Nombre,Lista)
            self.ListasDeReproduccion.append(w)
        else:
            print("Deben Existir Canciones Para Agregarlas a una Lista De Reproduccion")
    def agregarALista(self):
        self.mostrarListas()
        z=int(input("Introduzca el numero de la lista a agregarle una cancion: "))
        if z>=0 and z<len(self.ListasDeReproduccion):
            if len(self.TodasLasCanciones)>0:
                x=int(input("Introduzca el numero de Canciones a Agregar: "))
                print("El numero de canciones Seleccionadas es Invalidos") if x<=0 else ("Agregando",x,"Canciones")
                for i in range(0,x):
                 self.mostrarCanciones()
                 x=int(input("Introduzca el numero de cancion a agregar:"))
                 self.ListasDeReproduccion[z].Canciones.append(self.TodasLasCanciones[x])
                 os.system("cls")
            else:
                print("Deben Existir Canciones Para Agregarlas a una Lista De Reproduccion")
        else:
            print("Lista No existente")
    def removerDeLista(self):
        self.mostrarListas()
        z=int(input("Introduzca el numero de la lista a removerle una cancion: "))
        if z>=0 and z<len(self.ListasDeReproduccion):
            self.mostrarLista(z)
            x=int(input("Introduzca el numero de cancion a eliminar:"))
            self.ListasDeReproduccion[z].Canciones.pop(x) if x>=0 and x<len(self.ListasDeReproduccion[z].Canciones) else print("La Cancion No existe")
        else:
            print("Lista No Existente")
    def removerLista(self):
        self.mostrarListas()
        z=int(input("Introduzca el numero de la lista a agregarle una cancion: "))
        if z>=0 and z<=len(self.ListasDeReproduccion):
            if self.MusicaAppRep.ListaDeReproduccionActual==self.ListasDeReproduccion[z]:
                self.MusicaAppRep.ListaDeReproduccionActual=self.TodasLasCanciones
                self.MusicaAppRep.Titulo="Todas Las Canciones"
                self.MusicaAppRep.cancionAct=0
            self.ListasDeReproduccion.pop(z)
        else:
            print("El Elemento No Existe")
    def reproducirLista(self):
        self.mostrarListas()
        z=int(input("Introduzca el numero de la lista a reproducir: "))
        if z>=0 and z<=len(self.ListasDeReproduccion) and len(self.ListasDeReproduccion)>0:
            self.MusicaAppRep.ListaDeReproduccionActual=self.ListasDeReproduccion[z].Canciones
            self.MusicaAppRep.Titulo=self.ListasDeReproduccion[z].Title
        else:
            print("El Elemento No Existe")
    def agregarCancion(self):
        song=Cancion(input("Introduca artista: "),(input("Introduzca titulo: ")))
        self.TodasLasCanciones.append(song)
    def removerCancion(self):
        self.mostrarCanciones()
        z=int(input("Introduzca el numero de la cancion a eliminar: "))
        if z>=0 and z<=len(self.TodasLasCanciones):
            for x in self.ListasDeReproduccion:
                for y in x.Canciones:
                    if y.Title== self.TodasLasCanciones[z].Title:
                        x.Canciones.pop(x.Canciones.index(y))
            self.TodasLasCanciones.pop(z)
    def mostrarLista(self,i):
        for x in self.ListasDeReproduccion[i].Canciones:
            print (self.ListasDeReproduccion[i].Canciones.index(x), x.Artista, x.Title, x.Longitud)

    def reproducirCancion(self):
        self.mostrarCanciones()
        x=int(input("Introduzca el numero de la cancion a reproducir: "))
        if x>0 and x<len(self.TodasLasCanciones):
            self.MusicaAppRep.cancionAct=x
            self.MusicaAppRep.ListaDeReproduccionActual=self.TodasLasCanciones
        else:
            print("La Cancion no existe")



class Reproductor():
    def __init__(self,ListaDeRep,actual=0):
        self.cancionAct=actual
        self.ListaDeReproduccionActual=ListaDeRep
        self.reproduciendo=False
        self.Titulo="Todas las Canciones"
        
    def play(self):
        if not self.reproduciendo:
            self.reproduciendo=True
        
    def pause(self):
        if  self.reproduciendo:
            self.reproduciendo=False
    def siguientePista(self):
    
        if self.cancionAct >= len(self.ListaDeReproduccionActual)-1:
            self.cancionAct=0
        else:
           self.cancionAct=self.cancionAct+1
    def anteriorPista(self):
        if self.cancionAct<=0:
            self.cancionAct=len(self.ListaDeReproduccionActual)-1
        else:
            self.cancionAct=self.cancionAct-1
    


