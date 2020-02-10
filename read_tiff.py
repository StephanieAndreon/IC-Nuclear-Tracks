### Import necessary libraries ################################################
import cv2
import os
import matplotlib.pyplot as plt
from  matplotlib.pyplot import imshow
from skimage.color import rgb2gray
from skimage.filters import threshold_yen
from skimage.filters import threshold_isodata
from skimage import io
###############################################################################
######################## Parameters for editing ###############################

### Directory where images to be loaded are, change accordingly
diretorio = '/home/stephanie/Desktop/vidro-3/vidro3-10s/'
### Directory where images are to be saved, change accordingly
diretorio_save = '/home/stephanie/Desktop/'
### Threshold method, can be isodata or yen.
threshold_method = 'yen'
### If images are already grayscale, set is_gray = 1, else set to 0.
is_grayscale = 0
###############################################################################

###############################################################################
## Global variables ###########################################################
### Etching time based on directory name
tempo_exposicao = diretorio[39]

###############################################################################
######################### Functions ###########################################

### Function for loading images from a folder #################################
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

### Function for binarizing image according to threshold method ###############
def gray_to_binary_with_thresh_method(image, is_gray, thresh_method):
    ### Set image to graycale if needed
    if is_gray == 0:
        ### Convert to grayscale
        grayscale = rgb2gray(image)
    elif is_gray == 1:
        ### Does nothing to the image, already grayscale
        grayscale = image
    ### Determine threshold method to use according to parameter thresh_method
    if thresh_method == 'yen':
        ### Calculate treshold according to yen method
        thresh = threshold_yen(grayscale)
    elif thresh_method == 'isodata':
        ### Calculate treshold according to isodata method
        thresh = threshold_isodata(grayscale)
    else:
        print('Invalid threshold method! Please choose isodata or yen. ')

    ### Generate binary image
    binary = grayscale > thresh
    ### Show thresholded image
    plt.imshow(binary,cmap='gray')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ### Return binary image
    return binary


### Function for saving binarized images to desired folder #############
def save_binary_images_from_folder(folder, folder_save, is_gray, thresh_method):
    ### Create list with images from folder
    imagens = load_images_from_folder(folder)
    ### Get number of images in folder
    tamanho = len(imagens)
    ### Some output for debugging
    print('Numero de imagens no diretorio: ' + str(tamanho))
    ### Iterate over images in directory
    for i in range (0, tamanho):
        ### Create list to store binary images
        binary_imgs = []
        ### Generate binary image
        imgbw = gray_to_binary_with_thresh_method(imagens[i], is_gray, thresh_method)
        ### Add binary image to list binary_imgs
        binary_imgs.append(imgbw)
        filename = str(folder_save) + str(thresh_method) +'_v3a' + str(tempo_exposicao) + 'f' + str(i+1)+'.tiff'
        print(filename)

        img = io.imread(binary_imgs[i], as_gray=True)

        ### Save binary images to folder
        io.imsave(filename, img)

    return 0
################## End of Functions ##############################
##################################################################

save_binary_images_from_folder(str(diretorio), str(diretorio_save), is_grayscale, str(threshold_method))
