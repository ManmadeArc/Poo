import random


class Usuario():
    def __init__(self, Dia, Mes, Año, Nombre, Appellido_P,
                 Appellido_M, Sexo, Estado):
        self.Dia = Dia
        self.Mes = Mes
        self.Año = Año
        self.Nombre = Nombre
        self.Apellido_M = Appellido_M
        self.Apellido_P = Appellido_P
        self.Sexo = Sexo
        self.Estado = Estado

    def _First_Voc_And_Letter_App_P(self):
        VOC = "AEIOU"
        for i in self.Apellido_P:
            if i.upper() in VOC:
                return str(self.Apellido_P[0] + i)

    def _First_Letter_App_M(self):
        return self.Apellido_M[0]

    def _First_Letter_Name(self):
        return self.Nombre[0]

    def _get_sex(self):
        if self.Sexo:
            return "H"
        else:
            return "M"

    def _get_State(self):
        abreviaciones = {}
        with open("Practica 7\claves_estados.txt", "r",) as f:
            for linea in f.readlines():
                modo = linea.strip().split("\t")
                abreviacin = modo[-1]
                abreviaciones[modo[0]] = abreviacin
        return abreviaciones[self.Estado.upper()]

    def _get_C_intern_App_P(self):
        x = 0
        VOC = "AEIOU"
        for i in self.Apellido_P:
            x += 1
            if not(i.upper() in VOC) and x != 1:
                return i

    def _get_C_intern_App_M(self):
        x = 0
        VOC = "AEIOU"
        for i in self.Apellido_M:
            x += 1
            if i not in VOC and x != 1:
                return i

    def _get_C_intern_Name(self):
        x = 0
        VOC = ["A"]
        for i in self.Nombre:
            x += 1
            if i.upper() not in VOC and x != 1:
                return i

    def _get_Year_DIGIT(self):
        if self.Año <= 1999:
            return random.randint(0, 9)
        else:
            return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def _get_Year(self):
        return str(self.Año)[-1] + str(self.Año)[-2]

    def _get_DIA(self):
        return str(self.Dia)

    def _get_Month(self):
        return str(self.Mes)

    def _get_random_D(self):
        return str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"))

    def GetCurp(self):
        Curp = ""
        Curp += self._First_Voc_And_Letter_App_P().upper()
        Curp += self._First_Letter_App_M().upper()
        Curp += self._First_Letter_Name().upper()
        Curp += self._get_Year().upper()
        Curp += self._get_Month().upper()
        Curp += self._get_DIA().upper()
        Curp += self._get_sex().upper()
        Curp += self._get_State().upper()
        Curp += self._get_C_intern_App_P().upper()
        Curp += self._get_C_intern_App_M().upper()
        Curp += self._get_C_intern_Name().upper()
        Curp += str(self._get_Year_DIGIT()).upper()
        Curp += self._get_random_D().upper()
        return Curp
    
    def Save_User(self):
        with open("Practica 7/Usuarios.txt", "a",) as f:
            f.write(str(self.Nombre.upper() + "\t\t"
                        + self.Apellido_P.upper() + "\t\t"
                        + self.Apellido_M.upper() + "\t\t"
                        + self._get_sex().upper() + "\t\t"
                        + str(self.Dia) + "\\" + str(self.Mes)
                        + "\\"+str(self.Año) + "\t\t"
                        + self.Estado.upper() + "\t\t" +
                        self.GetCurp()+"\n"))


X = Usuario(22, 11, 2000, "Marcos", "Moroyoqui", "Olan", True, "Baja California")

print(X.GetCurp())

X.Save_User()