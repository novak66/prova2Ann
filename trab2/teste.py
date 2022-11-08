from math import *
import numpy as np


def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinômio)')
    A_printado = []
    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
            A_printado.append(somas[i+j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    print('Matriz A:\n',A_printado,'\n''Matriz B:\n',B)
    return A_printado, B, np.linalg.solve(A, B)

x = [1.7056, 2.2546, 3.3963, 3.961, 4.8494, 6.3316, 6.836, 7.8201, 8.8765, 9.8749, 11.0006, 11.4265]
y =  [2.2037, 2.8208, 3.5505, 3.7058, 3.9961, 4.1217, 4.0581, 4.1992, 4.214, 4.2182, 4.3239, 4.261]
values =  [3.0781, 3.6133, 10.7361]

#linearização, transformando x em sqrt(x)

for i in range(0, len(x)):
    x[i] = 1/sqrt(x[i])

for i in range(0, len(y)):
    y[i] = sqrt(y[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
w, z = listPol

b = 1/w
a = z*b

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return pow((a+sqrt(x))/(b*sqrt(x)),2)


print()
print('Values:')
for value in values:
    print(f' {(p(value, a, b))}', end=", ")
print("")
print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")