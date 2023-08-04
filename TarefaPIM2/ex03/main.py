import cv2
import numpy as np
import math as m


def operadorMedia(image, linhasMedia, colunasMedia, valorMedia):
    border_heigth = int((linhasMedia - 1) / 2)
    border_width = int((colunasMedia - 1) / 2)

    image_with_border = cv2.copyMakeBorder(image, border_heigth, border_heigth, border_width, border_width, cv2.BORDER_CONSTANT, value=0)

    image = image.astype(np.float32)

    rows, cols = image_with_border.shape

    for row in range(border_heigth, rows - border_heigth):
        for col in range(border_width, cols - border_width):
            soma = 0
            for i in range(int(row - ((linhasMedia - 1) / 2)), int(row + ((linhasMedia - 1) / 2) + 1)):
                for j in range(int(col - ((colunasMedia - 1) / 2)), int(col + ((colunasMedia - 1) / 2) + 1)):
                    soma += (image_with_border[i][j] * valorMedia)
            image[row - border_heigth][col - border_width] = np.round(soma)

    image = image - image.min()
    image = image * 255 / image.max()
    image = np.uint8(image)

    return image


def escolhaVizinhos(i, j, valor):
    if(22.5 < valor <= 67.5):
        return i-1, j+1, i+1, j-1
    elif(67.5 < valor <= 112.5):
        return i-1, j, i+1, j
    elif(112.5 < valor <= 157.5):
        return i-1, j-1, i+1, j+1
    elif(157.5 < valor <= 180):
        return i, j-1, i, j+1
    elif(-22.5 < valor <= 22.5):
        return i, j+1, i, j-1
    elif(-67.5 < valor <= -22.5):
        return i+1, j+1, i-1, j-1
    elif(-112.5 < valor <= -67.5):
        return i+1, j, i-1, j
    elif(-157.5 < valor <= -112.5):
        return i+1, j-1, i-1, j+1
    elif(-180 < valor <= -157.5):
        return i, j-1, i, j+1

def operadorGradiente(caminho, nome, formato, linhasMatriz, colunasMatriz, X, Y):
    image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

    image = operadorMedia(image, 3, 3, 1/9)

    border_heigth = int((linhasMatriz - 1) / 2)
    border_width = int((colunasMatriz - 1) / 2)

    image_with_border = cv2.copyMakeBorder(image, border_heigth, border_heigth, border_width, border_width, cv2.BORDER_CONSTANT, value=0)
    image = image.astype(np.float32)

    image_float = image_with_border.astype(np.float32)
    direction = []

    rows, cols = image_with_border.shape

    for row in range(border_heigth, rows - border_heigth):
        aux = []
        for col in range(border_width, cols - border_width):
            somaX = 0
            somaY = 0
            linhaAux = 0
            for i in range(int(row - ((linhasMatriz - 1) / 2)), int(row + ((linhasMatriz - 1) / 2) + 1)):
                colunaAux = 0
                for j in range(int(col - ((colunasMatriz - 1) / 2)), int(col + ((colunasMatriz - 1) / 2) + 1)):
                    somaX += (image_with_border[i][j] * X[linhaAux][colunaAux]) 
                    somaY += (image_with_border[i][j] * Y[linhaAux][colunaAux])
                    colunaAux += 1
                linhaAux += 1
            image_float[row][col] = (m.sqrt(m.pow(somaX, 2) + m.pow(somaY, 2)))
            aux.append(m.degrees(m.atan2(somaY, (somaX + m.pow(10, -8)))))
        direction.append(aux)

    for row in range(border_heigth, rows - border_heigth):
        for col in range(border_width, cols - border_width):
            i1, j1, i2, j2 = escolhaVizinhos(row, col, direction[row - border_heigth][col - border_width])
            if(image_float[row][col] > image_float[i1][j1] and image_float[row][col] > image_float[i2][j2]):
                image[row - border_heigth][col - border_width] = image_float[row][col]

    image = image - image.min()
    image = image * 255 / image.max()
    image = np.uint8(image)

    cv2.imwrite(f'./ex03/imagensGradiente/{nome}_gradiente.{formato}', image)


prewittX = [
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]

prewittY = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

sobelX = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

sobelY = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

scharrX = [
    [-3, 0, 3],
    [-10, 0, 10],
    [-3, 0, 3]
]

scharrY = [
    [-3, -10, -3],
    [0, 0, 0],
    [3, 10, 3]
]

operadorGradiente('./imagens/Lua1_gray.jpg', 'Lua1_gray_Prewitt', 'jpg', 3, 3, prewittX, prewittY)
operadorGradiente('./imagens/Lua1_gray.jpg', 'Lua1_gray_Sobel', 'jpg', 3, 3, sobelX, sobelY)
operadorGradiente('./imagens/Lua1_gray.jpg', 'Lua1_gray_Scharr', 'jpg', 3, 3, scharrX, scharrY)
operadorGradiente('./imagens/chessboard_inv.png', 'chessboard_inv_Prewitt', 'jpg', 3, 3, prewittX, prewittY)
operadorGradiente('./imagens/chessboard_inv.png', 'chessboard_inv_Sobel', 'jpg', 3, 3, sobelX, sobelY)
operadorGradiente('./imagens/chessboard_inv.png', 'chessboard_inv_Scharr', 'jpg', 3, 3, scharrX, scharrY)

