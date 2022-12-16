""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.70413 e y0=2.29604. Use o método de Runge-Kutta de ordem 2 com b=0.67687 para estimar o valor da solução exata desse PVI nos pontos
x1=0.74709, x2=0.79084, x3=0.84863, x4=0.89447, x5=0.93033, x6=0.98228, x7=1.02367, x8=1.08151, x9=1.12528, x10=1.18806, x11=1.21152, x12=1.2605, x13=1.31232, x14=1.37394, x15=1.44834, x16=1.46184, x17=1.53036, x18=1.56183, x19=1.63693 e x20=1.69858."""

def RK2(f, x0, y0, h, n, b=0.53):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y*(1-x)+x+2
    
if __name__ == "__main__":
    func = lambda x, y: y * (1 - x) + x + 2
    
    x0 = 0.70413
    y0 = 2.29604
    x_values = [0.74709, 0.79084, 0.84863, 0.89447, 0.93033, 0.98228, 1.02367, 1.08151, 1.12528, 1.18806, 1.21152, 1.2605, 1.31232, 1.37394, 1.44834, 1.46184, 1.53036, 1.56183, 1.63693, 1.69858]
    b = 0.67687

    n = 20
    
    e = RK2(f,x0,y0, x_values,n, b)

    for _, i in e:
        print(f"{i},")