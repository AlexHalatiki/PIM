import cv2
import numpy as np

def operadorMedia(caminho, nome, formato, linhasMedia, colunasMedia, valorMedia):
    image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

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

    cv2.imwrite(f'./ex01/imagensMedia/{nome}_media.{formato}', image)

operadorMedia('./imagens/Lua1_gray.jpg', 'Lua1_gray_3x3', 'jpg', 3, 3, 1/9)
operadorMedia('./imagens/Lua1_gray.jpg', 'Lua1_gray_5x5', 'jpg', 5, 5, 1/9)

