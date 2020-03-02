import random
import colorama
import copy
import os

colorama.init()

class Grid:
    def __init__(self):
        self.Grid=[]
        self.size=21
    def CrearGrid(self):
        for i in range (self.size):
            self.Grid.append([])
            for j in range (self.size):
                self.Grid[i].append("  ")
    def PrintGrid(self):
        for i in range (self.size):
            for j in range (self.size):
                print(self.Grid[i][j], end= " | ")
            print()
    def Add_Indexe(self):
        for i in range (self.size):
            for j in range (self.size):
                if j>0:
                    if j<10:
                        self.Grid[0][j]=" "+str(j)
                    else:
                        self.Grid[0][j]=""+str(j)
        for i in range (self.size):
            for j in range (self.size):
                if i>0:
                    if i<10:
                        self.Grid[i][0]=" "+str(i)
                    else:
                        self.Grid[i][0]=""+str(i)

class Palabra:
    def __init__(self,Frase):
        self.Direccion=random.randint(0,3)
        self.Sentido=random.randint(0,1)
        self.word=Frase
    def get_Direccion(self):
        return self.Direccion
    def get_sentido(self):
        return self.Sentido
    def get_word(self):
        return self.word

class Ahorcado:
    def __init__(self,Lista):
        self.Palabras=copy.deepcopy(Lista)
        self.PalabrasActuales=[]
        self.PalabrasEncontradas=[False,False,False,False,False,False,False,False,False,False]
        self.Tablero=Grid()
        self.Selccionador=Select("0","0","0","0")
    def Ganar(self):
        x=0
        for i in self.PalabrasEncontradas:
            if i==True:
                x=x+1
        if x==10:
            return True
        else:
            return False

    def MostrarPalabras(self):
        for i in self.Palabras:
            if self.PalabrasEncontradas[self.Palabras.index(i)]==True:
                print(colorama.Fore.GREEN + str(self.Palabras.index(i)+1),i + colorama.Fore.WHITE)
            else:
                print(colorama.Fore.RED + str(self.Palabras.index(i)+1),i + colorama.Fore.WHITE)
    def Elegir(self):
        self.Selccionador.x=int(input("ingrese la coordenada en x donde comienza su palabra: " ))
        self.Selccionador.y=int(input("Ingrese el valor en y donde comienza su palabra: "))
        print()
        self.Selccionador.direccion=input("[1]Horizonta\n[2]Vertical\n[3]Diagonal \\ \n[Cualquier otra Cosa]Diagonal Inversa /\n Selecciona la direccion: ")
        print()
        self.Selccionador.sentido=input("[1]Izq-Der/Arriba-Abajo \n[Cualquier Otra cosa]Der-Izq/Abajo-Arriba \n Selecciona el sentido: ")
        self.MostrarPalabras()
        self.Selccionador.largo=len(self.Palabras[int(input("Introduce el numero de la palabra "))-1])
        palabra=""
        if self.Selccionador.direccion=="1":
            if self.Selccionador.sentido=="1":
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Add_x()
            else:
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Minus_x()
        elif self.Selccionador.direccion=="2":
            if self.Selccionador.sentido=="1":
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Add_y()
            else:
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Minus_y()
        elif self.Selccionador.direccion=="3":
            if self.Selccionador.sentido=="1":
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Add_y()
                    self.Selccionador.Add_x()
            else:
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Minus_y()
                    self.Selccionador.Minus_x()
        else:
            if self.Selccionador.sentido=="1":
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Minus_y()
                    self.Selccionador.Add_x()
            else:
                for i in range(self.Selccionador.largo):
                    palabra=palabra+self.Tablero.Grid[self.Selccionador.y][self.Selccionador.x][1]
                    self.Selccionador.Add_y()
                    self.Selccionador.Minus_x()
        print("Su palabra fue:",colorama.Fore.LIGHTCYAN_EX +palabra+ colorama.Fore.WHITE)
        input("Enter para continuar: ")
        for i in self.Palabras:
            if i==palabra:
                self.PalabrasEncontradas[self.Palabras.index(i)]=True
                
            
    def RellenarTabla(self):
        lista="abcdegfhijklmnopqrstuvwxyz"
        for i in range(len(self.Tablero.Grid)):
            for j in range(21):
                if self.Tablero.Grid[i][j]=="  ":
                    self.Tablero.Grid[i][j]=" "+lista[random.randint(0,len(lista)-1)]
    def SelecionarPalabras(self):
        while len(self.Palabras)>10:
            self.Palabras.pop(random.randint(0,len(self.Palabras)-1))
        for i in self.Palabras:
            x=Palabra(i)
            self.PalabrasActuales.append(x)
    def ColocarPalabras(self):
        for i in self.PalabrasActuales:
            a=i.get_Direccion()
            b=i.get_sentido()
            c=i.get_word()
            num=len(c)
            if a ==0:
                if b==0:
                    fit=False
                    while not fit:
                        x=random.randint(1,20-num)
                        x1=x
                        y=random.randint(1,20)
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y]==" "+c[i] or self.Tablero.Grid[x1][y]=="  ":
                                z=z+1
                            x1=x1+1
                        if z==num:
                            fit=True  
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i]
                        x=x+1    
                else:
                    fit=False
                    while not fit:
                        x=random.randint(num,20)
                        x1=x
                        y=random.randint(1,20)
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y]==" "+c[i] or self.Tablero.Grid[x1][y]=="  ":
                                z=z+1 
                            x1=x1-1
                        if z==num:
                            fit=True  
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i]
                        x=x-1  
            elif a==1:
                if b==0:
                    fit=False
                    while not fit:
                        x=random.randint(1,20)
                        y=random.randint(1,20-num)
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x][y1]==" "+c[i] or self.Tablero.Grid[x][y1]=="  ":
                                z=z+1
                            y1=y1+1
                        if z==num:
                            fit=True  
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i]
                        y=y+1
                else:
                    fit=False
                    while not fit:
                        x=random.randint(1,20)
                        y=random.randint(num,20)
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x][y1]==" "+c[i] or self.Tablero.Grid[x][y1]=="  ":
                                z=z+1   
                            y1=y1-1
                        if z==num:
                            fit=True
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i] 
                        y=y-1
            elif a==2:
                if b==0:
                    fit=False
                    while not fit:
                        x=random.randint(1,20-num)
                        y=random.randint(1,20-num)
                        x1=x
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y1]==" "+c[i] or self.Tablero.Grid[x1][y1]=="  ":
                                z=z+1 
                            y1=y1+1
                            x1=x1+1
                        if z==num:
                            fit=True
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i]
                        y=y+1
                        x=x+1
                else:
                    fit=False
                    while not fit:
                        x=random.randint(num,20)
                        y=random.randint(num,20)
                        x1=x
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y1]==" "+c[i] or self.Tablero.Grid[x1][y1]=="  ":
                                z=z+1   
                            y1=y1-1
                            x1=x1-1
                        if z==num:
                            fit=True
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i] 
                        y=y-1
                        x=x-1
            else:
                if b==0:
                    fit=False
                    while not fit:
                        x=random.randint(1,20-num)
                        y=random.randint(num,20)
                        x1=x
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y1]==" "+c[i] or self.Tablero.Grid[x1][y1]=="  ":
                                z=z+1  
                            y1=y1-1
                            x1=x1+1
                        if z==num:
                            fit=True    
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i]
                        y=y-1
                        x=x+1
                else:
                    fit=False
                    while not fit:
                        x=random.randint(num,20)
                        y=random.randint(1,20-num)
                        x1=x
                        y1=y
                        z=0
                        for i in range(0,num):
                            if self.Tablero.Grid[x1][y1]==" "+c[i] or self.Tablero.Grid[x1][y1]=="  ":
                                z=z+1
                            y1=y1+1
                            x1=x1-1
                        if z==num:
                            fit=True
                    for i in range(0,num):
                        self.Tablero.Grid[x][y]=" "+c[i] 
                        y=y+1
                        x=x-1
            #self.Tablero.PrintGrid()

