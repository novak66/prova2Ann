""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.61144 e y0=0.32504. Use o método de Euler para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.125.

Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.29152 e y0=1.48766. Use o método de Euler para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,15. Use h=0.14865.
"""

import math
import numpy as np

def euler(f, x0, y0, h, n):
    result = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
        print(y0,",")
        # print(f'x_{i+1} = {x0} \t||\t y_{i+1} = {y0}')
    return result

if __name__ == '__main__':

    def f(x, y):
        return y * (1 - x) + x + 2

    x0 = 0.35564
    y0 = 0.76924
    h = 0.16257
    n = 15 #n=15

    #P3.7
    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.47205, 2.16382
    # h = 0.13102
    # n = 10

    resposta = euler(f, x0, y0, h, n)

    def y(x):
        return 5 * math.exp(x - 1) - x - 2