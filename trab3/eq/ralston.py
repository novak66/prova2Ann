""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=1.07249 e y0=1.68656. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.125. """

def ralston(f, x0, y0, h,n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + 3/4 * h, y0 + m1 *3/4 * h )
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y*(2-x)+x+1


    
    
    
if __name__ == "__main__":
    func = lambda x, y: y * (2 - x) + x + 1
    
    x0 = 0.86572
    y0 = 2.10388
    h = 0.13583
    
    n = 15


    e = ralston(f,x0,y0, h, n)
    
    for _, i in e:
        print(f"{i},")