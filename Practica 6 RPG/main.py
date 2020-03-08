from Characters import *
import os
import colorama


colorama.init()


class Game():
    def __init__(self):
        self.Personas = []
        self.Player1 = object
        self.Player2 = object

    def Create_Characters(self):
        P1 = Elf()
        P2 = Undead()
        P3 = Dragon()
        self.Personas.append(P1)
        self.Personas.append(P2)
        self.Personas.append(P3)

    def Select_Character(self, Name):
        Selected = False

        while not Selected:
            for Type in self.Personas:
                print(colorama.Back.YELLOW, colorama.Fore.BLACK)
                print(Name, "Select your Charcter")
                print(colorama.Back.BLACK, colorama.Fore.WHITE)
                Type.Show()
                print("Health Points:", Type.Health)
                print("Magic Power:", Type.Magic_Damage)
                print("Physic Power:", Type.Physical_Damage)
                print("[1]Select\n[Anything Else]Next PJ")
                print(Name)
                x = input("Select Your Action: ")
                os.system("cls")
                if x == "1":
                    Selected = True
                    idx = self.Personas.index(Type)
                    Selection = self.Personas.pop(idx)
                    break
        return Selection

    def PlayersActions(self, Player, Player2):
        print(colorama.Back.YELLOW, colorama.Fore.BLACK)
        print(Player.Name, "Turn")
        print(colorama.Back.BLACK, colorama.Fore.WHITE)
        Player.Show()
        Player.Show_Health()
        Player.Show_Special_Stadistic()
        print(Player.Name, "Actions:")
        print("[1]Basic Attack\n[2]Special Attack\n[Anything else]Surrender")
        x = input("Select Your Action: ")
        Player.Special_Abilitie()
        if x == "1":
            Damage, Type = Player.Attack()
            print("The attack has", Damage, "Points")
            if Player2.Dodge():
                print(Player2.Name, "Has Dodged The Ability")
            else:
                print(Player2.Name, "Has Been Damaged")
                Player2.Take_Damage(Damage, Type)
        elif x == "2":
            Damage, Type = Player.Special_Attack(Player.Physical_Damage,
                                                 Player.Magic_Damage)
            print("The attack has", Damage, "Points")
            if Player2.Dodge():
                print(Player2.Name, "Has Dodged The Ability")
            else:
                print(Player2.Name, "Has Been Damaged")
                Player2.Take_Damage(Damage, Type)
        else:
            Player.Surrender()
            print(Player.Name, "Has Surrended")
        input("Press anything to continue")
        Player.Add_Especial()
        os.system("cls")
        Player2.Show()
        Player2.Show_Health()
        input("Opponent Status\n Press anything to end turn")
        os.system("cls")

    def Battle_Bucle(self):
        while True:
            self.PlayersActions(self.Player1, self.Player2)
            if self.Player1.Health <= 0 or self.Player2.Health <= 0:
                break
            self.PlayersActions(self.Player2, self.Player1)
            if self.Player1.Health <= 0 or self.Player2.Health <= 0:
                break

        if self.Player1.Health <= 0 or self.Player2.Health <= 0:
            if self.Player1.Health <= 0:
                self.Player2.Show()
                print(colorama.Fore.GREEN)
                print("THE WINNER IS PLAYER 2")
                print(colorama.Fore.WHITE)
            else:
                self.Player2.Show()
                print(colorama.Fore.GREEN)
                print("THE WINNER IS PLAYER 1")
                print(colorama.Fore.WHITE)
        input("Press Anything to go back Menu")
        os.system("cls")

    def Menu(self):
        print("Battle Game\nPossible Actions")
        print("[1]Play\n[Anything else]Exit")
        x = input("Select your option: ")
        if x == "1":
            os.system("cls")
            self.play()
        else:
            exit()

    def play(self):
        self.Create_Characters()
        self.Player1 = self.Select_Character("Player 1")
        self.Player1.Set_Name("Player 1")
        self.Player2 = self.Select_Character("Player 2")
        self.Player2.Set_Name("Player 2")
        self.Battle_Bucle()
        self.Personas = []
        self.Menu()


Battle = Game()
Battle.Menu()
