#abertura = open("msg.txt", "r")
#leitura= abertura.read()
#abertura.close()
#print(leitura)

#mensagem = "msg.txt"
#with open(mensagem, "r") as arq:
   #m = arq.read()
#print("-----")
#print(m)

Resposta = "Voce falhou!"

#with open("msg.txt", "w") as arquivo:
   # arquivo.write(Resposta)
    
#add "fake"
with open("msg.txt") as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo + "\nA nota em mat foi zerada"
with open("msg.text", "w") as arquivo:
      arquivo.write(conteudo)