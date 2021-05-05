import numpy as np
import matplotlib.pyplot as plt

from skimage import measure
from skimage import io
import os

image = io.imread(os.path.join('./images/binary.tiff'),
                  as_gray=True)

contours = measure.find_contours(image, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()

for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
