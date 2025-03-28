disciplinas = ("Historia", "Portugues", "Ciencias", "Geografia")
media = float(input("qual a media da sua escola?\n"))
for i in range(len(disciplinas)):
    notas = float(input(f"qual foi sua nota em {disciplinas[i]}?\n"))
with open("Boletim.txt", 'w') as arquivo:
        arquivo.write(f"voce tirou {notas} em {disciplinas[i]}\n")
for i in range(len(str(notas))):
    if notas[i] >= media:
        with open("boletim.txt", "a") as arquivo:
            arquivo.write(f"Voce passou em {disciplinas[i]}.")
        

