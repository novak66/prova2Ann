import numpy as np

def best_line(x, y):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a + b*x;

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

# exemplo:
x = [0.107, 0.3781, 0.8995, 1.2336, 1.5526, 1.7583, 1.9559, 2.197, 2.6382, 3.1056, 3.4249, 3.6408, 3.8204, 4.287, 4.4021, 4.7155, 5.2488, 5.5088, 5.7733, 6.1946, 6.291, 6.7364, 7.1057, 7.4486, 7.6079, 7.91, 8.2496, 8.6242, 8.8946, 9.305, 9.5334, 9.8058]
y =  [2.5661, 3.3753, 4.9357, 6.1475, 6.2578, 7.1889, 7.4496, 8.643, 9.573, 10.8016, 11.6449, 12.5737, 13.2745, 14.4719, 15.0215, 15.6066, 17.3302, 17.5543, 18.6194, 20.3814, 20.1264, 22.414, 22.5902, 23.3601, 23.2164, 24.8425, 25.8412, 26.7133, 27.6491, 28.6856, 29.4063, 30.2535]

a0, a1 = best_line(x, y)

print(f'{a0} e {a1}')

p = build_func(a0, a1)

x_values = [1.8805, 2.654, 2.7019, 4.9385, 8.758]
 
for xi_v in x_values:
    print(p(xi_v))