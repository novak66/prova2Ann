from nodesAndWeights import *


'''
Em uma pessoa contaminada com sarampo, o nível de vírus N (medido em número de células infectadas por mL de plasma de sangue) atinge um pico em cerca de t=12 dias (quando aparecem erupções cutâneas) e, então, diminui bem rápido como resultado da resposta imunológica. A área sob o gráfico de N(t) de t=0 a t=12 (como mostrado na figura) é igual à quantidade total de infecção necessária para desenvolver sintomas (medida em densidade de células infectadas x tempo). A função N tem sido modelada pela função
f(t)=-t(t-21)(t+1)
a) a regra dos trapézios com 31 subintervalos
b) a regra de Simpson com 14 subintervalos
c) o método de Romberg com h=12/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 6 estime a quantidade total de infecção necessária para desenvolver os sintomas de sarampo.
'''

def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


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

def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck*funcao(xk)

    return soma


def f(nome_funcao, value):
	x = value
	return eval(nome_funcao)

def change(nome_funcao, a, b):
	def g(u):
		return f(nome_funcao, (b+a)/2 + (b-a)*u/2) * (b-a)/2
	return g

answer = []
a = [0]
b = [12]
order = [8]
n = [10]
exact_for_degree_less_than = [6]
subintervalosTrapezio = 31
subintervalosSimpson = 14

funcs = ['-x*(x-21)*(x+1)']

def F(x):
	return -x*(x-21)*(x+1)

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
