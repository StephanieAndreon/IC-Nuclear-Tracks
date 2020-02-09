import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_yen
from skimage import io
import os
from skimage.color import rgb2gray


original = io.imread(os.path.join('/home/stephanie/Desktop/vidro-3/vidro3-10s', 'vidro3f1.tiff'))
grayscale = rgb2gray(original)
image = grayscale

thresh = threshold_yen(image)
binary = image > thresh

fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()
