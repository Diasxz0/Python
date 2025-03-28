def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Não é possível formar um triângulo"
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return "Não é possível formar um triângulo"
    return "É possível formar um triângulo"

with open ("controle.txt") as arquivo:
    arq = arquivo.readlines()
for linha in arq:
    dados_separados = linha.strip().split()
    dados_separados =[float(valor) for valor in dados_separados]
    print(triangulo_valido (dados_separados[0], dados_separados[1], dados_separados[2]))
        
    