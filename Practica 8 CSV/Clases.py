import random
import csv


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
        x = 0
        for i in self.Apellido_P:
            if i.upper() in VOC and x != 0:
                return str(self.Apellido_P[0] + i)
            x += 1

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
        with open("claves_estados.csv", "r",) as f:
            for linea in csv.reader(f,delimiter=","):

                abreviacin = linea[-1]
                abreviaciones[linea[0]] = abreviacin
        try:
            
            return abreviaciones[self.Estado.upper()]
        except:
            return "NE"

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
            if i.upper() not in VOC and x != 1:
                return i

    def _get_C_intern_Name(self):
        x = 0
        VOC = "AEIOU"
        for i in self.Nombre:
            x += 1
            if i.upper() not in VOC and x != 1:
                return i

    def _get_Year_DIGIT(self):
        if int(self.Año) <= 1999:
            return random.randint(0, 9)
        else:
            return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def _get_Year(self):
        return str(self.Año)[-2] + str(self.Año)[-1]

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
        return Curp.upper()
    
    def Save_User(self):
        with open("Usuarios.csv", "w",newline='') as f:
            write=csv.writer(f)
            Datos=[str(self.Nombre.upper()),
                        self.Apellido_P.upper(),
                        self.Apellido_M.upper(),
                        self._get_sex().upper(),
                        (str(self.Dia) + "\\" + str(self.Mes)
                        + "\\"+str(self.Año)),
                        self.Estado.upper(),
                        self.GetCurp()]
            write.writerow(Datos)
        
