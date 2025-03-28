import random

chute = 40
resposta = int(input('Adivinhe o numero'))

while resposta != chute:
    if resposta > chute:
        print("Seu chute é MAIOR que o numero")
    else:
        print("Seu chute é MENOR que o numero")
    print("Tente Novamente.")
    resposta = int(input('Adivinhe o numero'))
print('Parabens! Voce acertou o numero!')