import math
from nodesAndWeights import *

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')

x = [0.119, 0.398, 0.497, 0.535, 0.579, 0.6, 0.751, 0.796, 0.885, 1.027, 1.066, 1.074, 1.129, 1.141, 1.284, 1.53, 1.588, 1.683, 2.13, 2.181, 2.334, 2.508, 2.568, 2.719, 2.855, 2.881, 3.112, 3.234, 3.286, 3.381, 3.532, 3.537, 3.586, 3.67, 3.801, 3.893, 3.951, 3.984, 4.134, 4.16, 4.422, 4.439, 4.728, 4.737, 4.746, 4.912, 4.933]
y =   [1.614, 2.544, 2.772, 2.839, 2.901, 2.925, 3.0, 2.993, 2.947, 2.812, 2.766, 2.756, 2.688, 2.673, 2.49, 2.219, 2.169, 2.1, 2.017, 2.033, 2.111, 2.255, 2.317, 2.494, 2.668, 2.701, 2.945, 2.999, 2.997, 2.944, 2.714, 2.703, 2.586, 2.345, 1.898, 1.572, 1.383, 1.286, 1.013, 1.001, 1.595, 1.672, 2.916, 2.935, 2.951, 2.811, 2.733]
intervalo = [0.15,4.617]
subintervalos = [1, 22, 47, 50, 92, 138, 209, 263, 564, 972, 1845, 5145]

'''
n = len(subintervalos)
for i in range(n):
    trapz(f, intervalo[0], intervalo[1], subintervalos[i])
'''

trapzPonto(x, y)