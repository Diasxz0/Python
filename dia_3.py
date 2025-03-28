disciplinas = ("Historia", "Geografia", "Matematica", "Portugues")
notas = [10.0, 8.4, 7.6, 5.4]
lista = ['']

for i in range(len(notas)):
    lista.append(f"a sua nota na disciplina {disciplinas[i]} foi {notas[i]}\n")
with open("boletim.txt", 'a') as nota:
        nota.writelines(lista)
