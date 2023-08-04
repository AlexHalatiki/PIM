import cv2
import numpy as np
import math as m

def operadorGaussiano(caminho, nome, formato, linhasMatriz, colunasMatriz, matrizGaussiana):
    image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

    border_heigth = int((linhasMatriz - 1) / 2)
    border_width = int((colunasMatriz - 1) / 2)

    image_with_border = cv2.copyMakeBorder(image, border_heigth, border_heigth, border_width, border_width, cv2.BORDER_CONSTANT, value=0)

    rows, cols = image_with_border.shape

    for row in range(border_heigth, rows - border_heigth):
        for col in range(border_width, cols - border_width):
            soma = 0
            linhaGaussiana = 0
            for i in range(int(row - ((linhasMatriz - 1) / 2)), int(row + ((linhasMatriz - 1) / 2) + 1)):
                colunaGaussiana = 0
                for j in range(int(col - ((colunasMatriz - 1) / 2)), int(col + ((colunasMatriz - 1) / 2) + 1)):
                    soma += (image_with_border[i][j] * matrizGaussiana[linhaGaussiana][colunaGaussiana])
                    colunaGaussiana += 1
                linhaGaussiana += 1
            image[row - border_heigth][col - border_width] = np.round(soma)

    cv2.imwrite(f'./ex01/imagensGauss/{nome}_gauss.{formato}', image)


def matrizGaussiana(X, Y, o):
    matrizGaussiana = []

    for i in range(0, 3):
        aux = []
        for j in range(0, 3):
            aux.append(1 / (2*m.pi*m.pow(o, 2)) * m.exp(-(m.pow(X[i][j], 2) + m.pow(Y[i][j], 2)) / (2*m.pow(o, 2))))
        matrizGaussiana.append(aux)

    return matrizGaussiana


X = [
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]

Y = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

operadorGaussiano('./imagens/Lua1_gray.jpg', 'Lua1_gray3x3_0.6', 'jpg', 3, 3, matrizGaussiana(X, Y, 0.6))
operadorGaussiano('./imagens/Lua1_gray.jpg', 'Lua1_gray3x3_1.0', 'jpg', 3, 3, matrizGaussiana(X, Y, 1.0))

