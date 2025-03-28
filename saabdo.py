import math
from possivel_area_perimetro import tri_coordenada
from possivel_area_perimetro import triangulo_valido
from possivel_area_perimetro import area
from possivel_area_perimetro import perimetro

with open('coordenadas.txt') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        coordenada = linha.strip().replace('(',"").replace(')',"").split(',')
        coordenada = list(map(int, coordenada))    
    
        x1, y1 = coordenada [0], coordenada [1]
        x2, y2 = coordenada [2], coordenada [3]
        x3, y3 = coordenada [4], coordenada [5]

        lado1 = tri_coordenada(x1,y1,x2,y2)
        lado2 = tri_coordenada(x1,y1,x3,y3)
        lado3 = tri_coordenada(x2,y2,x3,y3)
    
        resultado = triangulo_valido(lado1, lado2, lado3)
        print(f"Coordenadas: ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) => {resultado}")
        if triangulo_valido(lado1, lado2, lado3):
            with open ('resultado_tri', 'a') as r:
                r.writelines(f'O perimetro e {perimetro(lado1, lado2, lado3)}\n')
                r.writelines(f'A area e {area(lado1, lado2, lado3)}\n')
            print('Pronto! O arquivo resultado_tri.txt deve ter sido aberto, mostrando as areas e os perimetros')
        else: 
            print('O triangulo nao e valido.')

        

