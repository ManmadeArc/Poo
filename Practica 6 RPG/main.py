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
            print("Health Points:", Type.Health)
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
    global Player1
    global Player2
    Player1.Show()
    Player1.Show_Health()
    Player1.Show_Special_Stadistic()
    print("Player 1 Actions")
    print("[1]Basic Attack\n[2]Special Attack\n[Anything else]Surrender")
    x = input("Select Your Action: ")
    Player1.Special_Abilitie()
    if x == "1":
        Damage, Type = Player1.Attack()
        if Player2.Dodge():
            input("Player Has Dodged The Ability")
        else:
            input("Player 2 Has Been Damaged")
            Player2.Take_Damage(Damage, Type)
    elif x == "2":
        Damage, Type = Player1.Special_Attack(Player1.Physical_Damage,
                                              Player1.Magic_Damage)
        if Player2.Dodge():
            input("Player Has Dodged The Ability")
        else:
            input("Player 2 Has Been Damaged")
            Player2.Take_Damage(Damage, Type)
    else:
        Player1.Surrender()

    Player1.Add_Especial()
    os.system("cls")
    Player2.Show()
    Player2.Show_Health()
    input("Opponent State Press anything to end turn")
    os.system("cls")


def ActionsP2():
    global Player1
    global Player2
    Player2.Show()
    Player2.Show_Health()
    Player2.Show_Special_Stadistic()
    print("Player 2 Actions")
    print("[1]Basic Attack\n[2]Special Attack\n[Anything else]Surrender")
    x = input("Select Your Action: ")
    os.system("cls")
    Player2.Special_Abilitie()
    if x == "1":
        Damage, Type = Player2.Attack()
        if Player1.Dodge():
            input("Player Has Dodged The Ability")
        else:
            input("Player 1 Has Been Damaged")
            Player1.Take_Damage(Damage, Type)
    elif x == "2":
        Damage, Type = Player2.Special_Attack(Player1.Physical_Damage,
                                              Player1.Magic_Damage)
        if Player1.Dodge():
            input("Player Has Dodged The Ability")
        else:
            input("Player 1 Has Been Damaged")
            Player1.Take_Damage(Damage, Type)
    else:
        Player2.Surrender()

    Player2.Add_Especial()
    os.system("cls")
    Player1.Show()
    Player1.Show_Health()
    input("Opponent State Press anything to end turn")
    os.system("cls")


def Battle_Bucle():
    global Player1
    global Player2
    End = False
    while not End:
        ActionsP1()
        if Player1.Health <= 0 or Player2.Health <= 0:
            break
        ActionsP2()
        if Player1.Health <= 0 or Player2.Health <= 0:
            break

    if Player1.Health <= 0 or Player2.Health <= 0:
        if Player1.Health <= 0:
            print("THE WINNER IS PLAYER 2")
        else:
            print("THE WINNER IS PLAYER 1")


Create_Characters()
Player1 = Select_Character()
Player2 = Select_Character()
Battle_Bucle()