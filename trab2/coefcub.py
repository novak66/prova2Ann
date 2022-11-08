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

def poly(x, a, b, c, d):
    return a + b*x + c*(x*x) + d*(x*x*x);

def build_func(a, b, c, d):
    def temp(x):
        return poly(x, a, b, c, d)
    return temp


x =   [-4.9786, -4.6406, -4.3643, -3.9132, -3.5392, -3.3266, -3.0037, -2.7067, -2.3887, -2.1679, -1.921, -1.678, -1.4647, -1.0588, -0.813, -0.5069, -0.1271, 0.0201, 0.5811, 0.7094, 1.1154, 1.2202, 1.7566, 2.0452, 2.3271, 2.6028, 2.7284, 3.087, 3.2372, 3.7616, 3.8376, 4.3281, 4.602, 4.77]
y = [1.1607, 2.3603, 2.8992, 3.964, 4.6081, 5.1438, 6.4757, 5.8031, 6.0026, 6.2015, 5.9786, 6.2435, 5.8735, 4.2385, 6.7831, 5.9868, 5.4963, 5.6025, 5.0919, 5.1878, 3.3684, 4.8661, 4.6198, 3.9166, 5.0629, 3.1054, 3.4348, 5.3614, 4.8947, 7.0539, 6.7291, 7.8725, 8.455, 9.0808]

a0, a1, a2, a3 = best_poly(x, y, 3)

print(f'{a0} , {a1 }, {a2 }, {a3 },')


p = build_func(a0, a1, a2, a3)

x_values =  [-3.2895, -2.9533, -1.992, 0.7556, 2.8912]
 
for xi_v in x_values:
    print(p(xi_v),',')