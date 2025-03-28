nomes = input("Quais os nomes dos alunos? (separe por virgulas)\n").strip().split(',')


for nome in nomes:
    notas = float(input((f"Qual foi a nota do(a) {nome}\n")))
    if notas < 6:
        print(f'{nome} está de recuperação!!')
    else: 
        print(f"{nome} foi aprovado!")
    notas = str(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print(f'A maior nota foi {maior_nota}')
print(f'A menor nota foi {menor_nota}')
    