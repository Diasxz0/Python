import random
import os



def notas():
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio, 'Boletim.texto')
    alunos = ((input('De quais alunos voce quer saber a nota? '
'(separe por virgulas)').strip().split(',')))
    disciplinas = ((input("Quais sao suas disciplinas? "
"(separe por virgulas)").strip().split(',')))
    for aluno in alunos:
        for disciplina in disciplinas:
            nota = random.randint(0, 10)
            with open (caminho, 'a') as arquivo:
                arquivo.write(f'{aluno}, a sua nota na {disciplina} foi {nota}\n')
        
print(notas())


