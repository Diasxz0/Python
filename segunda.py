#importa o modulo os
import os

saida = 'saida'
msg = "mensagem.txt"

#caso a pasta nao exista, ele cria uma
if not os.path.exists(saida):
    os.makedirs(saida)

#abre a pasta com o nome do primeiro, adiciona o 2 
#como elemento dessa pasta e escreve oq ta no .write
with open(os.path.join(saida, msg), 'w') as arq:
    arq.write('oi')