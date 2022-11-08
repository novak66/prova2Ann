import math

def double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:
    if n1 <= 0 or n2 <= 0:
        raise ValueError('Erro de valor')
    h1 = (b - a) / n1
    h2 = (d - c) / n2
    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c + j * h2)
    soma_arestas_horizontais = 0
    for i in range(1, n1):
        for j in [0, n2]:
            soma_arestas_horizontais += f(a + i * h1, c + j * h2)
    soma_arestas_verticais = 0
    for j in range(1, n2):
        for i in [0, n1]:
            soma_arestas_verticais += f(a + i * h1, c + j * h2)
    soma_vertices = 0
    for i in [0, n1]:
        for j in [0, n2]:
            soma_vertices += f(a + i * h1, c + j * h2)
    return (h1*h2/4)*(soma_vertices+4*soma_interior + 2*(soma_arestas_horizontais+soma_arestas_verticais))



'''
Use a regra dos trapézios para aproximar o valor da integral
'''

def f(x, y):
	#return math.cos(pow(x, 2)) * math.sin(pow(y, 2) * x) * math.exp(-math.pow(y, 2)) + 1
	return math.sqrt(math.exp((-x**2)*(y**2))+1)

intervalo1 = [-1.754, 1.614]
intervalo2 = [-1.603, 1.983]
n1 = 256
n2 = 128

# double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:

print(double_trapz(f, intervalo1[0], intervalo1[1], intervalo2[0], intervalo2[1], n1, n2))