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
            self.Health -= (Damage-self.Physical_Resistance)

        elif Type == 2:
            self.Health -= (Damage-self.Magic_Resistance)

        else:
            self.Health -= int(Damage*(self.Magic_Resistance +
                                       self.Physical_Resistance)/25)

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

    def Special_Attack(self, Physic):
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

    def Special_Attack(self, Magic):
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

    def Special_Attack(self, Magic, Physic):
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
        Character.__init__(self, 20, 0, 4, 2, 3, 2)
        Wizard.__init__(self, 1)

    def Show(self):
        print_Wizard()

    def Special_Abilitie(self):
        if self.is_Heal():
            self.Health += random.randint(1, 3)


class Undead(Character, Assassin):
    def __init__(self):
        Character.__init__(self, 15, 4, 0, 2, 1, 3)
        Assassin.__init__(self, 3)

    def Show(self):
        print_skull()
    
    def Special_Abilitie(self):
        if self.is_Critical():
            self.Damage += random.randint(1, 2)


class Dragon(Character, Berserker):
    def __init__(self):
        Character.__init__(self, 30, 2, 3, 1, 1, 0)
        Berserker.__init__(self, 2)

    def Show(self):
        print_Doragon()
    
    def Special_Abilitie(self):
        if self.is_Resistance():
            self.Magic_Resistance += 1
            self.Physical_Resistance += 1

