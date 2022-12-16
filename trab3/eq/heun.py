""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.25471 e y0=1.73075. Use o método de Heun para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.125. """

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

def f(x,y):
    return y*(2-x)+x+1

if __name__ == "__main__":    
    
    func = lambda x, y: y * (2 - x) + x + 1
    x0 = 1.42441
    y0 = 2.26192
    h = 0.16625
    n = 15

    
    r = heun(func, x0, y0, h, n)

    for _, v in r:
        print(f"{v},")
