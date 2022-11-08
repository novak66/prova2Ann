import numpy as np

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*(x/(x+b))


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [1.3078, 1.8905, 1.9988, 2.7691, 3.1172, 3.5808, 4.1474, 4.3223, 4.6408, 5.289, 5.6696, 6.1074, 6.7658, 7.2667, 7.678, 8.1435, 8.2616, 8.9996, 9.2567, 9.6391, 10.138, 10.7563, 11.1613, 11.6661, 12.029, 12.558, 12.7993, 13.6506, 14.0236, 14.4245, 14.6314, 15.133, 15.9255, 16.3042, 16.7401, 17.0614, 17.4494, 17.8646, 18.5172, 18.7316, 19.3, 19.887]
    y = [1.4468, 1.9075, 1.9332, 2.296, 2.3979, 2.5812, 2.6896, 2.7638, 2.8307, 2.8995, 3.0157, 3.0907, 3.1818, 3.2385, 3.2866, 3.3002, 3.3481, 3.3444, 3.4108, 3.4548, 3.4821, 3.4805, 3.5409, 3.5908, 3.6036, 3.5639, 3.6256, 3.6784, 3.6844, 3.6881, 3.6912, 3.6735, 3.7461, 3.7731, 3.7674, 3.7751, 3.8181, 3.7123, 3.8084, 3.7965, 3.8352, 3.8607]
    values = [7.1058, 8.5264, 14.1275, 15.9391, 16.4116]
    
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0} e {a1}')

    print('Coeficientes da potencia')
    print(f'{a },{b},')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value),',')

"""     # visualização
    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]
    plt.plot(t, qt)
    plt.savefig('best_poly_regressao_potencia.png') """