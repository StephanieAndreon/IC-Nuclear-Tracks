import matplotlib.pyplot as plt
import cv2
from skimage import data, color, img_as_ubyte
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

from skimage import io
import numpy as np
import PIL
from PIL import Image

from skimage.filters import threshold_isodata

#Load Image
img = Image.open('vidro1.tif')
img_thresh = cv2.imread('vidro1.tif')
thresh = threshold_isodata(img_thresh)
print(thresh)

#Make array of image
img_arr = np.array(img)

#detect edges
edges = canny(img_arr, sigma=2.0, low_threshold=0.55, high_threshold=0.8)
##Calculate threshold


# Perform a Hough Transform
# The accuracy corresponds to the bin size of a major axis.
# The value is chosen in order to get a single high accumulator.
# The threshold eliminates low accumulators
result = hough_ellipse(edges, accuracy=20, threshold=thresh, min_size=100, max_size=120)
print('Estou aqui')
result.sort(order='accumulator')


# Estimated parameters for the ellipse
best = list(result[-1])
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]
