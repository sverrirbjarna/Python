import numpy as np
import cv2

img_file = "depth_0.png"
img = cv2.imread(img_file, cv2.IMREAD_COLOR)           # rgb
alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # rgba
gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # grayscale

print (type(img))
print ('RGB shape: ', img.shape)        # Rows, cols, channels
print ('ARGB shape:', alpha_img.shape)
print ('Gray shape:', gray_img.shape)
print ('img.dtype: ', img.dtype)
print ('img.size: ', img.size)


cv2.imshow("image1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
