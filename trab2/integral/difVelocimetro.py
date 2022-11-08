

'''
A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 segundos, numa corrida na Daytona International Speedway, Flórida.
'''

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    return somas

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1 - x0) / 3) * (y0 + 4 * y1 + y2)


def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    return somas

answer = []
x = []
y = []

lista = []
lista.append((0.0, 265.51))
lista.append((5.0, 109.64))
lista.append((10.0, 141.1))
lista.append((15.0, 196.89))
lista.append((20.0, 290.57))
lista.append((25.0, 180.42))
lista.append((30.0, 232.18))
lista.append((35.0, 215.67))
lista.append((40.0, 279.38))
lista.append((45.0, 150.79))
lista.append((50.0, 123.23))
lista.append((55.0, 173.7))
lista.append((60.0, 244.08))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
