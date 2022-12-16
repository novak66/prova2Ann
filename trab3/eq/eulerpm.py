""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.34762 e y0=1.89755. Use o método do ponto médio de Euler para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.125. """

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

def euler_mid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y):
        return  y * (2 - x) + x + 1
    
    x0 = 0.8102
    y0 = 2.02028
    h = 0.18844
    n = 15
    #r1 = true_euler(f, x0, y0, h, n) #euler
    #print(r1)
    #x1, y1 = zip(*r1)
    #print(y1)

    r2 = euler_mid(f, x0, y0, h, n) #euler ponto medio
    for _, i in r2:
        print(f"{i},")


    #plot 
    """
    import matplotlib.pyplot as plt
    t = np.linspace(x0, x0 + n * h, 200)
    yt = [y(ti) for ti in t]
    plt.plot(t, yt, color='blue')
    plt.scatter(x1, y1, color='orange')
    plt.scatter(x2, y2, color='magenta')
    plt.savefig('euler.png')
    """