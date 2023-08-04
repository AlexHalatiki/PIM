import cv2
import numpy as np

def operadorLaplaciano(caminho, nome, formato, linhasMatriz, colunasMatriz, matrizLaplaciana):
    image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

    border_heigth = int((linhasMatriz - 1) / 2)
    border_width = int((colunasMatriz - 1) / 2)

    image_with_border = cv2.copyMakeBorder(image, border_heigth, border_heigth, border_width, border_width, cv2.BORDER_CONSTANT, value=0)

    image_float = image.astype(np.float32)

    rows, cols = image_with_border.shape

    for row in range(border_heigth, rows - border_heigth):
        for col in range(border_width, cols - border_width):
            soma = 0
            linhaLaplaciana = 0
            for i in range(int(row - ((linhasMatriz - 1) / 2)), int(row + ((linhasMatriz - 1) / 2) + 1)):
                colunaLaplaciana = 0
                for j in range(int(col - ((colunasMatriz - 1) / 2)), int(col + ((colunasMatriz - 1) / 2) + 1)):
                    soma += (image_with_border[i][j] * matrizLaplaciana[linhaLaplaciana][colunaLaplaciana])
                    colunaLaplaciana += 1
                linhaLaplaciana += 1
            image_float[row - border_heigth][col - border_width] += (-soma)

    image_float = image_float - image_float.min()
    image_float = image_float * 255 / image_float.max()
    image_float += image
    image_float = image_float - image_float.min()
    image_float = image_float * 255 / image_float.max()
    image_float = np.uint8(image_float)

    cv2.imwrite(f'./ex02/imagensLaplace/{nome}_laplace.{formato}', image_float)


A = [
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
]

B = [
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
]

operadorLaplaciano('./imagens/11_test.png', '11_test_A', 'png', 3, 3, A)
operadorLaplaciano('./imagens/11_test.png', '11_test_B', 'png', 3, 3, B)






