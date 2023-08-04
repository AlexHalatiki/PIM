import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion, binary_dilation

def salvarImagem(nome, image):
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.savefig(f'{nome}.png', bbox_inches='tight', pad_inches=0)


# Definir a matriz W representando a imagem binária
W = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Definir o estruturante B
B = np.array([[0, 1, 0],
              [1, 1, 0],
              [0, 1, 0]])

salvarImagem('W', W)

X0 = binary_erosion(W, B)

X = X0
i = 0
salvarImagem(f'X{i}', X)

while True:
    X_previous = X
    X = binary_dilation(X_previous, B) & W
    if np.array_equal(X, X_previous):
        break
    i += 1
    salvarImagem(f'X{i}', X)

salvarImagem('ImagemFinal', X)



