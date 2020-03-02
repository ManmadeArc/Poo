class Smartphone():
    def __init__(self,Us,Uc,GP,Nomb):
        self.AppMusica=Reproductor()
        self.Configuracion=Config(Us,Uc,GP,Nomb)
        self.AppGaleria=Galeria()

class Config():
    def __init__(self, Usuario, UBC, GPS, Nombre):
        self.User=Usuario
        self.ubc=UBC
        self.Gps= GPS
        self.ID=Nombre
    
    def CambiarUsuario(self,name):
        self.User=name
    def CambiarUbicacion(self,Pas):
        self.ubc=Pas
    def CambiarNombre(self,Name):
        self.ID=Name
    def CambairGps(self):
        if self.Gps:
            self.Gps=False
        else:
            self.Gps=True

class Cancion():
    def __init__(self, artista,Titulo,Length):
        self.Artista=artista
        self.Title=Titulo
        self.Longitud

class Lista():
    def __init__(self,Title,Musicas):
        self.Titulo=Titulo
        self.Canciones=Musicas

class Reproductor():
    def __init__(self):
        self.Canciones=[]
        self.ListasDeRepoduccion=[]
        self.reproducciendo = False
    def playorpause(List):
        if not self.reproducciendo:
            print ("Reproduciendo "+List.Titulo)
            self.reproducciendo = True
        else:
            print ("Pausando "+List.Titulo)
            self.reproducciendo = False
    def CrearCancion(self):
        song=Cancion(input("Introduca artista: "),(input("Introduzca titulo: ")))
        self.Canciones.append(song)
    def MostarPlayLists(self):
        for x in self.ListasDeRepoduccion:
            print(x.Titulo)
    def CrearPlaylist(self):
        ss=[]
        for x in self.Canciones:
            print(self.Canciones.index(x), x.Titulo)
        NumeroDeCanciones=int(input("Introduca el numero de canciones a agregar"))
        if NumeroDeCanciones <=len(self.Canciones+1):
            for x in range (1,NumeroDeCanciones):
                i=int(input("Introduca el numero de la cancion "))
                ss.append(self.Canciones[i]) if i<=len(self.Canciones+1) and i>=0 else print("La Cancion No existe")
            w=Lista(input("Introduzca el titulo de la playlist: "),ss)
            self.ListasDeRepoduccion.append(w)
            ss.clear()
        else:
            print("Cantidad De Fotos No Soportada")

                

class Foto():
    def __init__(self,Tit,MB):
        self.Title=Tit
        self.Peso=MB

class Album:
    def __init__(self,NAME,FOTOS):
        self.Titulo=NAME
        self.Fotos=FOTOS
    
    def mostarFotos(self):
        print (self.Titulo)
        for x in self.Fotos:
            print(x.Title, x.Peso)



class Galeria():
    def __init__(self):
        self.Imagenes=[]
        self.Albumes=[]
    def CrearAlbum(self):
        alb=[]
        for x in self.Imagenes:
            print (self.Imagenes.index(x), x.Title)
        NumeroDeFotos=int(input("Introduca el numero de Fotos a agregar: "))
        if NumeroDeFotos<=len(self.Imagenes) and NumeroDeFotos>0:
            for i in range(0,NumeroDeFotos):
                i=int(input("Introduzca el numero de la foto a agregar: "))
                alb.append(self.Imagenes[i]) if i<=len(self.Imagenes)+1 and i>=0 else print("La Foto No Existe")
            w=Album(input("Introduzca el Nombre del album"), alb)
            self.Albumes.append(w)
            alb.clear()
        else:
            print("Los parametros que ha introducido son incorrectos")
    def MostrarAlbums(self):
        for x in self.Albumes:
            print(x.Titulo)
    def MostrarUnAlbum(self,i):
        self.Albumes[i].MostarFotos()

    def AgregaFoto(self):
        Fotillo=Foto(input("Introduzca el nombre de la Foto: "), input("Introduzca el peso con numeros en MB: "))
        self.Imagenes.append(Fotillo)
    def MostFotoAll(self):
        for x in  self.Imagenes:
            print (x.Title, x.Peso + "MB")
    def ViewOnePic(self):
        for x in self.Imagenes:
            print (self.Imagenes.index(x), self.Imagenes.Titulo)
        i=int(input("Introduzca el numero de la foto a mostrar"))
        print(self.Imagenes[i].Title, self.Imagenes[i].Peso) if i<=len(self.Imagenes+1) and i>=0 else  print("La imagen no existe")


    
        
        

        