
#def quadrado():
    # a = float(input("Digite o tamanho do primeiro lado.\n"))
    # b = float(input("Digite o tamanho do segundo lado.\n"))
    # c = float(input("Digite o tamanho do terceiro lado.\n"))
    # d = float(input("Digite o tamanho do quarto lado.\n"))
    # if a == b and a==c and a == d:
    #     print("e um quadrado")
    #  else:
    #      print("nao e um quadrado")
import math


def triangulo_retangulo():
    a = float(input("Digite o tamanho da base lado.\n"))
    b = float(input("Digite o tamanho do primeiro cateto.\n"))
    c =float(input("Digite o tamanho do segundo cateto.\n"))
    if a <= 0 or b <= 0 or c <= 0:
        return 'nao da pra fazer um triangulo'
    if (a + b) > c and (b + c)> a and (a + c) > b:
        return "e possivel formar um traingulo com esses valores"
    else:
        print("Nao e possivel formar um traingulo com esses valores")
    perimetro = a + b + c
    print(f"O perimetro desse traingulo e {perimetro}.")
    area = b * c / 2
    return f" a area do triangulo retangulo e {area}"
     
def triangulo_equilatero():
    a = float(input("Digite o tamanho do lado do triangulo equilatero.\n"))
    b = float(input("Digite o tamanho do segundo lado.\n"))
    c =float(input("Digite o tamanho do terceiro lado .\n"))
    if a <= 0 or b <= 0 or c <= 0:
        return 'nao da pra fazer um triangulo'
    if a == b and a == c :
        return"e possivel formar um traingulo equilatero com esses valores"
    else:
        print("Nao e possivel formar um tringulo com esses valores")
    perimetro = a + b + c
    print(f"O perimetro desse traingulo e {perimetro}.")
    h = b * (math.sqrt(3)/2)
    area = a * h / 2
    return f"A area do triangulo retangulo e {area}"

def triangulo_isoceles():
    a = float(input("Qual a base do traingulo isoceles?\n"))
    b = float(input("Qual a medida do primeiro lado?\n"))
    c = float(input("Qual a medida do segundo lado?\n"))
    if a <= 0 or b <= 0 or c <= 0:
        return 'nao da pra fazer um triangulo'
    if b == c :
        perimetro = a + b + c
        print(f"O perimetro desse triangulo e {perimetro}")
        h = b * (math.sqrt(3) / 2)
        area = a * h / 2
        return f"A area do trinagulo é {area}"
    else:
       return "isso nao e um triangulo isosceles."

t = str(input("de qual tipo de triangulo voce deseja saber a area e o perimetro?"))
if t.lower().strip() == "triangulo equilatero":
    print(triangulo_equilatero())
elif t.lower().strip() == "triangulo isosceles":
    print(triangulo_isoceles())
elif t.lower().strip() == "triangulo retangulo":
    print(triangulo_retangulo())
else: 
    print("Por favor, reveja sua escrita e escreva sem acento.")