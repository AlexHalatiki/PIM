import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

def fourier_masker_ver(image, i):
    f_size = 15
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(image))
    dark_image_grey_fourier[:590, 955:965] = i
    dark_image_grey_fourier[620:, 955:965] = i
    dark_image_grey_fourier[595:605, :940] = i
    dark_image_grey_fourier[595:605, 985:] = i
    fig, ax = plt.subplots(1,3,figsize=(15,15))
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize = f_size)
    ax[1].imshow(image, cmap = 'gray')
    ax[1].set_title('Image', fontsize = f_size);
    ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), 
                     cmap='gray')
    ax[2].set_title('Transformed Image', 
                     fontsize = f_size);
    plt.show()

    return abs(np.fft.ifft2(dark_image_grey_fourier))

img = imread('folhas1.jpg')

img_grade = imread('folhas1_reticulada.jpg')

img_fourier = fourier_masker_ver(img_grade, 1)

mse_fourier = mean_squared_error(img, img_fourier)
ssim_fourier = ssim(img, img_fourier,
                  data_range=img_fourier.max() - img_fourier.min())

print(f'MSE: {mse_fourier}')
print(f'SSIM {ssim_fourier}')

