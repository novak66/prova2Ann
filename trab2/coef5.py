import numpy as np
# import scipy as sp

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

def poly(x, a, b, c, d, e, f):
    return a + b*x + c*(x*x) + d*(x*x*x) + e*(x*x*x*x) + f*(x*x*x*x*x);

def build_func(a, b, c, d, e, f):
    def temp(x):
        return poly(x, a, b, c, d, e, f)
    return temp


x = [-4.4739, -4.2471, -3.8887, -3.7089, -3.5533, -3.2415, -2.9925, -2.7964, -2.7016, -2.3787, -2.1052, -2.0153, -1.6507, -1.4423, -1.3461, -1.0946, -0.8085, -0.5913, -0.3297, -0.1854, 0.0281, 0.1254, 0.4412, 0.6871, 0.8987, 1.1134, 1.3166, 1.5204, 1.7645, 1.87, 2.2223, 2.4267, 2.6675, 2.8575, 3.1092, 3.3302, 3.5228, 3.7892, 3.9654, 4.2538, 4.3088]
y = [-6.3081, -2.7911, 1.299, 1.9297, 0.9594, 2.5052, 1.3524, 1.9893, 1.8391, 1.2974, -1.0494, -0.8712, -0.5793, 0.9112, -1.0465, -1.2563, -1.0154, -0.7544, -2.3462, -0.2693, -0.1856, 0.7041, 0.6346, 1.012, 0.9463, 0.8228, 0.7763, 0.5561, 0.2188, 0.1386, 0.0652, -1.0702, -0.7805, -2.1977, -2.5772, -2.6693, -2.5257, -1.2382, -0.2302, 2.8587, 5.3099]
a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5)

print(f'{a0 } , {a1 }, {a2 }, {a3 }, {a4 }, {a5 }, ')

p = build_func(a0, a1, a2, a3, a4, a5)

x_values =  [0.5581, 0.9699, 2.0259, 2.2384, 3.069]
 
for xi_v in x_values:
    print(p(xi_v),',')