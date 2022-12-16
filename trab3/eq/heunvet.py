""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.57634 e y0=0.32826. Use o método de Heun para estimar o valor da solução exata desse PVI nos pontos
x1=0.59839, x2=0.64828, x3=0.70499, x4=0.77033, x5=0.79517, x6=0.84893, x7=0.92106, x8=0.94064, x9=1.00252, x10=1.04805, x11=1.09281, x12=1.16886, x13=1.20296, x14=1.25178, x15=1.29556, x16=1.3409, x17=1.40369, x18=1.43691, x19=1.4833 e x20=1.53535. """

def heun(f,x0,y0,x_values,n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
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
    x0 = 0.57634
    y0 = 0.32826
    x_values = [0.59839, 0.64828, 0.70499, 0.77033, 0.79517, 0.84893, 0.92106, 0.94064, 1.00252, 1.04805, 1.09281, 1.16886, 1.20296, 1.25178, 1.29556, 1.3409, 1.40369, 1.43691, 1.4833, 1.53535]
        
    n = 20

    
    r = heun(func, x0, y0, x_values, n)

    for _, v in r:
        print(f"{v},")
