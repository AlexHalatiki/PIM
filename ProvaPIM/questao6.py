import numpy as np
import cv2

# Definindo funcao que calcula o limiar via Isodata

def limiar_isodata(matriz, iteracoes=10, limiar=0.5):
    for i in range(iteracoes):
        group1 = matriz[matriz <= limiar]
        group2 = matriz[matriz > limiar]

        u1 = 0
        u2 = 0

        if(group1.size != 0):
            u1 = np.mean(group1)
        
        if(group2.size != 0):
            u2 = np.mean(group2)
        
        novo_limiar = (u1 + u2) / 2

        if abs(limiar - novo_limiar) < 0.01:
            break

        limiar = novo_limiar

    return limiar

# Definindo as mesmas matrizes da questao 5

blue = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,40,0,30,0,40,0],
        [0,0,0,0,0,0,0,0],
        [0,0,30,0,45,0,45,0],
        [0,0,0,0,0,0,0,0],
        [0,0,30,0,35,0,45,0],
        [0,0,0,0,0,0,0,0]]

green = [[0,0,0,0,0,0,0,0],
        [0,0,130,0,110,0,120,0],
        [0,215,0,250,0,250,0,0],
        [0,0,255,0,255,0,230,0],
        [0,210,0,255,0,250,0,0],
        [0,0,115,0,110,0,115,0],
        [0,110,0,110,0,115,0,0],
        [0,0,0,0,0,0,0,0]]

red = [[0,0,0,0,0,0,0,0],
        [0,10,0,15,0,15,0,0],
        [0,0,0,0,0,0,0,0],
        [0,15,0,15,0,15,0,0],
        [0,0,0,0,0,0,0,0],
        [0,10,0,10,0,10,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

# Definindo a matriz gray inicialmente com zeros
      
gray = np.zeros((6,6))

# Aplicando Bayer e gerando a matriz gray a partir das outras 3

for i in range(1, 7):
    for j in range(1, 7):
        if(blue[i][j] != 0):
            green[i][j] = (green[i-1][j] + green[i][j-1] + green[i][j+1] + green[i+1][j]) / 4
            red[i][j] = (red[i-1][j-1] + red[i-1][j+1] + red[i+1][j-1] + red[i+1][j+1]) / 4
            gray[i-1][j-1] = 0.3 * red[i][j] + 0.6 * green[i][j] + 0.1 * blue[i][j]
            continue
        if(green[i][j] != 0):
            if blue[i+1][j] == 0:
                red[i][j] =  (red[i-1][j] + red[i+1][j]) / 2
                blue[i][j] = (blue[i][j-1] + blue[i][j+1]) / 2
            else:
                blue[i][j] =  (blue[i-1][j] + blue[i+1][j]) / 2
                red[i][j] = (red[i][j-1] + red[i][j+1]) / 2
            gray[i-1][j-1] = 0.3 * red[i][j] + 0.6 * green[i][j] + 0.1 * blue[i][j]
            continue
        if(red[i][j] != 0):
            blue[i][j] = (blue[i-1][j-1] + blue[i-1][j+1] + blue[i+1][j-1] + blue[i+1][j+1]) / 4
            green[i][j] = (green[i-1][j] + green[i][j-1] + green[i][j+1] + green[i+1][j]) / 4
            gray[i-1][j-1] = 0.3 * red[i][j] + 0.6 * green[i][j] + 0.1 * blue[i][j]

# Imprimindo a matriz gray

print("Matriz de entrada (tons de cinza): \n")

for i in range(0,6):
    for j in range(0,6):
        print(f"{gray[i][j]:.2f}  ", end="")
    print("\n")

print("\n\n")

# Normalizando a matriz gray para exibir na tela

gray_norm = (gray / np.max(gray)) * 255
gray_norm = gray_norm.astype(np.uint8)

# Exibindo a matriz gray normalizada

cv2.namedWindow('Imagem de entrada (tons de cinza)', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Imagem de entrada (tons de cinza)', 400, 400)
cv2.imshow('Imagem de entrada (tons de cinza)', gray_norm)

# Encontrando limiar na matriz gray

limiar = limiar_isodata(gray)

print(f"Limiar encontrado: {limiar:.2f}\n")

print("\n\n")

# Aplicando o limiar encontrado na matriz gray

for i in range(0,6):
    for j in range(0,6):
        if(gray[i][j] <= limiar):
            gray[i][j] = 0
        else:
            gray[i][j] = 255

# Imprimindo a matriz gray limiarizada

print("Matriz de saida (limiarizada): \n")

for i in range(0,6):
    for j in range(0,6):
        print(f"{gray[i][j]:.2f}  ", end="")
    print("\n")

print("\n\n")

# Exibindo a matriz gray limiarizada

cv2.namedWindow('Imagem de saida (limiarizada)', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Imagem de saida (limiarizada)', 400, 400)
cv2.imshow('Imagem de saida (limiarizada)', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

