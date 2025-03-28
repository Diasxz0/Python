import math


nome = input("Olá, qual do seu nome?")
print(f"Muito bem, {nome}, vou te ajudar a fazer um controle de gastos!")
mes = input(f"voce, {nome}, deseja controlar os gastos de qual mês?")
salario = float(input("Qual o seu salario?\n"))
alimentacao = float(input(f"Quanto voce gastou com alimentação em {mes}? (Note que roles e fast foods entram em lazer!)\n"))
contas = float(input(f"Quanto voce gastou com contas em {mes} (Conta de agua, de luz, condominio, aluguel, etc)\n"))
namoro = float(input(f"Quanto voce gastou com seu (sua) namorado(a) em {mes}?\n"))
economizar = float(input(f"Quanto voce conseguiu guardar em {mes}?\n"))
lazer = float(input(f"Quanto você gastou com Lazer em {mes}? (saídas, passeios, fast food, etc)\n"))
cont = ("com seu namoro", "com suas contas", "com sua alimentacao", "com seu lazer")

aspectos = ["namoro", 'contas', 'alimentacao', 'lazer']
gastos = [namoro, contas, alimentacao, lazer]
total_gastos = sum(gastos)
saldo = salario - total_gastos


porcentagem_l = (lazer / salario) * 100
porcentagem_n = (namoro / salario) * 100
porcentagem_c = (contas / salario) * 100
porcentagem_a = (alimentacao / salario) * 100
porcentagem_e = (economizar / salario) * 100
porcentagem_s = (saldo / salario) * 100
porcentagem_geral = (porcentagem_n, porcentagem_c, porcentagem_a, porcentagem_l)

with open ("controle.txt", 'a') as arquivo:
    for gasto in range(len(gastos)):
        arquivo.write(f"{nome}, voce gastou {gastos[gasto]} reais {cont[gasto]}, o que corresponde a {round(porcentagem_geral[gasto])}% do seu salario\n")
    if saldo >= 0:
        arquivo.write(f"{nome}, voce rebece {salario} reais de salario e sobrou {saldo} reais, entao voce economizou {round(porcentagem_s)}%. Parabens, seu saldo esta positivo.\n")
    else: 
        arquivo.write(f"{nome}, voce rebece {salario} reais de salario e faltou {saldo} reais. Infelizmente, seu saldo esta negativo em {round(porcentagem_s)}%.\n")
