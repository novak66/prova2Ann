import numpy as np
import math

def coeffs_dif_fin(x, x0, k):
    n = len(x)

    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row = [xi ** i for xi in x]
        A.append(row)
        # construção da matrz B
        if i < k:
            B.append(0)
        else:
            bi = math.factorial(i) * x0 ** (i-k) / math.factorial(i - k) 
            B.append(bi)
    return np.linalg.solve(A, B)

def dif_fin(coeffs,f, x):
    return sum(ci * f(xi) for ci, xi in zip(coeffs, x))


if __name__ == '__main__':
    #exemplo1
    def f(x):
        return x**2 * math.exp(-x) * math.cos(x) + 1
    
    
    x = [1.5376, 1.5544, 1.5946, 1.6177, 1.6567, 1.7073, 1.7253, 1.7527, 1.808, 1.8377, 1.848, 1.8806, 1.9131, 1.9672, 1.9979]
    x0 = 1.7622
    k = 5 # ordem
    n = 1 # número de pontos
    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.0000001 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)

    y = [f(xi) for xi in x] 


    coeffs = coeffs_dif_fin(x, x0, k)
    aprox = dif_fin(coeffs,f, x)

    print(f'{coeffs}')
    print(f'{aprox}')