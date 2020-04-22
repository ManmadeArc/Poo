from clases import Game
import os




def Menu():
    Calabozo=Game()
    Calabozo._Configuration()
    Calabozo._Generate_Numbers()
    Calabozo._fill_Cells()
    Calabozo._generate_bomb()
    print("Bienvenido al juego del calabozo")
    print("en el juego avanzaras por casillas, las cuales tendran un valor")
    print("Y se iran sumando, hasta llegar a al meta, jugaras contra la maquina")
    print("Si quieres Ganar, tendras que no activar la casilla bomba con el 99")
    print("ya que te restara la mitad de los puntos obtenidos")
    print("Bienvenido al juego") 
    print("Que desea hacer\n[1]Jugar\n[2]Cargar Partida\n[Cualquier otra cosa]Salir\n")
    x =input()
    os.system("cls")
    if x =="1":
        Calabozo._select_side()
        
        Calabozo.GameLoop()
        os.system("cls")
        Menu()
    elif x=="2":
        try:
            Calabozo._Load_Game()
        except:
            input("No existe partida en curso.\nSe iniciara una partida nueva\n Presiona cualquier cosa para continuar")
            Calabozo._select_side()
            Calabozo._save_Game()
        if Calabozo.Ganar==1:
            Calabozo.Ganar=0
            input("No existe partida en curso, la anterior ganaste.\nSe iniciara una partida nueva\n Presiona cualquier cosa para continuar")
            Calabozo._Configuration()
            Calabozo._Generate_Numbers()
            Calabozo._fill_Cells()
            Calabozo._generate_bomb()
            Calabozo._select_side()
        
        Calabozo.GameLoop()
        os.system("cls")
        Menu()
    else:
        exit()


Menu()




