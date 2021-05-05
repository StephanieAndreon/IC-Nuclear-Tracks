import matplotlib.pyplot as plt
from skimage.filters import try_all_threshold
from skimage import io
import os


loaded_image = io.imread(os.path.join('./images/vidro3f6.tif'),
                         as_gray=True)
temp_image = loaded_image

fig, ax = try_all_threshold(temp_image, figsize=(12, 5))


fig, ax = try_all_threshold(temp_image, figsize=(10, 5))
plt.show()
