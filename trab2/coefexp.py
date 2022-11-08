import numpy as np
import math

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * 2 ** (b * x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0195, 0.1044, 0.1313, 0.2158, 0.2475, 0.3328, 0.3455, 0.4345, 0.4561, 0.5509, 0.6055, 0.6359, 0.7168, 0.7545, 0.8129, 0.875, 0.8904, 0.958, 1.0186, 1.1087, 1.1277, 1.2117, 1.2516, 1.3297, 1.3422, 1.4303, 1.4812, 1.5493, 1.61, 1.6518, 1.6872, 1.7558, 1.8221, 1.8495, 1.9109, 1.9689]
    y = [2.4574, 4.7015, 5.8216, 5.4823, 4.561, 4.953, 6.5203, 6.9704, 6.5074, 7.6508, 7.6497, 7.8747, 8.4957, 10.9812, 8.2326, 8.2202, 13.3008, 9.4712, 11.2161, 13.7095, 14.7924, 15.4904, 16.3316, 15.2914, 17.3314, 19.937, 20.8147, 21.7465, 22.8413, 24.1633, 25.2936, 24.6534, 29.3257, 33.3915, 32.8309, 35.4631]   
    
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

    print(f'{a0 } b: {a1}')

    a = np.exp(a0)
    b = a1/np.log(2)

    print('a:', f'{a} e {b}')

    p = build_func(a, b)

    x_values =  [0.4673, 0.6702, 0.9887, 1.1048, 1.7452]

    
    for xi_v in x_values:
        print(p(xi_v), ',')