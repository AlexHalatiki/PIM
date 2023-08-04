import numpy as np
import cv2

# Declarando cada matriz RGB com bordas de zeros

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

# Aplicando Bayer nas matrizes

for i in range(1, 7):
    for j in range(1, 7):
        if(blue[i][j] != 0):
            green[i][j] = (green[i-1][j] + green[i][j-1] + green[i][j+1] + green[i+1][j]) / 4
            red[i][j] = (red[i-1][j-1] + red[i-1][j+1] + red[i+1][j-1] + red[i+1][j+1]) / 4
            continue
        if(green[i][j] != 0):
            if blue[i+1][j] == 0:
                red[i][j] =  (red[i-1][j] + red[i+1][j]) / 2
                blue[i][j] = (blue[i][j-1] + blue[i][j+1]) / 2
            else:
                blue[i][j] =  (blue[i-1][j] + blue[i+1][j]) / 2
                red[i][j] = (red[i][j-1] + red[i][j+1]) / 2
            continue
        if(red[i][j] != 0):
            blue[i][j] = (blue[i-1][j-1] + blue[i-1][j+1] + blue[i+1][j-1] + blue[i+1][j+1]) / 4
            green[i][j] = (green[i-1][j] + green[i][j-1] + green[i][j+1] + green[i+1][j]) / 4

# Imprimindo cada matriz aplicada

print("Red:\n")

for i in range(1,7):
    for j in range(1,7):
        print(f"{red[i][j]:.2f}  ", end="")
    print("\n")

print("\n\n")

print("Green:\n")

for i in range(1,7):
    for j in range(1,7):
        print(f"{green[i][j]:.2f}  ", end="")
    print("\n")

print("\n\n")

print("Blue: \n")

for i in range(1,7):
    for j in range(1,7):
        print(f"{blue[i][j]:.2f}  ", end="")
    print("\n")

print("\n\n")

# Normalizando as matrizes para exibir na tela

blue = (blue / np.max(blue)) * 255
blue = blue.astype(np.uint8)

green = (green / np.max(green)) * 255
green = green.astype(np.uint8)

red = (red / np.max(red)) * 255
red = red.astype(np.uint8)

# Realizando merge das matrizes

imagem_colorida = cv2.merge((blue, green, red))

# Exibindo a imagem gerada

cv2.namedWindow('Imagem colorida com borda de zeros', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Imagem colorida com borda de zeros', 400, 400)
cv2.imshow("Imagem colorida com borda de zeros", imagem_colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()