class Select:
    def __init__(self,x,y,dire,sent):
        self.x=x
        self.y=y
        self.direccion=dire
        self.sentido=sent
        self.largo=0
    def Add_x(self):
        if self.x==20:
            self.x=1
        else:
            self.x=self.x+1
        
    def Minus_x(self):
        if self.x==1:
            self.x=20
        else:
            self.x=self.x-1
    def Add_y(self):
        if self.y==20:
            self.y=1
        else:
            self.y=self.y+1
    def Minus_y(self):
        if self.y==1:
            self.y=20
        else:
            self.y=self.y-1
        





def Menu():
    os.system("cls")
    print("Bienvenido a la sopa de letras")
    print("[1]Jugar\n[Cualquier otra cosa]Salir")
    x=input("Seleccione la opcion a realizar: ")
    if x=="1":
        SetUp()
        Jugar()
    else:
        exit()

awau=["manzana","pera","platano","avion","malandro","genio","discreto","columpio","salmon","lapiz","borrador","silla","gaming","comida","objeto","sal","tomate","azucar","mandado","celular","laptop","madera","plastico","cabello","cetys","jabon","anime","lentes","control","puerta","jicama"]
Ayuda=Ahorcado(awau)
lista=[]
def Jugar():
    global Ayuda, lista
    os.system("cls")
    if Ayuda.Ganar():
        for i in range(21):
            for j in range(21):
                print(colorama.Fore.GREEN+lista[i][j],end= " | ")
            print()
        print(colorama.Fore.WHITE+"Palabras: ")
        Ayuda.MostrarPalabras()
        print(colorama.Fore.YELLOW+"HAS GANADO HAS ENCONTRADO TODAS LAS PALABRAS")
        input("Presiona enter para volver al menu"+colorama.Fore.WHITE)
        Menu()

    Ayuda.Tablero.PrintGrid()
    print("Palabras: ")
    Ayuda.MostrarPalabras()
    print("[1]Regresar al Menu\n[2]Seleccionar Palabra\n[Cualquier otra cosa]Ver Repuestas")
    x=input("Seleccione la opcion a relizar: ")
    if x=="1":
        Menu()
    elif x=="2":
        Ayuda.Elegir()
        Jugar()
    else:
        for i in range(21):
            for j in range(21):
                print(lista[i][j],end= " | ")
            print()
        input("Introduzca cualquier tecla para volver al menu: ")
        Menu()

def SetUp():
    global Ayuda, lista
    del Ayuda
    random.seed()
    Ayuda=Ahorcado(awau)
    Ayuda.SelecionarPalabras()
    Ayuda.Tablero.CrearGrid()
    Ayuda.Tablero.Add_Indexe()
    Ayuda.ColocarPalabras()
    
    Ayuda.Tablero.Grid[0][0]="--"
    lista=copy.deepcopy(Ayuda.Tablero.Grid)
    Ayuda.RellenarTabla()
    


    

        
Menu()