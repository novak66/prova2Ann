"""Em um circuito com tensão aplicada E e com resistência R, indutância L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.3053farads, R=1.113ohm, L=1.7513henrie e que a tensão seja dada por
E(t)=e−0.0534πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas para a corrente i nos pontos"""

import numpy as np



def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return y * (1 - x) + x + 2


def g(t, i):
    c = 0.3053
    r = 1.113
    l = 1.7513

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0534

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0446, 0.1224, 0.2373, 0.3669, 0.4408, 0.5228, 0.6513, 0.7612, 0.8175, 0.9119, 1.0712, 1.1796, 1.2238, 1.3549, 1.4264, 1.5436, 1.618, 1.7512, 1.8644, 1.9316, 2.028, 2.1839, 2.2323, 2.3452, 2.4377, 2.579, 2.6162, 2.7808, 2.8513, 2.9165, 3.0626, 3.172, 3.2191, 3.3617, 3.426, 3.567, 3.6812, 3.7141, 3.8237, 3.9402, 4.0439, 4.1479, 4.2563, 4.3349, 4.479, 4.5631, 4.629, 4.7829, 4.87, 4.9486, 5.0149, 5.1538, 5.2192, 5.3595, 5.4478, 5.5465, 5.6326, 5.7832, 5.8378, 5.9436, 6.0557, 6.1386, 6.2521, 6.3782, 6.42, 6.5425, 6.6298, 6.7652, 6.8258, 6.9443, 7.0454, 7.1166, 7.2313, 7.3405, 7.4672, 7.5552, 7.6496, 7.7536, 7.8526, 7.9694, 8.0412, 8.1394, 8.2283, 8.3736, 8.4294, 8.5699, 8.6627, 8.7626, 8.8483, 8.9373, 9.0756, 9.1343, 9.2574, 9.3109, 9.4812, 9.5699, 9.6202, 9.7818, 9.8227, 9.9556, 10.0122, 10.1344, 10.2174, 10.3543, 10.431, 10.5539, 10.6314, 10.7121, 10.8861, 10.9286, 11.0323, 11.1267, 11.2519, 11.3636, 11.4106, 11.583, 11.6347, 11.7484, 11.8579, 11.9594, 12.0556, 12.1684, 12.263, 12.3283, 12.4302, 12.576, 12.6446, 12.7712, 12.8466, 12.957, 13.0479, 13.1576, 13.2824, 13.3521, 13.4795, 13.5491, 13.6417, 13.7772, 13.8881, 13.9171, 14.0359, 14.1147, 14.2556, 14.3544, 14.4829, 14.5122, 14.6301, 14.7898, 14.8132, 14.9564]
    
    
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

 