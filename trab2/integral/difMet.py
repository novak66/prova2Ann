import math
from nodesAndWeights import *

'''
Suponha que a força de resistência do ar sobre um objeto em queda livre é proporcional ao quadrado da velocidade. Neste caso, a velocidade pode ser calculada usando-se
v(t)=math.sqrt(({g}*{m})/({cd}))*math.tanh(math.sqrt(({g}*({cd}))/{m})*t), onde cd é um coeficiente de arrasto de segunda ordem. Sabendo que g=9.81m/s2, m=76.55kg e cd=0.22kg/m. Use
a) a regra dos trapézios com 32 subintervalos
b) a regra de Simpson com 16 subintervalos
c) o método de Romberg com h=9.87/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 10
para determinar a distância percorrida pelo objeto após 9.87s.
'''

def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck*funcao(xk)

    return soma

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

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)
    
def change(nome_funcao, a, b):
    def g(u):
        return f(nome_funcao, (b+a)/2 + (b-a)*u/2) * (b-a)/2
    return g


def trapzRomberg(nome_funcao, a, b, h, f):
    n = int((b-a)/h)
    soma = 0

    for k in range(1, n):
        soma += f(nome_funcao, a+k*h)

    return (h/2)*(f(nome_funcao, a) + 2*soma + f(nome_funcao, b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n-1):
        temp_col = [0] * (n-1-j)
        for i in range(n-1-j):
            power = j+1
            temp_col[i] = (4**power*coluna_f1[i+1]-coluna_f1[i])/(4**power-1)
        coluna_f1[:n-1-j] = temp_col
    return coluna_f1[0]

answer = []
a = [0]
b = [6.38]
order = [8]
n = [10]
exact_for_degree_less_than = [10]
g = '9.81'
m = '79.64'
cd = '0.23'
subintervalosTrapezio = 32
subintervalosSimpson = 16

funcs = [str(f'math.sqrt(({g}*{m})/({cd}))*math.tanh(math.sqrt(({g}*({cd}))/{m})*x)')]

def F(x):
    return math.sqrt((float(g)*float(m))/(float(cd)))*math.tanh(math.sqrt((float(g)*(float(cd)))/float(m))*x)

answer.append(trapz(F, a[0], b[0], subintervalosTrapezio))
answer.append(simps(F, a[0], b[0], subintervalosSimpson))

for i in range(len(funcs)):
    k = int(order[i]/2)
    h = float((b[i]-a[i])/n[i])
    hs = [h/2**i for i in range(k)]
    col1 = [trapzRomberg(funcs[i], a[i], b[i], hi, f) for hi in hs]

    answer.append(romberg(col1))

for i in range(len(funcs)):
    order = str(int(exact_for_degree_less_than[i]/2))
    txt_order = ['raiz'+order, 'peso'+order]
    r = quadratura(change(funcs[i], a[i], b[i]), locals()[txt_order[0]], locals()[txt_order[1]])
    answer.append(r)

print(*answer, sep=", ")



