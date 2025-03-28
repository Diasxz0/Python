def area(a, b, c):
    x = c * b / 2
    return x

def perimetro(a, b, c):
    p = a + b + c
    return p 

def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é possível formar um triângulo"
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return "Não é possível formar um triângulo"
    return "É possível formar um triângulo"


import math 


def tri_coordenada(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

