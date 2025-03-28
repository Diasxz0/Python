import os

datas = "datass"
#printa o caminho absoluto para a variavel datas
print(os.path.abspath(datas))

#printa o caminho pro primeiro e adiciona o segundo fim 
#desse caminho
caminho = os.path.join(os.path.abspath(datas), "c.txt")
print(caminho)

#printa todos os arquivos dentro da pasta selecionada
print(os.listdir("Nível_2"))


for nome in os.listdir("Nível_2"):
    if nome.endswith("y"):
        print('oi')
    else:
        print("erro")