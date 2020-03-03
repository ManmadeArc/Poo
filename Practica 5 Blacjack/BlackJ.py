import random
import colorama
import os

colorama.init()

class Mazo():
    def __init__(self):
        self.Mazo=[]
    def CrearMazo(self):
        Numeros_Cartas=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        Palos_Carta=["♥","♦","♣","♠"]
        for i in Palos_Carta:
            for j in Numeros_Cartas:
                self.Mazo.append(j+i)    

    def mezclar_Mazo(self):
        random.shuffle(self.Mazo)

    def multiplicarMazos(self,Num_Mazos):
        self.Mazo= self.Mazo * Num_Mazos
    
    def eliminar_Primer_Elemento(self,Num_Elementos=1):
        for i in range(Num_Elementos):
            self.Mazo.pop(0)


class Mano():
    def __init__(self,Cartas):
        self.Cartas=Cartas

    def Obtener_valor_num(self,Carta_A_Obtener):
        
        Valor=self.Obtener_Valor(Carta_A_Obtener)
        if Valor=="A":
            Valor=1
        elif Valor=="J" or Valor=="Q" or Valor=="K":
            Valor=10
        return int(Valor)
    
    def Obtener_Valor(self,Carta_A_Obtener):
        return self.Cartas[Carta_A_Obtener][:-1]

    def Obtener_Sumatoria_pts(self):
        Cantidad_AS=0
        Puntaje_Total=0
        for i in range(len(self.Cartas)):
            Valor_A_Sumar=self.Obtener_valor_num(i)
            if Valor_A_Sumar==1:
               Cantidad_AS+=1
            else:
                Puntaje_Total+=Valor_A_Sumar
        if Cantidad_AS>0:
            if ((Puntaje_Total+11)+(Cantidad_AS-1))<=21:
                Puntaje_Total+= 10 + Cantidad_AS
            else:
                Puntaje_Total+= Cantidad_AS
        return Puntaje_Total


class Jugador():
    def __init__(self,Mano,Dealer=False,Apuesta=50,Dinero=15000):
        self.Manos=[]
       
        self.plantarse=[False]
        self.Rendirse=[False]
        self.Seguro=[False]
        self.Apuesta=[]
        self.Seguro_Ap=[]

        self.Manos.append(Mano)
        self.Dealer=Dealer
        self.Dinero=Dinero
        self.Nombre="Jugador 1"
        if self.Dealer:
            self.Nombre="Dealer"

    def Verificar_Seguro(self,Num_Mano):
        return self.Seguro[Num_Mano]

    def Activar_Seguro(self, Num_Mano=0):
        self.Seguro[Num_Mano]=True

    def Obtener_num_manos(self):
        return(len(self.Manos))

    def Imprimir_Mano(self,Num_Mano=0):
        if self.Dealer:
            if self.plantarse[0]==False:
                print(colorama.Back.WHITE + colorama.Fore.RED + self.Manos[Num_Mano].Cartas[0] + colorama.Back.BLACK +colorama.Fore.WHITE, end=" ") if (self.Manos[Num_Mano].Cartas[0][len(self.Manos[Num_Mano].Cartas[0])-1] =="♥" or self.Manos[Num_Mano].Cartas[0][len(self.Manos[Num_Mano].Cartas[0])-1] =="♦") else print(colorama.Back.WHITE + colorama.Fore.BLACK + self.Manos[Num_Mano].Cartas[0] + colorama.Back.BLACK +colorama.Fore.WHITE,end=" ")

                for i in range(len(self.Manos[Num_Mano].Cartas)-1):
                    print(colorama.Back.BLUE+"  "+colorama.Back.BLACK, end=" ")
        else:
            for i in self.Manos[Num_Mano].Cartas:
                print(colorama.Back.WHITE + colorama.Fore.RED + i + colorama.Back.BLACK +colorama.Fore.WHITE, end=" ") if (i[len(i)-1] =="♥" or i[len(i)-1] =="♦") else print(colorama.Back.WHITE + colorama.Fore.BLACK + i + colorama.Back.BLACK +colorama.Fore.WHITE,end=" ")
        
        
