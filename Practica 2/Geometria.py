import math

def AreaPoligono(lados,radio):
    if lados==1:
        return math.pi*radio*radio
    elif lados>2:
        angulo=math.radians(360/lados)
        lado=radio*2* math.sin(angulo/2)
        apotema =lado/(2*math.tan(angulo/2))
        perimetro= lado*lados
        area=(perimetro*apotema)/2
        return area
    else:
        return 0

def Volumen(areaBase,alturaPrisma, Piramide=False):
    if not Piramide:
        return (areaBase*alturaPrisma)
    else:
        return((areaBase*alturaPrisma)/3)

