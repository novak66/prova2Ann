import math

"""No livro Looking at History Through Mathematics, Rashevsky [Ra], p. 103-110, considera um modelo para um problema envolvendo a produção de rebendes na sociedade. Considere uma sociedade com x(t) indivíduos no instante t, em anos, e suponha que todo rebelde que se acasale com outro rebelde tenha filhos também rebeldes, enquanto uma proporção fixa r de todos os filhos de outros tipos de acasalamento também seja rebelde. Se for suposto que as taxas de nascimento e mortalidade para todos os indivíduos são as constantes λ e μ, respectivamente, e se não rebeldes e rebeldes se acasalam aleatoriamente, o problema pode ser expresso pelas equações diferenciais
dx(t)dt=(λ−μ)x(t)edxn(t)dt=(λ−μ)xn(t)+rλ(x(t)−xn(t)),
em que xn(t) denota o número de rebeldes na população no instante t.
Suponha que a variável p(t)=xn(t)/x(t) seja introduzida para representar a proporção de rebeldes na sociedade no instante t. Neste caso, as equações diferenciais acima podem ser combinadas e simplificadas na única equação diferencial
dp(t)dt=rλ(1−p(t)).
Considerando p(t0)=p0, com t0=0, p0=0.00149, λ=0.02954, μ=0.0079 e r=0.15938, use o método de Runge-Kutta de ordem 4 para encontrar aproximações para a solução p(t) nos instantes

Sugestões:
Note que os tempos tk não são igualmente espaçados. Assim, na k-ésima iteração, você deve usar hk=tk−tk−1, k=1,2,…,150.
Para encontrar a solução exata use o Wolfram Alpha
"""

def rk4(f, x0, y0,x_values, n):
    r = []
    h = x_values[0] - x0
    for _ in range(n):
        #realizar as iterações
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 = x_values[_]
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r
    
# modificar valores de r e lambd    
def f(p, t):
    r = 0.15938
    lambd = 0.02954
    k = r * lambd
    return k * (1 - t)

# modificar valor de p0    
t0 = 0
p0 = 0.00149
t_values = [0.38699, 1.12518, 1.75867, 2.08651, 2.79019, 3.63728, 4.38579, 5.14329, 5.75768, 6.38763, 7.24528, 7.67987, 8.2421, 8.95632, 9.61754, 10.14242, 11.0967, 11.45428, 12.07697, 13.20305, 13.6692, 14.34673, 15.11959, 15.875, 16.14948, 16.8441, 17.78968, 18.4115, 19.08776, 19.62894, 20.49526, 20.7559, 21.49624, 22.07336, 22.86464, 23.6358, 24.12518, 24.74374, 25.61907, 26.42701, 27.24183, 27.58744, 28.43286, 29.01265, 29.738, 30.56104, 30.84887, 31.76625, 32.10913, 33.12777, 33.88272, 34.21846, 35.26554, 35.41933, 36.39281, 37.15735, 37.58087, 38.13864, 39.21207, 39.86256, 40.14165, 40.92177, 41.72487, 42.25854, 42.8703, 43.46813, 44.20714, 45.00462, 45.70538, 46.3665, 46.87471, 47.8404, 48.25912, 49.21569, 49.61841, 50.23469, 51.12881, 51.57891, 52.08128, 52.94072, 53.56239, 54.2351, 54.95487, 55.90068, 56.2688, 56.82804, 57.79542, 58.54843, 59.22547, 59.74181, 60.06702, 61.18264, 61.92517, 62.47303, 63.18987, 63.86721, 64.51469, 64.81737, 65.40278, 66.31458, 66.74708, 67.88451, 68.16418, 68.76977, 69.51747, 70.47597, 70.92586, 71.60513, 72.42708, 72.78149, 73.66516, 74.58854, 75.12912, 75.71456, 76.2191, 77.12263, 77.8441, 78.48023, 79.18316, 79.82323, 80.13509, 81.03833, 81.64084, 82.17256, 83.03649, 83.48992, 84.50996, 84.74213, 85.80607, 86.38152, 86.771, 87.79292, 88.16834, 89.20641, 89.46365, 90.26034, 90.81635, 91.45048, 92.49921, 92.86965, 93.6108, 94.59791, 95.04687, 95.41767, 96.42216, 97.16986, 97.75586, 98.25229, 99.13134, 99.75286]

n = 150

r = rk4(f, t0, p0, t_values, n)

runge = []
for yi in r:
    runge.append(yi[1])
    
# solução exata:
# modificar valores de r, lambd e coef 
def p(t):
    r = 0.15938
    lambd = 0.02954
    k = r * lambd
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao
    coef = 0.9986
    return 1 - coef * math.exp(-k*t)
    
for i in range(150):
    print(f"{runge[i]}, {0},")