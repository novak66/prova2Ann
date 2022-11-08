import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sin(x/(math.sqrt(x**2 + 1))) + 1

def g(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1)+2)+3)+4)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')

x =  [0.128, 0.137, 0.146, 0.2815, 0.417, 0.6285, 0.84, 0.879, 0.918, 0.9735, 1.029, 1.084, 1.139, 1.1635, 1.188, 1.331, 1.474, 1.567, 1.66, 1.927, 2.194, 2.2035, 2.213, 2.3815, 2.55, 2.5955, 2.641, 2.6415, 2.642, 2.67, 2.698, 2.7275, 2.757, 3.0925, 3.428, 3.5955, 3.763, 4.063, 4.363, 4.473, 4.583, 4.733, 4.883, 4.915, 4.947]
y =  [1.645, 1.677, 1.709, 2.187, 2.594, 2.952, 2.975, 2.951, 2.921, 2.869, 2.809, 2.744, 2.675, 2.644, 2.613, 2.433, 2.273, 2.186, 2.115, 2.005, 2.038, 2.041, 2.045, 2.145, 2.298, 2.347, 2.399, 2.4, 2.401, 2.434, 2.468, 2.505, 2.542, 2.93, 2.892, 2.561, 2.033, 1.102, 1.356, 1.833, 2.379, 2.927, 2.897, 2.8, 2.674]
intervalo = [-1.078, 1.011]
subintervalos =  [4, 22, 36, 66, 86, 112, 136, 164, 188, 248, 348]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(g, intervalo[0], intervalo[1], subintervalos[i]), ',')
'''

simpsPonto(x, y)