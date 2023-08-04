import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.stats import entropy

def processaImagem(caminho, nome):
    imagem = io.imread(caminho)

    media = np.mean(imagem)
    variancia = np.var(imagem)

    histograma, intervalos = np.histogram(imagem, bins=range(257))
    entropia = entropy(histograma)

    print(f'Imagem {nome}:')
    print("Média: ", media)
    print("Variância: ", variancia)
    print("Entropia: ", entropia)
    print()

    plt.bar(intervalos[:-1], histograma, width=1.0, color='b')
    plt.xlim([0, 255])
    plt.xlabel('Intensidade')
    plt.ylabel('Quantidade')
    plt.savefig(f'./ex1/histogramas/{nome}_histograma.png')


processaImagem('./imagens/figuraClara.jpg', 'figuraClara')
processaImagem('./imagens/figuraEscura.jpg', 'figuraEscura')
processaImagem('./imagens/lena_B.png', 'lena')
processaImagem('./ex2/imagens_equalizadas/figuraClara_equalizada.jpg', 'figuraClara_equalizada')
processaImagem('./ex2/imagens_equalizadas/figuraEscura_equalizada.jpg', 'figuraEscura_equalizada')
processaImagem('./ex2/imagens_equalizadas/marilyn_equalizada.jpg', 'marilyn_equalizada')