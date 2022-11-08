
import math
import numpy as np

def richardson(x, b=1):
    n = len(x)
    for k in range(1, n):
        for i in range(n - k):
            numer = 2 ** (b * k) * x[i + 1] - x[i]
            denom = 2 ** (b * k) - 1
            aprox = numer/denom
            x[i] = aprox
    return x[0]


def dif_fin(coeffs,f, x):
    return sum(ci * f(xi) for ci, xi in zip(coeffs, x))



if __name__ == '__main__':
    def f(x):
        return (x**2)*math.e(-x)*math.cos(x) + 1
    
    x0 =  2.7004
    h = 0.39691
    
    def F1(h):
        return (f(x0 + h) - f(x0))/h
    
    
    col_F1 = [-0.1672764059740155, -0.13066885240655512, -0.1124180983100711, -0.10333626058889678, -0.09880981759665275, -0.09655065132622553]
    #F1(h), F1(h/2), F1(h/4), F1(h/8), F1(h/16)
    print (col_F1)
    
    aprox = richardson(col_F1)
    print('o erro e ', len(col_F1))
    print('aprox', aprox)
    
    