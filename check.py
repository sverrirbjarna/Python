# importing the required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# here 0 means that the image is loaded in gray scale format
gray_image = cv2.imread("depth_0.png", -1)

ret, thresh_binary = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
ret, thresh_binary_inv = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh_trunc = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TRUNC)
ret, thresh_tozero = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TOZERO)
ret, thresh_tozero_inv = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TOZERO_INV)

# DISPLAYING THE DIFFERENT THRESHOLDING STYLES
names = ['Oiriginal Image', 'BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
images = gray_image, thresh_binary, thresh_binary_inv, thresh_trunc, thresh_tozero, thresh_tozero_inv

#for i in range(6):
#    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#    plt.title(names[i])
#    plt.xticks([]), plt.yticks([])
#plt.show()
# print(gray_image)
#plt.imshow(gray_image,'gray')
#plt.show()
#plt.imshow(thresh_binary)
# plt.imshow(thresh_binary_inv)
# plt.imshow(thresh_trunc)
# plt.imshow(thresh_tozero)
# plt.imshow(thresh_tozero_inv)

#imgplot = plt.imshow(gray_image)
#imgplot.set_cmap('gray')
#plt.show()

#imgplot = plt.imshow(thresh_binary)
#imgplot.set_cmap('Greys')
#plt.show()

#imgplot = plt.imshow(thresh_binary_inv)
#imgplot.set_cmap('Greys')
#plt.show()

img = gray_image.astype(np.uint8)
edges = cv2.Canny(img,0,250)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

