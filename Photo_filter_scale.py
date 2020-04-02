import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import glob



for filename in glob.glob(os.path.join( '*.png')):

    gray_image = cv2.imread(filename, -1)
    img = gray_image.astype(np.uint8)
    img = cv.resize(img, (0, 0), fx=1.45, fy=1.45)
    width, height = img.shape[1], src2.shape[0]
    y = (height - 720) / 2
    x = (width - 1280) / 2
    print(x, y)
    img = img[160:160 + 720, 255:255 + 1280]

    cv2.imwrite(filename,cv2.cvtColor(img, cv2.COLOR_RGB2BGR))