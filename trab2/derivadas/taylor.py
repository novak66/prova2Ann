import numpy as np
import math

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada

def coeffs_dif_fin(x, x0, k):
    n = len(x)

    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row = [xi ** i for xi in x]
        A.append(row)
        # construção da matrz B
        if i < k:
            B.append(0)
        else:
            bi = math.factorial(i) * x0 ** (i-k) / math.factorial(i - k) 
            B.append(bi)
    return np.linalg.solve(A, B)
        

def dif_fin(coeffs,f, x):
    return sum(ci * f(xi) for ci, xi in zip(coeffs, x))
        

if __name__ == '__main__':
    # exemplo 1:
    def f(x):
        return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
    def p(xp):
        x0 = 0.4823
        k = 3
        n = 10 # numero de pontos igualmente espaçados
        # queremos pontos no intervalo [x0-e, x0+e]
        # ao diminuir o epsilon (e) os pontos são cada vez mais próximos
        e = 0.001
        x = [0.2416, 0.3199, 0.364, 0.388, 0.4681, 0.5291, 0.5491, 0.5965, 0.6558, 0.7174]
        y = [f(xi) for xi in x]
        
        coeffs = coeffs_dif_fin(x, x0, 1)
        f_1 = dif_fin(coeffs,f, x)
        
        coeffs = coeffs_dif_fin(x, x0, 2)
        f_2 = dif_fin(coeffs,f, x)
        
        coeffs = coeffs_dif_fin(x, x0, 3)
        f_3 = dif_fin(coeffs,f, x)
        
        coeffs = coeffs_dif_fin(x, x0, 4)
        f_4 = dif_fin(coeffs,f, x)
        
        coeffs = coeffs_dif_fin(x, x0, 5)
        f_5 = dif_fin(coeffs,f, x)
        return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3) + (f_4/24) *((xp -x0)**4) + (f_5/120) *((xp -x0)**5)
    
    
    values = [0.2939, 0.3162, 0.3252, 0.4354, 0.5452]
    px = [p(vi) for vi in values]
    print(f'{px}')

    fx_menos_px = [np.abs(f(vi) - p(vi)) for vi in values]
    print(f'{fx_menos_px}')