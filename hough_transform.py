

import matplotlib.pyplot as plt

from skimage import data, color, img_as_ubyte, io, measure
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

# Load picture, convert to grayscale and detect edges

image_gray = io.imread('./images/binary_black_bg_no_axis.tiff', as_gray=True)
image_rgb = color.gray2rgb(image_gray)
edges = canny(image_gray, sigma=2.0,
              low_threshold=0.55, high_threshold=0.8)
contours = measure.find_contours(image_gray, 0.8)

# Display the image and plot all contours found
for contour in contours:
    result = hough_ellipse(contour)
    result.sort(order='accumulator')

    # Estimated parameters for the ellipse
    best = list(result[-1])
    yc, xc, a, b = [int(round(x)) for x in best[1:5]]
    orientation = best[5]

# Draw the ellipse on the original image
    cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
    image_rgb[cy, cx] = (0, 0, 255)
# Draw the edge (white) and the resulting ellipse (red)
    edges = color.gray2rgb(img_as_ubyte(contour))
    edges[cy, cx] = (250, 0, 0)

    fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
                                    sharex=True, sharey=True)

    ax1.set_title('Original picture')
    ax1.imshow(image_rgb)

    ax2.set_title('Edge (white) and result (red)')
    ax2.imshow(edges)

    plt.show()