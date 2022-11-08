
'''
Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) em direção à ISS (International Space Station) com a missão de levar o AMS-2 (Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.
'''


def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    return somas


def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    return somas


def simp(x0,x1,x3,y0,y1,y2):
    return ((x1 - x0) / 3) * (y0 + 4 * y1 + y2)

answer = []
x = []
y = []

lista = []
lista.append((0, 0))
lista.append((5, 107))
lista.append((10, 227))
lista.append((15, 365))
lista.append((20, 513))
lista.append((25, 676))
lista.append((30, 819))
lista.append((35, 968))
lista.append((40, 1090))
lista.append((45, 1211))
lista.append((50, 1316))
lista.append((55, 1464))
lista.append((60, 1632))
lista.append((65, 1820))
lista.append((70, 2047))
lista.append((75, 2312))
lista.append((80, 2602))
lista.append((85, 2893))
lista.append((90, 3201))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
