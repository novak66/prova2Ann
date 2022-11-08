import numpy as np
import math


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

def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a*x*np.e**(b*x)
    # return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.1567, 0.3916, 0.7417, 1.0483, 1.2688, 1.4194, 1.6966, 1.7762, 2.1367, 2.2653, 2.5725, 2.8227, 3.1758, 3.3125, 3.5597, 3.8449, 4.0992, 4.2691, 4.5253, 4.6063, 4.9483, 5.2177, 5.373, 5.6819, 5.8976, 6.1877, 6.3636, 6.4851, 6.762, 7.0533, 7.2324, 7.5778, 7.676, 8.0473, 8.2168, 8.5625, 8.6561, 8.8717, 9.2057, 9.3922, 9.7292, 9.9827]
    y = [0.5748, 1.3729, 2.3007, 2.9304, 3.3831, 3.6175, 3.9122, 4.0101, 4.3288, 4.5917, 4.5811, 4.683, 4.8347, 4.7534, 4.7963, 4.8667, 4.7111, 4.6593, 4.5766, 4.5672, 4.4503, 4.3235, 4.2412, 4.2084, 3.9975, 3.958, 3.7629, 3.7014, 3.5936, 3.4254, 3.3081, 3.1434, 3.1298, 2.972, 2.8904, 2.7138, 2.6201, 2.5616, 2.4046, 2.3067, 2.168, 2.0865]
    values = [3.3584, 5.2145, 5.6142, 7.59, 7.7032]

    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(np.divide(y,x))

    xt = [xi + k2 for xi in x]

    x_ = x
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0} e {a1}')

    print('Coeficientes')
    print(f'{a} e {b}')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px}')

"""     # visualização
    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]
    plt.plot(t, qt)
    plt.savefig('best_poly_regressao_potencia.png') """