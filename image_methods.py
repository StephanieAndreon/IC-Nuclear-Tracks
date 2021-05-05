import matplotlib.pyplot as plt
from skimage.filters import threshold_yen, threshold_triangle, threshold_li, threshold_isodata, threshold_otsu, \
    threshold_minimum, threshold_local, threshold_sauvola, threshold_niblack, threshold_mean
from skimage import io, measure
from skimage.color import rgb2gray

original = io.imread(r'C:\Users\andre\PycharmProjects\IC-Nuclear-Tracks\images\vidro3f6.tif')
grayscale = rgb2gray(original)
image = grayscale


def convert_to_binary(image, threshold_algorithm='yen', save_binary_image=False, output_image='None', verbose=False):
    loaded_image = io.imread(image)
    grayscale_image = rgb2gray(loaded_image)

    thresh = threshold_yen(grayscale_image)
    if threshold_algorithm == 'triangle':
        thresh = threshold_triangle(grayscale_image)
    elif threshold_algorithm == 'isodata':
        thresh = threshold_isodata(grayscale_image)
    elif threshold_algorithm == 'li':
        thresh = threshold_li(grayscale_image)
    elif threshold_algorithm == 'otsu':
        thresh = threshold_otsu(grayscale_image)
    elif threshold_algorithm == 'local':
        thresh = threshold_local(grayscale_image, block_size=999)
    elif threshold_algorithm == 'sauvola':
        thresh = threshold_mean(grayscale_image)
    binary = grayscale_image > thresh

    if verbose:
        plt.imshow(binary, cmap='gray')
    if save_binary_image:
        plt.savefig(f'./images/{output_image}.tiff')

    return binary


def draw_countours_on_binary_image(image, save_image_with_countours=True, verbose=True):
    contours = measure.find_contours(image, 0.8)

    # Display the image and plot all contours found
    fig, ax = plt.subplots()

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=0.8)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    if verbose:
        plt.show()
    if save_image_with_countours:
        plt.savefig('images/image_with_countours.png')


binary = convert_to_binary('images/vidro3f6.tif', 'sauvola', verbose=True)
draw_countours_on_binary_image(binary)
