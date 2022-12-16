""" A taxa de crescimento de uma população P ao longo do tempo t (em anos), com taxa de natalidade constante λ e taxa de emigração constante ν é modelada pela seguinte equação diferencial
dPdt=λP−ν,
Assuma que a população de um país em t=0 seja de 1102403 indivíduos, que a taxa de natalidade seja constante igual a λ=0.0463 e que ν=25719 seja a taxa de emigração anual. Use o método de Heun para estimar o número de indivíduos nessa população após 1 ano. Use tamanho do passo h=0.0625. """

from ast import Lambda


def heun(f,x0,y0,h,n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h *(m1 + m2) / 2
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r

#Q9 Prova:
def f(x,y):
    Lambda = 0.0463
    v = 25719  
    return Lambda * y - v

x0, y0 = 0 , 1102403
e = heun(f,x0,y0, h=0.0625,n=int(1/0.0625))

for xi, yi in e:
    print(xi, yi)
    
#ultimo tmb