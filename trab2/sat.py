import numpy as np
import math

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
    #return a*x*np.e**(b*x)
    return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.7202, 4.0387, 5.2614, 5.7556, 7.8154, 9.3252, 11.3774, 13.4531, 14.6414, 15.7516, 18.0668, 18.7147]
    y = [1.7216, 2.5507, 2.8462, 2.8467, 3.0678, 3.1997, 3.2841, 3.3628, 3.3867, 3.4211, 3.4871, 3.4656]
    values = [2.1249, 5.5091, 7.1951]

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


    print('Coeficientes')


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