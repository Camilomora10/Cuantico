import math

"""Libreria de Numeros complejos. , r y angle.
    Donde a y b con las componentes cartesianes ( x : parte real , y: parte imaginaria),
    r es el modulo o magnitud, y angle es angulo theta en coordenadas polares.
    Son INMUTABLES , por lo tanto una vez creados no se pueden modificar ninguno de sus atributos.
 """

def suma_complejos(num1:list,num2:list) -> list:
    """
    Funcion que realiza la suma de dos numeros complejos.
    :param num1: lista que representa primer numero complejo
    :param num2: lista que representa segundo numero complejo
    :return: lista que representa la suma de los numeros complejos.
    """
    res = []
    res.append(num1[0] + num2[0])
    res.append(num1[1] + num2[1])
    return res

def resta_complejos(num1:list,num2:list) -> list:
    """
    Funcion que realiza la resta de dos numeros complejos.
    :param num1: lista que representa primer numero complejo
    :param num2: lista que representa segundo numero complejo
    :return: lista que representa la resta de los numeros complejos.
    """
    res = []
    res.append(num1[0] - num2[0])
    res.append(num1[1] - num2[1])
    return res


def producto_complejos(num1:list,num2:list) -> list:
    """
    Funcion que realiza el producto de dos numeros complejos.
    :param num1: lista que representa primer numero complejo
    :param num2: lista que representa segundo numero complejo
    :return: lista que representa el producto de los numeros complejos.
    """
    res = []
    res.append(num1[0]*num2[0] - num1[1]*num2[1])
    res.append(num1[0]*num2[1] + num1[1]*num2[0])
    return res

def division_complejos(num1:list,num2:list) -> list:
    """
    Funcion que realiza la division de dos numeros complejos.
    :param num1: lista que representa primer numero complejo
    :param num2: lista que representa segundo numero complejo
    :return: lista que representa la division de los numeros complejos.
    """
    res = []
    res.append(round((num1[0]*num2[0]+num1[1]*num2[1])/(num2[0]**2 + num2[1]**2), 2))
    res.append(round((num1[1]*num2[0]-num1[0]*num2[1])/(num2[0]**2 + num2[1]**2), 2))
    return res

def conjugado_complejos(num:list) -> list:
    """
    Funcion que realiza el conjugado de un numero complejo.
    :param num: lista que representa el numero complejo
    :return: lista que representa el conjugado del numero complejo.
    """
    res = []
    res.append(num[0])
    res.append(num[1]*(-1))
    return res

def modulo_complejos(num:list) -> list:
    """
    Funcion que realiza el modulo de un numero complejo.
    :param num: lista que representa el numero complejo
    :return: lista que representa el modulo del numero complejo.
    """
    res = []
    res.append(round((num[0]**2 + num[1]**2)**(0.5), 2))
    return res

def angulo_complejos(num:list) -> list:
    """
    Funcion que realiza la fase o angulo de un numero complejo.
    :param num: lista que representa el numero complejo
    :return: lista que representa el angulo del numero complejo en radianes.
    Recuerde que los angulos los da desde 0 hasta el angulo.
    """
    res = []
    angle = math.atan2(num[1], num[0])
    if (num[0] < 0 and num[1] < 0):
        res.append(round(math.pi*2 +angle,3))
    elif num[0] < 0:
        res.append(round(angle,3))
    elif num[1] < 0:
        res.append(round(math.pi*2 + angle,3))
    else:
        res.append(round(angle,3))
    return res

def cartesianas_polares_complejos(num:list) -> list:
    """
    Funcion que realiza la transformacion de coordenadas
    cartesianas a polares de un numero complejo.
    :param num: lista que representa el numero complejo
    :return: lista que representa la forma polar del numero complejo.
    """
    res = []
    res.append(modulo_complejos(num))
    res.append(angulo_complejos(num))
    return res

def polares_cartesianas_complejos(nump:list) -> list:
    """
    Funcion que realiza la transformacion de coordenadas
    polares a cartesianas de un numero complejo.
    Recuerde que debe ingresar el angulo en radianes.
    :param nump: lista que representa el numero complejo en cordenadas polares
    :return: lista que representa la forma cartesiana del numero complejo.
    """
    res = []
    res.append(round(nump[0]*(math.cos(nump[1]))))
    res.append(round(nump[0]*(math.sin(nump[1]))))
    return res



