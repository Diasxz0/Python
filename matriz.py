import numpy as np 


#faz uma matriz usando np
mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2 = np.array([[1, 5, 7], [9, 1, 3], [0, 4, 5]]) 

#faz uma matriz identidade
mat3 = np.eye(3,3)


print(mat1)
print(mat2)
print(mat3)
#multiplica uma matriz por outra
print(mat1 @ mat2)


print('A média dos valores da matriz 1 é', mat1.mean())

#maior valor da matriz
print(mat1.max())

#espaços uniformes
pontos = np.linspace(1, 2, 10)
print(pontos)

#espaços aleatorios e nao inclui o primeiro e o segundo
pontosa = np.random.uniform(1, 2, 10)
print(pontosa)