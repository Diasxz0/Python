def soma():
    a = float(input("qual o primeiro numero?"))
    b = float(input("qual o segundo numero?"))
    return a + b

def subtração():
    a = float(input("qual o primeiro numero?"))
    b = float(input("qual o segundo numero?"))
    return a - b 
    
def divisao():
    a = float(input("qual o primeiro numero?"))
    b = float(input("qual o segundo numero?"))
    return  a / d

def mult():
    a = float(input("qual o primeiro numero?"))
    b = float(input("qual o segundo numero?"))
    return b * a

operação = input('Qual operação deseja fazer?')
if operação.strip() == 'soma':
    print(soma())
if operação.strip() == 'divisao':
    print(divisao())
if operação.strip() == 'multiplicacao':
    print(mult())
if operação.strip() == 'subtracao':
    print(subtração())