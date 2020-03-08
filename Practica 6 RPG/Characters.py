import random
from Ascii_Characters import *


class Character:
    def __init__(self, Health, Physical_Damage, Magic_Damage,
                 Physical_Resistance, Magic_Resistance, Dodge_Rate):
        self.Health = Health
        self.Physical_Damage = Physical_Damage
        self.Magic_Damage = Magic_Damage
        self.Physical_Resistance = Physical_Resistance
        self.Magic_Resistance = Magic_Resistance
        self.Dodge_Rate = Dodge_Rate

    def Attack(self):
        return self.Physical_Damage, 1

    def Dodge(self):
        return random.randint(0, 5) <= self.Dodge_Rate

    def Take_Damage(self, Damage, Type):
        if Type == 1:
            self.Health -= int(Damage - (Damage * (self.Physical_Resistance
                                                   / 10)))

        elif Type == 2:
            self.Health -= int(Damage - (Damage * (self.Magic_Resistance
                                                   / 10)))

        else:
            self.Health -= int(Damage - Damage * (self.Magic_Resistance +
                                                  self.Physical_Resistance/25))

    def Show_Health(self):
        print("Health Points:", self.Health)

    def Surrender(self):
        self.Health = 0


class Assassin:
    def __init__(self, Critical_Rate):
        self.Critical_Rate = Critical_Rate
        self.Energy = 0

    def Add_Especial(self):
        self.Energy += 1

    def Special_Attack(self, Physic, Magic):
        if self.Energy >= 3:
            Damage = Physic * 3
            self.Energy -= 3
        elif self.Energy >= 1:
            Damage = Physic * 1.5
            self.Energy = 0
        else:
            Damage = 0
        return Damage, 1

    def is_Critical(self):
        return random.randint(0, 5) <= self.Critical_Rate


class Wizard:
    def __init__(self, Heal_Rate):
        self.Heal_Rate = Heal_Rate
        self.Mana = 0

    def Add_Especial(self):
        self.Mana += 1

    def Special_Attack(self, Physic, Magic):
        if self.Mana >= 3:
            Damage = Magic * 3
            self.Mana -= 3
        elif self.Mana >= 1:
            Damage = Magic * 1.5
            self.Mana = 0
        else:
            Damage = 0
        return Damage, 2

    def is_Heal(self):
        return random.randint(0, 5) <= self.Heal_Rate


class Berserker:
    def __init__(self, Resistance_Rate):
        self.Resistance_Rate = Resistance_Rate
        self.Fury = 0

    def Add_Especial(self):
        self.Fury += 1

    def Special_Attack(self, Physic, Magic):
        if self.Fury >= 3:
            Damage = int(2.5 * (Magic+Physic))
        elif self.Fury >= 1:
            Damage = int(1.5 * (Magic+Physic))
        else:
            Damage = 0
        return Damage, 3

    def is_Resistance(self):
        return random.randint(0, 5) <= self.Resistance_Rate


class Elf (Character, Wizard):
    def __init__(self):
        Character.__init__(self, 15, 0, 4, 2, 3, 1)
        Wizard.__init__(self, 1)

    def Show(self):
        print_Wizard()

    def Show_Special_Stadistic(self):
        print ("Mana:", self.Mana)
        print("Especial Attack Uses Mana")
        print("0 Mana =  0 Damage")
        print("2 or 1 Mana =  Medium Damage")
        print(" 3 Mana or more = Maximum Damage")

    def Attack(self):
        return self.Magic_Damage, 2

    def Special_Abilitie(self):
        if self.is_Heal():
            self.Health += random.randint(1, 3)
            input("Elf has healed himself")


class Undead(Character, Assassin):
    def __init__(self):
        Character.__init__(self, 10, 5, 0, 2, 1, 2)
        Assassin.__init__(self, 3)

    def Show(self):
        print_skull()
    
    def Show_Special_Stadistic(self):
        print("Energy:", self.Energy)
        print("Especial Attack Uses Energy")
        print("0 Energy =  0 Damage")
        print("2 or 1 Energy =  Medium Damage")
        print(" 3 energy or more = Maimum Damage")

    def Special_Abilitie(self):
        if self.is_Critical():
            self.Physical_Damage += random.randint(1, 2)
            input("Pyhisical Damage UP")


class Dragon(Character, Berserker):
    def __init__(self):
        Character.__init__(self, 25, 2, 3, 1, 1, 0)
        Berserker.__init__(self, 2)

    def Show(self):
        print_Doragon()

    def Show_Special_Stadistic(self):
        print("Fury:", self.Fury)
        print("Especial Attack Uses Fury")
        print("0 Fury =  0 Damage")
        print("2 or 1 Fury =  Medium Damage")
        print(" 3 Fury or more = Maimum Damage")

    def Attack(self):
        Damage = self.Magic_Damage + self.Physical_Damage
        return Damage, 3

    def Special_Abilitie(self):
        if self.is_Resistance():
            self.Magic_Resistance += 1
            self.Physical_Resistance += 1
            input("Dragon Resistances Up")
