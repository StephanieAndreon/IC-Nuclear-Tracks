import matplotlib.pyplot as plt
from skimage.filters import threshold_yen, threshold_triangle, threshold_li, threshold_isodata
from skimage import io, measure
from skimage.color import rgb2gray

original = io.imread(r'C:\Users\andre\PycharmProjects\IC-Nuclear-Tracks\images\vidro3f6.tif')
grayscale = rgb2gray(original)
image = grayscale


def convert_to_binary(image, threshold_algorithm='yen', save_binary_image=True, verbose=True):
    loaded_image = io.imread(image)
    grayscale_image = rgb2gray(loaded_image)

    thresh = threshold_yen(grayscale_image)
    if threshold_algorithm == 'triangle':
        thresh = threshold_triangle(image)
    elif threshold_algorithm == 'isodata':
        thresh = threshold_isodata(image)
    elif threshold_algorithm == 'li':
        thresh = threshold_li(image)

    binary = grayscale_image > thresh

    if verbose:
        plt.imshow(binary, cmap='gray')
    if save_binary_image:
        plt.savefig('./images/binary.tiff')

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


binary = convert_to_binary('images/vidro3f6.tif')
draw_countours_on_binary_image(binary)
