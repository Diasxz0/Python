nota = float(input('qnto q vc tirou?'))
media_alta = 7
media_baixa = 5

if nota >= media_alta:
    print("Parabens!Passou direto!")
elif nota >= media_baixa: 
      print ("vai para a prova final")
      nota_pf = float(input("qual foi sua nota na prova final?"))
      if nota_pf >= media_baixa:
       print("voce passou, quase hein!")
      else:
       print("você ta de recuperação")
else: 
    print(" voce ta de recuperação")
    nota_rf =  float(input("qual foi sua nota da recuperação?"))
    if nota_rf < media_baixa:
      print("voce reprovou")
    else:
      print("voce passou")