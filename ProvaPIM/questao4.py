import numpy as np

# definindo matriz de pontos

pontos = np.array([
    [650.7, 2000.0, 1500.0, 1.0],
    [653.5, 2000.0, 1500.0, 1.0],
    [650.7, 1990.0, 1500.0, 1.0],
    [645.3, 500.3, 1500.0, 1.0],
    [645.0, 500.3, 1500.0, 1.0],
    [645.3, 500.3, 1500.0, 1.0]
])

# definindo M completa

m_completa = np.array([
    [1/0.0075, 0, 2048/5, 0],
    [0, -1/0.0075, 2048/5, 0],
    [0, 0, 1/5, 0]
])

pontos_pixel = []

# Aplicando M completa em cada ponto e transformando em pixel (dividindo por (z/d))

for ponto in pontos:
    aux = np.dot(m_completa, ponto) / (ponto[2] / 5)
    pontos_pixel.append([aux[0], aux[1]])

# Imprimindo cada ponto em pixel

for p in pontos_pixel:
    print(f"[{p[0]:.2f}, {p[1]:.2f}]")