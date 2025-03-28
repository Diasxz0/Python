nome = str(input("Olá, qual o seu nome?"))
print(f"Por favor, {nome}, lembre que esse programa so aceita respostas simples, como sim ou nao.")
auto_1 = str(input(f"Muito bem, {nome}, vou pedir umas informações, ok?"))

if auto_1.lower().strip() == "sim" or auto_1.lower().strip() == "yes" or auto_1.lower().strip() == "ok" or auto_1.lower().strip() == "ta bom":
    print("OK")
    disciplinas = ["Matematica", "portugues","historia", "geografia","biologia", "quimica"]
    media = float(input("Antes de tudo, me fale a media da sua escola. (responda em numero, não por extenso)"))
    auto_2 = str(input(f"OK, poderia me confirmar se {disciplinas} são suas materias?"))

    if auto_2.lower().strip() == "sim" or auto_2.lower().strip() == "sao" or auto_2.lower().strip() == "exato" or auto_2.lower().strip() == "isso mesmo":
        print("OK")
        notas = []

        for i in range(len(disciplinas)):
           nota = float(input(f"Qual foi a sua nota em {disciplinas[i]}?"))
           notas.append(nota) == [float(input(f"Qual foi a sua nota em {disciplinas[i]}"))]

        if notas[i] >= media:
                
                with open ("Resultado_Notas.txt", "a") as resultado:
                        resultado.write(f"\nParabens, {nome}, voce passou em {disciplinas[i]}!!")

        else:
                
                with open ("Resultado_Notas.txt", "a") as resultado:
                        resultado.write(f"\nInfelizmente, {nome}, você reprovou em {disciplinas[i]}!")

    else:
        disciplinas_faltando = input("Quais matérias estão faltando? (Separe por vírgulas) ")
        novas_disciplinas = disciplinas_faltando.split(",")  # Divide a string em uma lista

        for nova in novas_disciplinas:
            disciplinas.append(nova.strip())  # Adiciona cada matéria removendo espaços extras
        print(f"Agora suas matérias são: {disciplinas}")  # Confirmação
        notas = []

        for i in range(len(disciplinas)):
            nota = float(input(f"Qual foi a sua nota em {disciplinas[i]}?"))
            notas.append(nota)

            if notas[i] >= media:
                with open ("Resultado_Notas.txt", "a") as resultado:
                        resultado.write(f"\nParabens, {nome}, voce passou em {disciplinas[i]}!!")           

            else:
                with open ("Resultado_Notas.txt", "a") as resultado:
                        resultado.write(f"\nInfelizmente, {nome}, voce reprovou em {disciplinas[i]}!")

else:
    print("Ah, que pena!")
