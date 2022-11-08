import math
from numpy import double

'''Use o método de Romberg, com o h indicado, para encontrar uma aproximação 
com erro O(hk) para as integrais a seguir:'''

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)


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

func = ['math.exp(-x**2)', '(x+1/x)**2', 'math.sqrt(1+x**2)', 'math.cos(-x**2/3)', 'math.exp(x)*math.sin(x)/(1+x**2)']
a = [-0.518, 0.868, 0.57, 0.988, 0.407]
b = [0.482, 1.868, 1.57, 1.988, 1.407]
order = [10, 10, 6, 4, 6]
n = [2, 4, 5, 5, 5]

for i in range(len(func)):
    k = int(order[i]/2)
    h = float((b[i]-a[i])/n[i])
    hs = [h/2**i for i in range(k)]
    col1=[trapzRomberg(func[i],a[i],b[i],hi, f) for hi in hs]

    r = romberg(col1)

    print(r,end=", ")
print()