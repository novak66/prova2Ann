""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=1.05254 e y0=2.04769. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos
x1=1.07156, x2=1.12543, x3=1.19176, x4=1.22513, x5=1.2779, x6=1.33806, x7=1.36005, x8=1.41521, x9=1.48503, x10=1.52998, x11=1.58904, x12=1.6275, x13=1.6597, x14=1.72031, x15=1.76977, x16=1.82227, x17=1.87605, x18=1.94127, x19=1.99711 e x20=2.04476."""

def ralston(f, x0, y0, x_values, n):
    for i in range(n):
        m1 = f(x0, y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0 + 3/4 * h, y0 + m1 *3/4 * h )
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y*(2-x)+x+1


    
    
    
if __name__ == "__main__":
    func = lambda x, y: y * (2 - x) + x + 1
    
    x0 = 1.05254
    y0 = 2.04769
    x_values = [1.07156, 1.12543, 1.19176, 1.22513, 1.2779, 1.33806, 1.36005, 1.41521, 1.48503, 1.52998, 1.58904, 1.6275, 1.6597, 1.72031, 1.76977, 1.82227, 1.87605, 1.94127, 1.99711, 2.04476] 
    
    n = 20


    e = ralston(f,x0,y0, x_values, n)
    
    for _, i in e:
        print(f"{i},")