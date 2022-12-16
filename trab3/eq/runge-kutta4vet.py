""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.5875 e y0=2.9699. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos
x1=0.6193, x2=0.6602, x3=0.7021, x4=0.7475, x5=0.7935, x6=0.8525, x7=0.893, x8=0.9703, x9=0.9999, x10=1.071, x11=1.1122, x12=1.1724, x13=1.211, x14=1.2796, x15=1.3239, x16=1.3529, x17=1.4189, x18=1.4565, x19=1.5199 e x20=1.5524."""

def RK4(f, x0, y0, x_values, n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
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
    x0 = 0.5875
    y0 = 2.9699
    x_values = [0.6193, 0.6602, 0.7021, 0.7475, 0.7935, 0.8525, 0.893, 0.9703, 0.9999, 1.071, 1.1122, 1.1724, 1.211, 1.2796, 1.3239, 1.3529, 1.4189, 1.4565, 1.5199, 1.5524]
        
    n = 20
    
    r = RK4(func,x0,y0, x_values,n)
    
    for _, i in r:
        print(f"{i},")
