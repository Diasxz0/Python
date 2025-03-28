disciplinas = ('historia', 'geografia',
                'matematica', 'portugues', 
                'quimica', 'fisica')
alunos = ['Rebeca','Amanda', 'Brunno', 
          'Cris', 'Davi', 'Felipe']

for i in range(len(alunos)):
    print("Olá,", alunos [i])
    media = float(input('Qual a média da sua escola?'))
    for t in range(len(disciplinas)):
        notas = [float(input(f'qual foi a sua nota em {disciplinas [t]}?'))]
        for j in range(len(notas)):
            if notas [j] >= media:
                print(f"Parabens, {alunos [i]}, você foi aprovado")
            else:
                print(f"Vixe, {alunos [i]}, você foi reprovado")
        
    
