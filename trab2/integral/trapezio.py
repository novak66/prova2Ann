import math
from numpy import double
from nodesAndWeights import *

# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma


def f(x):
    return math.sqrt(1 + math.cos(x)**2)


def g(x):
    return math.sin(math.e**-x**2) + 1

def h(x):
    return math.sin(x/(math.sqrt(x**2 + 1))) + 1

def p(s, m ,kg, t):
    return math.sqrt(((m**2)*kg)/((s**2)*kg))*math.tanh(math.sqrt(m*kg/((s**2)*m*kg))*t) 

# Variável inferior
a = 0

# Variável superior
b = 6.38

# Lista de subintervalos
n =   [8, 16, 40, 63, 81, 143, 248, 337, 705, 948, 2724, 9467]

for i in range(len(n)):
    r = trapz(p, a, b, n[i])
    print(r, ',')