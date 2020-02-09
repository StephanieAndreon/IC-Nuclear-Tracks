import matplotlib.pyplot as plt
from skimage.filters import threshold_yen
from skimage import io
import os
from skimage.color import rgb2gray
#image = data.camera()

original = io.imread(os.path.join('/home/stephanie/Desktop/vidro-3/vidro3-70s', 'v3a7f5.tiff'))
grayscale = rgb2gray(original)
image = grayscale

fig, ax = try_all_threshold(image, figsize=(10, 8), verbose=False)
plt.show()
