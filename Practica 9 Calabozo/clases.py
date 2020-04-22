import random
import os
import csv
import time


class Game:
    def __init__(self):
        self.Numpool=[]
        self.leftCells = []
        self.leftCellsUsed = []
        self.rightCells = []
        self.rightCellsUsed = []
        self.LeftPlayer = False
        self.PosLplayer = -1
        self.PosRplayer = -1
        self.LeftBomb = False
        self.RightBomb = False
        self.rightpoints = 0
        self.leftpoints = 0
        self.SavedGame = False
        self.ronda=0
        self.Ganar=0
    def _Load_Game(self):
        with open("Guardar.csv", "r",) as f:
            x=0
            for linea in csv.reader(f,delimiter=","):
                if x==0:
                    for i in range(11):
                        self.rightCells[i]=int(linea[i])
                    
                if x==1:
                    for i in range(11):
                        self.leftCells[i]=int(linea[i])
                if x==2:
                    for i in range(11):
                        self.rightCellsUsed[i]=(linea[i]=="True")
                    
                if x==3:
                    for i in range(11):
                        self.leftCellsUsed[i]=(linea[i]=="True")
                if x==4:
                    self.LeftPlayer= (linea[0]=="True")
                    self.LeftBomb=(linea[0]=="True")
                    self.RightBomb=(linea[0]=="True")
                    self.ronda=int(linea[3])
                    self.rightpoints=int(linea[4])
                    self.leftpoints=int(linea[5])
                    self.PosLplayer=int(linea[6])
                    self.PosRplayer=int(linea[7])
                    self.Ganar=int(linea[8])
                    
                x+=1
    
    def _save_Game(self):
        with open("Guardar.csv", "w",newline='') as f:
            write=csv.writer(f)
            write.writerow(self.rightCells)
            write.writerow(self.leftCells)
            write.writerow(self.rightCellsUsed)
            write.writerow(self.leftCellsUsed)
            config = [self.LeftPlayer, self.LeftBomb, self.RightBomb,self.ronda,int(self.rightpoints),int(self.leftpoints),self.PosLplayer,self.PosRplayer,self.Ganar]
            write.writerow(config)
                    

    def _Generate_Numbers(self):
        for i in range(11):
            self.Numpool.append(random.randint(2,20))
    
    def _Configuration(self):
        self.rightCells.clear()
        self.leftCells.clear()
        self.leftCellsUsed.clear()
        self.rightCellsUsed.clear()
        for i in range(11):
            self.rightCells.append(0)
            self.leftCells.append(0)
            self.leftCellsUsed.append(False)
            self.rightCellsUsed.append(False)
        self.Numpool=[]
        self.PosLplayer = -1
        self.PosRplayer = -1
        self.rightpoints = 0
        self.leftpoints = 0
        self.RightBomb = False
        self.LeftBomb = False
        
        
    
    def _fill_Cells(self):
        for i in self.Numpool:
            Pos = random.randint(0,10)
            while True:
                if self.leftCellsUsed[Pos]:
                    Pos= random.randint(0,10)
                else:
                    self.leftCells[Pos] = i
                    self.leftCellsUsed[Pos] = True
                    break
            Pos= random.randint(0,10)
            while True:
                if self.rightCellsUsed[Pos]:
                    Pos= random.randint(0,10)
                else:
                    self.rightCells[Pos] = i
                    self.rightCellsUsed[Pos] = True
                    break

    def _generate_bomb(self):
        
        pos = random.randint(1,10)
        self.rightCells[pos]= 99
        self.leftCells[pos] = 99
    
    


    def _select_side(self):
        self.print_table()
        x = input("Introduzca 1 si quiere jugar en el lado izquierdo, cualquier otra cosas el derecho\n")
        self.LeftPlayer = (x=="1")
        os.system("cls")
    
    def print_table(self):
        if self.PosLplayer !=-1 and self.PosLplayer != 11:
            self.leftCellsUsed[self.PosLplayer] = False
        
        if self.PosRplayer != -1 and self.PosRplayer != 11:
            self.rightCellsUsed[self.PosRplayer] = False

        for i in range(0, 6):
            for j in range(0, 24):
                if i == 3 and j == 0:
                    if (self.PosLplayer == -1):
                        print("[I .]", end="")
                    else:
                        print("[ I ]", end="")
                elif  i == 2 and j == 2:
                    if not(self.leftCellsUsed[0]):
                        if self.PosLplayer == 0:
                            print("["+str(self.leftCells[0])+" .]",end="") if (self.leftCells[0]) <=9 else print("["+str(self.leftCells[0])+".]",end="")
                        else:
                            print("["+str(self.leftCells[0])+"  ]",end="") if (self.leftCells[0]) <=9 else print("["+str(self.leftCells[0])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 4 and j == 2:
                    if not(self.leftCellsUsed[1]):
                        if self.PosLplayer == 1:
                            print("["+str(self.leftCells[1])+" .]",end="") if (self.leftCells[1]) <=9 else print("["+str(self.leftCells[1])+".]",end="")
                        else:
                            print("["+str(self.leftCells[1])+"  ]",end="") if (self.leftCells[1]) <=9 else print("["+str(self.leftCells[1])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 1 and j == 4:
                    if not(self.leftCellsUsed[2]):
                        if self.PosLplayer == 2:
                            print("["+str(self.leftCells[2])+" .]",end="") if (self.leftCells[2]) <=9 else print("["+str(self.leftCells[2])+".]",end="")
                        else:
                            print("["+str(self.leftCells[2])+"  ]",end="") if (self.leftCells[2]) <=9 else print("["+str(self.leftCells[2])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 4:
                    if not(self.leftCellsUsed[3]):
                        if self.PosLplayer == 3:
                            print("["+str(self.leftCells[3])+" .]",end="") if (self.leftCells[3]) <=9 else print("["+str(self.leftCells[3])+".]",end="")
                        else:
                            print("["+str(self.leftCells[3])+"  ]",end="") if (self.leftCells[3]) <=9 else print("["+str(self.leftCells[3])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 4:
                    if not(self.leftCellsUsed[4]):
                        if self.PosLplayer == 4:
                            print("["+str(self.leftCells[4])+" .]",end="") if (self.leftCells[4]) <=9 else print("["+str(self.leftCells[4])+".]",end="")
                        else:
                            print("["+str(self.leftCells[4])+"  ]",end="") if (self.leftCells[4]) <=9 else print("["+str(self.leftCells[4])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 1 and j == 6:
                    if not(self.leftCellsUsed[5]):
                        if self.PosLplayer == 5:
                            print("["+str(self.leftCells[5])+" .]",end="") if (self.leftCells[5]) <=9 else print("["+str(self.leftCells[5])+".]",end="")
                        else:
                            print("["+str(self.leftCells[5])+"  ]",end="") if (self.leftCells[5]) <=9 else print("["+str(self.leftCells[5])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 6:
                    if not(self.leftCellsUsed[6]):
                        if self.PosLplayer == 6:
                            print("["+str(self.leftCells[6])+" .]",end="") if (self.leftCells[6]) <=9 else print("["+str(self.leftCells[6])+".]",end="")
                        else:
                            print("["+str(self.leftCells[6])+"  ]",end="") if (self.leftCells[6]) <=9 else print("["+str(self.leftCells[6])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 6:
                    if not(self.leftCellsUsed[7]):
                        if self.PosLplayer == 7:
                            print("["+str(self.leftCells[7])+" .]",end="") if (self.leftCells[7]) <=9 else print("["+str(self.leftCells[7])+".]",end="")
                        else:
                            print("["+str(self.leftCells[7])+"  ]",end="") if (self.leftCells[7]) <=9 else print("["+str(self.leftCells[7])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 1 and j == 8:
                    if not(self.leftCellsUsed[8]):
                        if self.PosLplayer == 8:
                            print("["+str(self.leftCells[8])+" .]",end="") if (self.leftCells[8]) <=9 else print("["+str(self.leftCells[8])+".]",end="")
                        else:
                            print("["+str(self.leftCells[8])+"  ]",end="") if (self.leftCells[8]) <=9 else print("["+str(self.leftCells[8])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 8:
                    if not(self.leftCellsUsed[9]):
                        if self.PosLplayer == 9:
                            print("["+str(self.leftCells[9])+" .]",end="") if (self.leftCells[9]) <=9 else print("["+str(self.leftCells[9])+".]",end="")
                        else:
                            print("["+str(self.leftCells[9])+"  ]",end="") if (self.leftCells[9]) <=9 else print("["+str(self.leftCells[9])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 8:
                    if not(self.leftCellsUsed[10]):
                        if self.PosLplayer == 10:
                            print("["+str(self.leftCells[10])+" .]",end="") if (self.leftCells[10]) <=9 else print("["+str(self.leftCells[10])+".]",end="")
                        else:
                            print("["+str(self.leftCells[10])+"  ]",end="") if (self.leftCells[10]) <=9 else print("["+str(self.leftCells[10])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif i ==3 and j==10:
                    print("  F  ",end="")
                elif i ==3 and j==11:
                    print("  I  ",end="")
                elif i ==3 and j==12:
                    print("  N  ",end="")
                elif  i == 1 and j == 14:
                    if not(self.rightCellsUsed[8]):
                        if self.PosRplayer == 8:
                            print("["+str(self.rightCells[8])+" .]",end="") if (self.rightCells[8]) <=9 else print("["+str(self.rightCells[8])+".]",end="")
                        else:
                            print("["+str(self.rightCells[8])+"  ]",end="") if (self.rightCells[8]) <=9 else print("["+str(self.rightCells[8])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 14:
                    if not(self.rightCellsUsed[9]):
                        if self.PosRplayer == 9:
                            print("["+str(self.rightCells[9])+" .]",end="") if (self.rightCells[9]) <=9 else print("["+str(self.rightCells[9])+".]",end="")
                        else:
                            print("["+str(self.rightCells[9])+"  ]",end="") if (self.rightCells[9]) <=9 else print("["+str(self.rightCells[9])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 14:
                    if not(self.rightCellsUsed[10]):
                        if self.PosRplayer == 10:
                            print("["+str(self.rightCells[10])+" .]",end="") if (self.rightCells[10]) <=9 else print("["+str(self.rightCells[10])+".]",end="")
                        else:
                            print("["+str(self.rightCells[10])+"  ]",end="") if (self.rightCells[10]) <=9 else print("["+str(self.rightCells[10])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 1 and j == 16:
                    if not(self.rightCellsUsed[5]):
                        if self.PosRplayer == 5:
                            print("["+str(self.rightCells[5])+" .]",end="") if (self.rightCells[5]) <=9 else print("["+str(self.rightCells[5])+".]",end="")
                        else:
                            print("["+str(self.rightCells[5])+"  ]",end="") if (self.rightCells[5]) <=9 else print("["+str(self.rightCells[5])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 16:
                    if not(self.rightCellsUsed[6]):
                        if self.PosRplayer == 6:
                            print("["+str(self.rightCells[6])+" .]",end="") if (self.rightCells[6]) <=9 else print("["+str(self.rightCells[6])+".]",end="")
                        else:
                            print("["+str(self.rightCells[6])+"  ]",end="") if (self.rightCells[6]) <=9 else print("["+str(self.rightCells[6])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 16:
                    if not(self.rightCellsUsed[7]):
                        if self.PosRplayer == 7:
                            print("["+str(self.rightCells[7])+" .]",end="") if (self.rightCells[7]) <=9 else print("["+str(self.rightCells[7])+".]",end="")
                        else:
                            print("["+str(self.rightCells[7])+"  ]",end="") if (self.rightCells[7]) <=9 else print("["+str(self.rightCells[7])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 1 and j == 18:
                    if not(self.rightCellsUsed[2]):
                        if self.PosRplayer == 2:
                            print("["+str(self.rightCells[2])+" .]",end="") if (self.rightCells[2]) <=9 else print("["+str(self.rightCells[2])+".]",end="")
                        else:
                            print("["+str(self.rightCells[2])+"  ]",end="") if (self.rightCells[2]) <=9 else print("["+str(self.rightCells[2])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 18:
                    if not(self.rightCellsUsed[3]):
                        if self.PosRplayer == 3:
                            print("["+str(self.rightCells[3])+" .]",end="") if (self.rightCells[3]) <=9 else print("["+str(self.rightCells[3])+".]",end="")
                        else:
                            print("["+str(self.rightCells[3])+"  ]",end="") if (self.rightCells[3]) <=9 else print("["+str(self.rightCells[3])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 5 and j == 18:
                    if not(self.rightCellsUsed[4]):
                        if self.PosRplayer == 4:
                            print("["+str(self.rightCells[4])+" .]",end="") if (self.rightCells[4]) <=9 else print("["+str(self.rightCells[4])+".]",end="")
                        else:
                            print("["+str(self.rightCells[4])+"  ]",end="") if (self.rightCells[4]) <=9 else print("["+str(self.rightCells[4])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 4 and j == 20:
                    if not(self.rightCellsUsed[1]):
                        if self.PosRplayer == 1:
                            print("["+str(self.rightCells[1])+" .]",end="") if (self.rightCells[1]) <=9 else print("["+str(self.rightCells[1])+".]",end="")
                        else:
                            print("["+str(self.rightCells[1])+"  ]",end="") if (self.rightCells[1]) <=9 else print("["+str(self.rightCells[1])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 2 and j == 20:
                    if not(self.rightCellsUsed[0]):
                        if self.PosRplayer == 0:
                            print("["+str(self.rightCells[0])+" .]",end="") if (self.rightCells[0]) <=9 else print("["+str(self.rightCells[0])+".]",end="")
                        else:
                            print("["+str(self.rightCells[0])+"  ]",end="") if (self.rightCells[0]) <=9 else print("["+str(self.rightCells[0])+" ]",end="")
                    else:
                        print("[ ? ]",end="")
                elif  i == 3 and j == 22:
                    if self.PosRplayer == -1:
                        print("[D .]",end="")
                    else:
                        print("[D  ]",end="")
                else:
                    print("     ",end="")
            print()

    def VictoriaPvE(self):

        if self.RightBomb:
            self.rightpoints = self.rightpoints/2
            print("El jugador derecho ha activado la bomba")
        if self.LeftBomb:
            self.leftpoints = self.leftpoints/2
            print("El jugador izquierdo ha activado la bomba")

        print("Jugador Izquierdo",self.leftpoints, "puntos")
        print("Jugador Derecho",self.rightpoints, "puntos")
        if self.rightpoints > self.leftpoints:
            print("El lado derecho gana")
        elif self.rightpoints < self.leftpoints:
            print("El lado izquierdo gana")
        else:
            print("Tenemos un Empate")
        input("Presiona cualquier cosa para continuar")
        self.Ganar=1
        self.ronda=0
        self._save_Game()
        os.system("cls")

    def GameLoop(self):
        
        self.print_table()
        
        if self.LeftPlayer:
            print("El jugador De la Izquierda Comienza comienza")
            while self.ronda<5:
                print("Ronda", self.ronda)
                print("Jugador izquierdo",self.leftpoints, "puntos")
                print("Jugador izquierdo",self.rightpoints, "puntos")
                print("Jugador haga su movimiento")
                self.MoverJugador(self.PosLplayer,self.leftCells,self.leftpoints,self.LeftBomb,"Left")
                print("Maquina haciendo su movimiento")
                time.sleep(2.5)
                self.IA(self.PosRplayer, self.rightCells,self.rightpoints,self.RightBomb,"der")
                self.ronda+=1
                
            
        else:
            print("El jugador De la Derecha Comienza comienza")
            while self.ronda<5:
                print("Ronda", self.ronda)
                print("Jugador Izquierdo",self.leftpoints, "puntos")
                print("Jugador Derecho",self.rightpoints, "puntos")
                print("Jugador haga su movimiento")
                self.MoverJugador(self.PosRplayer, self.rightCells,self.rightpoints,self.RightBomb,"der")
                print("Maquina haciendo su movimiento")
                time.sleep(2.5)
                self.IA(self.PosLplayer,self.leftCells,self.leftpoints,self.LeftBomb,"Left")
                self.ronda+=1
        self.VictoriaPvE()

    def Pausa(self):
        print("Seleccione la accion a relizar\n[1]Guardar y Continuar\n[2]Guardar y salir\n[3]Salir\n[Cualquier otra cosa]Continuar")
        x=input()
        if x=="1":
            self._save_Game()
            
        if x=="2":
            self._save_Game()
            os._exit(1)
        if x=="3":
            os._exit(1)
        os.system("cls")
        self.print_table()
              
    
    def MoverJugador(self,Player,Cells,Points,Bomb,Jug):
        

        if Player == -1:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n[3]Pausa\n")
                if x == "1":
                    Player +=1
                    break
                elif x =="2":
                    Player +=2
                    break
                elif x=="3":
                    self.Pausa()
        elif Player == 0 or Player == 1:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Diagonal Inferior\n[3]Pausa\n")
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
                elif x=="3":
                    self.Pausa()
        elif Player == 2 or Player == 5:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Mover Adelante\n[2]Mover Diagonal Inferior\n[3]Pausa\n")
                if x == "1":
                    Player +=3
                    break
                elif x =="2":
                    Player +=4
                    break
                elif x=="3":
                    self.Pausa()
        elif Player == 4 or Player == 7:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n[3]Pausa\n")
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
                elif x=="3":
                    self.Pausa()
        elif Player == 3 or Player == 6:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Mover Diagonal Superior\n[2]Mover Adelante\n[3]Mover Diagonal Inferior\n[4]Pausa\n")
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
                elif x =="3":
                    Player+=4
                    break
                elif x=="4":
                    self.Pausa()
        elif Player == 9 or Player == 8 or Player ==10:
            while True:
                x=input("Seleccione su Movimiento:\n[1]Avanzar a la meta\n")
                if x == "1":
                    Player = 11
                    break
        if Player>= 0 and Player<=10:
            if Cells[Player] <=20:
                Points += Cells[Player]
            elif Cells[Player] == 99:
                Bomb = True
        if Jug == "Left":
            self.PosLplayer= Player
            self.leftpoints=Points
            self.LeftBomb=Bomb
        else:
            self.PosRplayer= Player
            self.rightpoints=Points
            self.RightBomb=Bomb
        
        os.system("cls")
        self.print_table()
    
    def IA(self,Player,Cells,Points,Bomb,Jug):
        
        if Player == -1:
            while True:
                x=str(random.randint(1,2))
                if x == "1":
                    Player +=1
                    break
                elif x =="2":
                    Player +=2
                    break
        elif Player == 0 or Player == 1:
            while True:
                x=str(random.randint(1,2))
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
        elif Player == 2 or Player == 5:
            while True:
                x=str(random.randint(1,2))
                if x == "1":
                    Player +=3
                    break
                elif x =="2":
                    Player +=4
                    break
        elif Player == 4 or Player == 7:
            while True:
                x=str(random.randint(1,2))
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
        elif Player == 3 or Player == 6:
            while True:
                x=str(random.randint(1,3))
                if x == "1":
                    Player +=2
                    break
                elif x =="2":
                    Player +=3
                    break
                elif x =="3":
                    Player+=4
                    break
        elif Player == 8 or Player == 9 or Player ==10:
            while True:
                x=str(1)
                if x == "1":
                    Player = 11
                    break
        if Player>= 0 and Player<=10:
            if Cells[Player] <=20:
                Points += Cells[Player]
            elif Cells[Player] == 99:
                Bomb = True
        if Jug == "Left":
            self.PosLplayer= Player
            self.leftpoints=Points
            self.LeftBomb=Bomb
        else:
            self.PosRplayer= Player
            self.rightpoints=Points
            self.RightBomb=Bomb
        os.system("cls")
        self.print_table()
                


    



                    
                        
