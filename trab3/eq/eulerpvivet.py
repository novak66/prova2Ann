""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.83347 e y0=1.7933. Use o método de Euler para estimar o valor da solução exata desse PVI nos pontos
x1=1.85255, x2=1.90705, x3=1.95647, x4=2.01295, x5=2.04876, x6=2.12828, x7=2.14712, x8=2.22144, x9=2.25285, x10=2.31169, x11=2.36565, x12=2.40544, x13=2.47376, x14=2.4941, x15=2.56359, x16=2.5906, x17=2.65598, x18=2.72291, x19=2.77664 e x20=2.79584. """

import math
import numpy as np

def euler(f, x0, y0, h, n):
    result = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
    return result

def euler_mod(f, x0, y0, x_values, n):
    result = []
    for i in range(n):
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
    return result

if __name__ == '__main__':

    def f(x, y):
        return y * (1 - x) + x + 2

    x0 = 1.83347
    y0 = 1.7933
    x_values = [1.85255, 1.90705, 1.95647, 2.01295, 2.04876, 2.12828, 2.14712, 2.22144, 2.25285, 2.31169, 2.36565, 2.40544, 2.47376, 2.4941, 2.56359, 2.5906, 2.65598, 2.72291, 2.77664, 2.79584]
    n = 20

    #P3.7
    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.47205, 2.16382
    # h = 0.13102
    # n = 10

    # resposta = euler(f, x0, y0, h, n)
    resposta = euler_mod(f, x0, y0, x_values, n)
    
    for _, i in resposta:
        print(f"{i},")

    def y(x):
        return 5 * math.exp(x - 1) - x - 2

    ##Visualizacao
""" t = np.linspace(x0, x0 + n * h, 100)
    yt = [y(i) for i in t]

    cx, cy = zip(*resposta)

    plt.plot(t, yt)
    plt.scatter(cx, cy)
    plt.savefig('euler.png') """