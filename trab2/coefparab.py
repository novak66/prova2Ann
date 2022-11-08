import numpy as np

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


def poly(x, a, b, c):
    return a + b*x + c*(x*x);

def build_func(a, b, c):
    def temp(x):
        return poly(x, a, b, c)
    return temp



x = [0.3883, 1.1288, 2.288, 2.9166, 3.393, 4.508, 5.2813, 5.9223, 7.2824, 7.5737, 8.7571, 9.9583]
y = [5.1767, 4.3203, 3.8968, 3.7207, 3.6304, 3.6376, 3.8767, 4.2896, 4.3704, 4.3498, 5.3199, 6.4393]
values = [2.2108, 3.204, 6.7012]

a0, a1, a2 = best_poly(x, y, 2)

##coeficiente p(x)
print(f'{a0} , {a1}, {a2}')

p = build_func(a0, a1, a2)


 
 ##valor de p nos pontos
for xi_v in values:
    print(p(xi_v))