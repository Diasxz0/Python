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
        
       












else:     
    print("Ah, que pena!")
    breakpoint