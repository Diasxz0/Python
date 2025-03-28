import trianggulos

with open("dados.txt") as arquivo:
    arq = arquivo.readlines()
for linha in arq:
    dado_unico = linha.strip().split()
    dado_unico = [float(item) for item in dado_unico]
    print(trianggulos.triangulo_valido(dado_unico[0], dado_unico[1], dado_unico[2]))
    with open ("dados.txt", 'a') as w:
        w.write('\n')
        w.write(trianggulos.triangulo_valido(dado_unico[0], dado_unico[1], dado_unico[2]))