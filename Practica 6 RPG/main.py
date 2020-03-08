from Characters import *
import os


Personas = []


def Create_Characters():
    global Personas
    P1 = Elf()
    P2 = Undead()
    P3 = Dragon()
    Personas.append(P1)
    Personas.append(P2)
    Personas.append(P3)


def Select_Character():
    global Personas
    Selected = False
    while not Selected:
        for Type in Personas:
            Type.Show()
            print("Heal Points:", Type.Health)
            print("Magic Power:", Type.Magic_Damage)
            print("Physic Power:", Type.Physical_Damage)
            print("[1]Select\n[Anything Else]Next PJ")
            x = input("Select Your Action: ")
            os.system("cls")
            if x == "1":
                Selected = True
                idx = Personas.index(Type)
                Selection = Personas.pop(idx)
                break
    return Selection


def ActionsP1():
    Player1.Show()
    Player1.Show_Health()
    print("Player 1 Actions")
    print("[1]Basic Attack\n[2]Special Attack\n[Anything else]Surrender")
    x == input("Select Your Action: ")
    Player1.Special_Abilitie():
    if x == "1":
        Damage, Type = Player1.Attack()
        


Create_Characters()
Player1 = Select_Character()
Player2 = Select_Character()
