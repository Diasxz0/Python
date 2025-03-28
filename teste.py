disciplinas = ("matematica", 'portugues', 
               'historia', 'geografia',
               'quimica', 'biologia')
notas = [ 7.0, 8.0, 
         10.0, 7.6, 
         5.4, 2.8]

with open("notas.txt", "w") as nota:
    nota.write("Suas notas foram:")
    for i in range(len(disciplinas)):
        nota.write(f"\n {notas [i]} em {disciplinas[i]}")

    


  

             