import getpass
import random

EMPATE = 0
VIT_JOGADOR1 = 1
VIT_JOGADOR2 = 2

OPCOES_VALIDAS = {"pedra", "papel", "tesoura"}

def resposta (escolha):
    return escolha

def solicita():
    escolhas = []
    for i in range(1, 3):
        while True:
            escolha = getpass.getpass(f'Jogador{i}, escolha "pedra", "papel" ou "tesoura": ').strip().lower()
            if escolha in OPCOES_VALIDAS:
                escolhas.append(escolha)
                break
            else:
                print("Escolha inválida! Tente novamente.")
    return escolhas

def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return EMPATE
    elif ((jogador1 == 'pedra' and jogador2 == 'papel' or
        jogador1 == 'papel' and jogador2 == 'tesoura'or 
        jogador1 == 'tesoura' and jogador2 == 'pedra')):
        return VIT_JOGADOR2
    else: 
        return VIT_JOGADOR1

escolhas = solicita()
resultado = jokenpo(escolhas [0], escolhas[1])

print('\n------------------')
for i, escolha in enumerate(escolhas):
    print(f"Jogador {i+1}: {escolha}.")
print('\nResultado: ')

if resultado == EMPATE:
    print('Deu empate.')
elif resultado == VIT_JOGADOR1:
    print('Jogador 1 venceu!')
else:
    print('Jogador 2 venceu!')