import cv2
import numpy as np
from skimage import io, color

def equalizaMatriz(matriz):
    histograma = np.zeros(256)

    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            histograma[matriz[i][j]] += 1

    histograma = histograma / matriz.size

    for i in range(1,256):
        histograma[i] += histograma[i-1]

    histograma = histograma * 255

    for i in range(0,256):
        histograma[i] = round(histograma[i])

    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            matriz[i][j] = histograma[matriz[i][j]]

def equalizamatrizRGB(caminho, nome, formato):
    img = cv2.imread(caminho)

    blue = img[:, :, 0]
    green = img[:, :, 1]
    red = img[:, :, 2]

    equalizaMatriz(blue)
    equalizaMatriz(green)
    equalizaMatriz(red)

    matriz_equalizada = cv2.merge([blue, green, red])

    cv2.imwrite(f'./ex3/rgb_equalizadas/{nome}_equalizada.{formato}', matriz_equalizada)

def equalizamatrizYIQ(caminho, nome, formato):
    img = io.imread(caminho)

    img_yiq = color.rgb2yiq(img)

    img_yiq = img_yiq - img_yiq.min()
    img_yiq = img_yiq * 255 / img_yiq.max()
    img_yiq = np.uint8(img_yiq)

    y = img_yiq[:, :, 0]

    equalizaMatriz(y)

    img_yiq[:, :, 0] = y

    img_rgb = color.yiq2rgb(img_yiq)
   
    img_rgb = img_rgb - img_rgb.min()
    img_rgb = img_rgb * 255 / img_rgb.max()
    img_rgb = np.uint8(img_rgb)

    io.imsave(f'./ex3/yiq_equalizadas/{nome}_equalizada.{formato}', img_rgb)


#equalizamatrizRGB('./imagens/outono_LC.png', 'outono_equalizada', 'png')
#equalizamatrizRGB('./imagens/predios.jpeg', 'predios_equalizada', 'jpeg')
#equalizamatrizYIQ('./imagens/outono_LC.png', 'outono_equalizada', 'png')
#equalizamatrizYIQ('./imagens/predios.jpg', 'predios_equalizada', 'jpeg')
equalizamatrizRGB('./imagens/camily.jpg', 'camily_equalizada', 'jpg')
equalizamatrizYIQ('./imagens/camily.jpg', 'camily_equalizada', 'jpg')