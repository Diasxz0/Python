nome = str(input('Qual o seu nome?'))
print(f'Olá, {nome}, vou te ajudar a ver se você foi ou não aprovado!')
disciplinas = [str(input(f'{nome}, quais são suas disciplinas?'))]
media_escolar = float(input('Qual a media da sua instituição de ensino?'))
for i in range(len(disciplinas)):
    notas = [float(input(f'Qual foi sua nota na {disciplinas[i]}'))]
    if notas [i] >= media_escolar:
        print(f'Parabéns, {nome}, você foi aprovado!')
    else:
        print(f'Infelizmente, {nome}, você foi reprovado!')