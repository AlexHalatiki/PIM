import numpy as np
from skimage import io

def equalizaImagem(caminho, nome, formato):
    imagem = io.imread(caminho)

    histograma = np.zeros(256)

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1

    histograma = histograma / imagem.size

    for i in range(1,256):
        histograma[i] += histograma[i-1]

    histograma = histograma * 255

    for i in range(0,256):
        histograma[i] = round(histograma[i])

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            imagem[i][j] = histograma[imagem[i][j]]

    io.imsave(f'./ex2/imagens_equalizadas/{nome}_equalizada.{formato}', imagem)

    print(f'{nome}:')
    print(histograma)
    print(imagem)
    print()


#equalizaImagem('./imagens/marilyn.jpg', 'marilyn', 'jpg')
#equalizaImagem('./imagens/figuraEscura.jpg', 'figuraEscura', 'jpg')
#equalizaImagem('./imagens/figuraClara.jpg', 'figuraClara', 'jpg')
equalizaImagem('./imagens/camily.jpg', 'camily_equalizada', 'jpg')



