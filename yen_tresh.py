import matplotlib.pyplot as plt
from  matplotlib.pyplot import imshow
from skimage.filters import threshold_yen
from skimage import io
import os
from skimage.color import rgb2gray
#image = data.camera()

original = io.imread(os.path.join('/home/stephanie/Desktop/vidro-3/vidro3-10s', 'vidro3f1.tiff'))
grayscale = rgb2gray(original)
image = grayscale

thresh = threshold_yen(image)
binary = image > thresh

plt.imshow(binary,cmap='gray')
plt.show()
