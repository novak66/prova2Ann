import numpy as np
# import scipy as sp

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

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

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
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

def poly(x, a, b, c, d, e):
    return a + b*x + c*(x*x) + d*(x*x*x) + e*(x*x*x*x);

def build_func(a, b, c, d, e):
    def temp(x):
        return poly(x, a, b, c, d, e)
    return temp

x = [1.7202, 4.0387, 5.2614, 5.7556, 7.8154, 9.3252, 11.3774, 13.4531, 14.6414, 15.7516, 18.0668, 18.7147]
y = [1.7216, 2.5507, 2.8462, 2.8467, 3.0678, 3.1997, 3.2841, 3.3628, 3.3867, 3.4211, 3.4871, 3.4656]


a0, a1, a2, a3, a4 = best_poly(x, y, 4)

print(f'{a0} , {a1}, {a2}, {a3}, {a4},')

p = build_func(a0, a1, a2, a3, a4)

x_values = [2.1249, 5.5091, 7.1951]
 
for xi_v in x_values:
    print(p(xi_v),',')