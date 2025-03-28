import random
import os

def jogar_dados():
    dados = []
    for i in range(1, 11):
        dado = random.randint(1, 6)
        print (f'Dado {i}: {dado}')
        dados.append(dado)
    return dados
   
def variancia(dados):
    media = sum(dados) / len(dados)
    subtracao = [(x - media) ** 2 for x in dados]
    soma = sum(subtracao)
    resultado = soma / len(dados) 
    return f'A variancia e de: {resultado}'

def media(dados):
    dados = list(map(int, dados))
    final =  sum(dados) / len(dados)
    return f'A media e de: {final}'

def escrita(dados):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio, 'Dados.txt')
    with open(caminho,'w') as arquivo:
        arquivo.write(f'O resultado das rolagens foi: {resultado}\n')
        arquivo.write(f'{media(dados)}\n')
        arquivo.write(f'{variancia(dados)}\n')
    


resultado = jogar_dados()
print(resultado)
escrita(resultado)
print('Veja se um arquivo txt foi aberto!')
