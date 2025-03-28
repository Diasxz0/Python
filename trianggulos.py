def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é possível formar um triângulo"
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return "Não é possível formar um triângulo"
    return "É possível formar um triângulo"