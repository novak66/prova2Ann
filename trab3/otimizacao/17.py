import math
import numpy as np

"""Seja V o espaço vetorial das funções contínuas definidas no intervalo [a,b] com produto escalar definido por
⟨f,g⟩=∫baf(x)g(x)dx,
onde f e g são duas funções contínuas definidas em [a,b], com a=−1.25046 e b=1.46144.
O processo de ortogonalização de Gram-Schmidt consiste em transformar uma lista de n funções linearmente independentes
f1,f2,…,fn,
numa lista de n funções duas a duas ortogonais
g1,g2,…,gn,
definidas por g1=f1 e, para k=2,3,…,n,
gk=fk−∑i=1k−1ak,igi,
onde ak,i=⟨fk,gi⟩⟨gi,gi⟩.
Expandindo as expressões acima para n=4, ficamos com
g1g2g3g4=f1=f2−a2,1g1=f3−a3,1g1−a3,2g2=f4−a4,1g1−a4,2g2−a4,3g3
Assim, para ortogonalizar as funções f1,f2,…,fn, devemos apenas calcular os coeficientes ak,i.
Use o processo de ortogonalização de Gram-Schmidt para ortogonalizar a seguinte lista de 4 funções:
f1(x)=1, f2(x)=x, f3(x)=x2 e f4(x)=x3.
Para o cálculo dos coeficientes ak,i use a regra dos trapézios com 256 subintervalos."""


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def coef(f,g):
    # a = -1.05973 
    # b=1.4086
    a=-1.25046   
    b=1.46144
    n = 256
    func = lambda x: (f(x) * g(x) ) 
    func2 = lambda x: g(x) * g(x)
    numer = trapz(func,a,b,n)
    denom = trapz(func2,a,b,n)
    
    return (numer/denom)




# def coefs_comb(f, funcs):
#     a = -1
#     b= 1
#     n = 256
#     list_coefs = []
#     for gk in funcs:
#         numer = trapz(
#             lambda x: f(x) * gk(x),
#             a,
#             b,
#             n
#             )
#         denom = trapz(
#             lambda x: gk(x) * gk(x),
#             a,
#             b,
#             n
#                     )
#         ck = numer/denom
#         list_coefs.append(ck)
#     return list_coefs
        
if __name__ == '__main__':
    
    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3
    
    def g1(x): 
        return f1(x)

    a_21 =  coef(f2, g1)
    print(f'{a_21},')
    
    def g2(x):
        return f2(x) - a_21*g1(x)
    
    a_31 = coef(f3, g1)
    a_32 = coef(f3, g2)
    
    print(f'{a_31},')
    print(f'{a_32},')
    
    def g3(x): 
        return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = coef(f4, g1)
    a_42 = coef(f4, g2)
    a_43 = coef(f4, g3)
    
    print(f'{a_41},')
    print(f'{a_42},')
    print(f'{a_43},')
   
    def g4(x): 
        return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)
    
    
        
        