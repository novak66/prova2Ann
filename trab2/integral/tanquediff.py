
'''
Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à medida que o tempo passa, conforme mostrado na tabela a seguir.
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
lista.append((0.0, 9.63))
lista.append((0.75, 9.26))
lista.append((1.5, 8.91))
lista.append((2.25, 8.43))
lista.append((3.0, 8.12))
lista.append((3.75, 7.71))
lista.append((4.5, 7.21))
lista.append((5.25, 6.78))
lista.append((6.0, 6.52))
lista.append((6.75, 6.02))
lista.append((7.5, 5.69))
lista.append((8.25, 5.16))
lista.append((9.0, 4.74))
lista.append((9.75, 4.47))
lista.append((10.5, 4.05))
lista.append((11.25, 3.54))
lista.append((12.0, 3.26))

for i in range(len(lista)):
    x.append(lista[i][0])
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
