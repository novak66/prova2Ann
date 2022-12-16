""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=1.78709 e y0=1.43416. Use o método do ponto médio de Euler para estimar o valor da solução exata desse PVI nos pontos
x1=1.82243, x2=1.85759, x3=1.92669, x4=1.95457, x5=1.99357, x6=2.05733, x7=2.10401, x8=2.16365, x9=2.20165, x10=2.26592, x11=2.31861, x12=2.37193, x13=2.39499, x14=2.45683, x15=2.49715, x16=2.56774, x17=2.62874, x18=2.6711, x19=2.72826 e x20=2.77568."""

import numpy as np

def true_euler(f, x0, y0, h, n):
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h        
        print(f'x_{k + 1}={x0} e y_{k+1}={y0}')

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid(f, x0, y0, x_values, n):
    for i in range(n):
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0 = 1.78709
    y0 = 1.43416
    x_values = [1.82243, 1.85759, 1.92669, 1.95457, 1.99357, 2.05733, 2.10401, 2.16365, 2.20165, 2.26592, 2.31861, 2.37193, 2.39499, 2.45683, 2.49715, 2.56774, 2.62874, 2.6711, 2.72826, 2.77568]
    n = 20
    
    
    r2 = euler_mid(f, x0, y0, x_values, n) #euler ponto medio
    for _, i in r2:
        print(f"{i},")