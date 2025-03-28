import random
import os

def notas():
    # Obtém o diretório onde o script Python está sendo executado
    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    # Caminho completo do arquivo Boletim.txt dentro do mesmo diretório do script
    caminho_arquivo = os.path.join(diretorio_script, "Boletim.txt")

    disciplinas = input("Quais são suas disciplinas? (separe por vírgulas) ").strip().split(',')
    alunos = input("De quais alunos você quer saber a nota? (separe por vírgulas) ").strip().split(',')

    for aluno in alunos:
        for disciplina in disciplinas:
            nota = random.randint(0, 10)
            with open(caminho_arquivo, 'a') as arquivo:
                arquivo.write(f'{aluno}, a sua nota na {disciplina} foi {nota}\n')

    print(f"Boletim salvo em: {caminho_arquivo}")

notas()