class Juego():
    def __init__(self):
        self.Baraja=Mazo()
        self.Ronda=0
        self.Dealer=Jugador([1,2],True)
        self.Jugador1=Jugador([1,2])
        self.Finalizado=False
        self.Mano_Act=0

    def Repartir_Manos(self):
        ManoDealer=[self.Baraja.Mazo[0],self.Baraja.Mazo[1]]
        self.Baraja.eliminar_Primer_Elemento(2)
        ManoDealer1=Mano(ManoDealer)
        self.Dealer=Jugador(ManoDealer1,True)
        ManoJ1=[self.Baraja.Mazo[0],self.Baraja.Mazo[1]]
        ManoJ11=Mano(ManoJ1)
        self.Baraja.eliminar_Primer_Elemento(2)
        self.Jugador1=Jugador(ManoJ11)
    
    def Apostar(self):
        print("Su Cantidad De Dinero Es:",self.Jugador1.Dinero)
        Cantidad_apuesta=0
        try:
            Cantidad_apuesta=int(input("Introduzca la cantidad a apostar:"))
        except:
            Cantidad_apuesta=50
        if (self.Jugador1.Dinero< Cantidad_apuesta or Cantidad_apuesta<50):
            Cantidad_apuesta=50
        else: 
            Cantidad_apuesta=Cantidad_apuesta
        self.Jugador1.Apuesta.append(Cantidad_apuesta)
        self.Jugador1.Dinero+=-1*(Cantidad_apuesta)

    def CrearMazo(self):
        self.Baraja=Mazo()
        self.Baraja.CrearMazo()
        self.Baraja.multiplicarMazos(4)
        self.Baraja.mezclar_Mazo()

    def SetUp(self,Dinero=15000):
        self.Ronda=0
        self.Finalizado=False
        self.Mano_Act=0
        
        self.CrearMazo()
        self.Repartir_Manos()
        self.Jugador1.Dinero=Dinero
        self.Apostar()
        
        
        
        
    def SplitearMano(self):
        CartaTemp=[]
        CartaTemp.append(self.Jugador1.Manos[self.Mano_Act].Cartas.pop(0))
        self.Jugador1.Manos[self.Mano_Act].Cartas.append(self.Baraja.Mazo[0])
        self.Baraja.eliminar_Primer_Elemento()
        CartaTemp.append(self.Baraja.Mazo[0])
        self.Baraja.eliminar_Primer_Elemento()
        ManoTmp=Mano(CartaTemp)
        self.Jugador1.Manos.append(ManoTmp)     
        self.Jugador1.plantarse.append(False)
        ApuestaTemp=self.Jugador1.Apuesta[self.Mano_Act]
        self.Jugador1.Apuesta.append(ApuestaTemp)
        self.Jugador1.Seguro.append(False)
        self.Jugador1.Rendirse.append(False)
        self.Jugador1.Dinero+=-1*ApuestaTemp
        

    def Comprar_seguro(self,Num_Mano):
        self.Jugador1.Activar_Seguro(self.Mano_Act)
        self.Jugador1.Seguro_Ap.append(self.Jugador1.Apuesta[self.Mano_Act]/2)
        self.Jugador1.Dinero+=-1*self.Jugador1.Apuesta[self.Mano_Act]/2

    def Rendirse(self,Num_Mano):
        input(self.Jugador1.Rendirse[self.Mano_Act])
        self.Jugador1.plantarse[self.Mano_Act]=True
        self.Jugador1.Rendirse[self.Mano_Act]=True
        

    def Comprobar_Fin(self):
        contador=0
        for i in self.Jugador1.plantarse:
            if i:
                contador+=1
        if contador==len(self.Jugador1.plantarse):
            self.Finalizado=True

    def Imprimir_Manos(self, i):
            print("Ronda",self.Ronda)
            print(self.Dealer.Nombre)
            self.Mano_Act=self.Jugador1.Manos.index(i)
            self.Dealer.Imprimir_Mano()
            print("\n")
            print(self.Jugador1.Nombre,"Mano: ",self.Mano_Act+1 )
            self.Jugador1.Imprimir_Mano(self.Mano_Act)
            print("\n")
            print("Su total de puntos es:", i.Obtener_Sumatoria_pts())
            print("Su total De Dinero es: ", self.Jugador1.Dinero)
            print("La cantidad De Dinero apostada en esta mano es: ", self.Jugador1.Apuesta[self.Mano_Act])
    
    def Imprimir_Mano_JGana(self):
            print(self.Dealer.Nombre)
            self.Dealer.Dealer=False
            self.Dealer.Imprimir_Mano()
            self.Dealer.Dealer=True
            print("\n")
            print("Los puntos de la casa son:",self.Dealer.Manos[0].Obtener_Sumatoria_pts(),"\n")
            print(self.Jugador1.Nombre,"Mano: ",self.Mano_Act+1 )
            self.Jugador1.Imprimir_Mano(self.Mano_Act)
            print("\n")
            print("Su total de puntos es:", self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts())
            print("La cantidad De Dinero apostada en esta mano es: ", self.Jugador1.Apuesta[self.Mano_Act])

    def Imprimir_Mano_CasaGana(self):
            
            print(self.Dealer.Nombre)
            self.Dealer.Imprimir_Mano()
            print("\n")
            print(self.Jugador1.Nombre,"Mano: ",self.Mano_Act+1 )
            self.Jugador1.Imprimir_Mano(self.Mano_Act)
            print("\n")
            print("Su total de puntos es:", self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts())
            print("La cantidad De Dinero apostada en esta mano es: ", self.Jugador1.Apuesta[self.Mano_Act])

    def Comprobar_Split(self, i):
        if i.Obtener_Valor(0)==i.Obtener_Valor(1) and self.Ronda==0:
            x=input("Desea hacer split\n [1]Si\n[Cualquier otra Tecla]No\nIntroduza su respuesta: ")
            os.system("cls")
            self.Imprimir_Manos(i)
            return x=="1"
            
        else:
            return False
    
    def Comprobar_Seguro(self,i):
        if self.Dealer.Manos[0].Obtener_Valor(0)=="A" and len(self.Dealer.Manos[0].Cartas)==2 and self.Ronda==0:
            z=input("La primera Carta del Dealer es un AS\n[1]Comprar Seguro\n[Cualquie otra cosa]No Comprar Seguro\nIntroduzca la accion a realizar: ")
            os.system("cls")
            self.Imprimir_Manos(i)
            return z=="1"
            
        else:
            return False

    def Comprobar_Rendirse(self,i):
        if self.Ronda==0:
            y=input("Desea Rendirse?\n[1]Si\n[Cualquier Otra Cosa]No\n Introduzca su opcion: ")
            os.system("cls")
            self.Imprimir_Manos(i)
            return y=="1"
        else:
            return False

    def doblar_Apuesta(self,i):
        self.Jugador1.Dinero+=-1*self.Jugador1.Apuesta[self.Mano_Act]
        self.Jugador1.Apuesta[self.Mano_Act]=self.Jugador1.Apuesta[self.Mano_Act]*2
        
    def Pedir_otra_Carta(self,Mano_Act=0,Dealer=False):
        if not Dealer:
            self.Jugador1.Manos[Mano_Act].Cartas.append(self.Baraja.Mazo[0])
        else:
            self.Dealer.Manos[Mano_Act].Cartas.append(self.Baraja.Mazo[0])
        self.Baraja.eliminar_Primer_Elemento()
    
    def Plantarse(self,i):
        self.Jugador1.plantarse[self.Mano_Act]=True
    
    def Mostrar_Victorias(self):
        for i in self.Jugador1.Manos:
            self.Mano_Act=self.Jugador1.Manos.index(i)

            if self.Jugador1.Verificar_Seguro(self.Mano_Act):
                self.Imprimir_Mano_JGana()
                if self.Dealer.Manos[0].Obtener_Sumatoria_pts()==21 and len(self.Dealer.Manos[0].Cartas)==2:
                    
                    print("HAS GANADO EL DINERO DEL SEGURO")
                    self.Jugador1.Dinero+=self.Jugador1.Seguro_Ap[self.Mano_Act]*3
                    print("Su dinero ahora es",self.Jugador1.Dinero)
                    input("Presione Cualquier Tecla Para Continuar: ")
                    
                else:
                    print("Ha perdido el dinero del Seguro")
                    input("Presione Cualquier Tecla Para Continuar: ")
                os.system("cls")
                    
            if self.Jugador1.Rendirse[self.Mano_Act]:
                self.Imprimir_Mano_JGana()
                print("Quitandole la Mitad de la Apuesta debido a que se rindio: ")
                self.Jugador1.Dinero+=self.Jugador1.Apuesta[self.Mano_Act]/2
                print("Su dinero ahora es:", self.Jugador1.Dinero)
                input("Presione Cualquier Tecla Para Continuar: ")
                
            elif (self.Dealer.Manos[0].Obtener_Sumatoria_pts()==21 and len(self.Dealer.Manos[0].Cartas)==2) and (self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts()==21 and len(self.Jugador1.Manos[self.Mano_Act].Cartas)==2) or self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts==self.Dealer.Manos[0].Obtener_Sumatoria_pts():
                self.Imprimir_Mano_JGana()
                print("Tenemos un EMPATE")
                self.Jugador1.Dinero+=self.Jugador1.Apuesta[self.Mano_Act]
                print("Su dinero ahora es: ",self.Jugador1.Dinero)
                input("Presione Cualquier Tecla Para Continuar: ")
            elif self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts()>21 or self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts()<self.Dealer.Manos[0].Obtener_Sumatoria_pts():
                self.Imprimir_Mano_CasaGana()
                print("HAS PERDIDO")
                print("Su dinero ahora es: ",self.Jugador1.Dinero)
                input("Presione Cualquier Tecla Para Continuar: ")
            elif self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts()==21:
                self.Imprimir_Mano_JGana()
                print("HAS GANADO POR BLACJACK, Se te pagara 3 a 2")
                self.Jugador1.Dinero+=self.Jugador1.Apuesta[self.Mano_Act]*2.5
                print("Su dinero ahora es: ",self.Jugador1.Dinero)
                input("Presione Cualquier Tecla Para Continuar: ")
            else:
                self.Imprimir_Mano_JGana()
                print("HAS GANADO , Se te pagara 1 a 1")
                self.Jugador1.Dinero+=self.Jugador1.Apuesta[self.Mano_Act]*2
                print("Su dinero ahora es: ",self.Jugador1.Dinero)
                input("Presione Cualquier Tecla Para Continuar: ")
            os.system("cls")


    def BucleJuego(self):
        x=False    
        while not self.Finalizado:

            for i in self.Jugador1.Manos:
               
                self.Imprimir_Manos(i)
                while self.Dealer.Manos[0].Obtener_Sumatoria_pts()<17:
                    self.Pedir_otra_Carta(0,True)

                

                if not self.Jugador1.plantarse[self.Mano_Act]:
                    if self.Comprobar_Split(i):
                        self.SplitearMano()
                        x=True
                        break
                    if self.Comprobar_Seguro(i):
                        self.Comprar_seguro(self.Mano_Act)
                    if self.Comprobar_Rendirse(i):
                        self.Rendirse(self.Mano_Act)
                    
                    Accion=input("[1]Doblar Apuesta\n[2]Pedir Otra Carta\n[Cualquier otra cosa]Plantarse\n Introduca la accion a realizar:" )
                    if Accion=="1":
                        self.doblar_Apuesta(self.Mano_Act)
                    elif Accion=="2":
                        self.Pedir_otra_Carta(self.Mano_Act)
                    else:
                        self.Plantarse(self.Mano_Act)
                    if self.Jugador1.Manos[self.Mano_Act].Obtener_Sumatoria_pts()>=21:
                        self.Plantarse(self.Mano_Act)
                os.system("cls")

            self.Comprobar_Fin()
            if x:
                x=False
                continue
            self.Ronda+=1
        self.Mostrar_Victorias()

            
                    

            






