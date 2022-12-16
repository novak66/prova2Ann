""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.0522 e y0=2.2573. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.125. """

def RK4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    return y*(1-x)+x+2
    
if __name__ == "__main__":    
    func = lambda x,y: y * (1 - x) + x + 2
    x0 = 1.8465
    y0 = 1.3043
    h = 0.1319
    
    n = 15
    
    r = RK4(func,x0,y0, h,n)
    
    for _, i in r:
        print(f"{i},")
