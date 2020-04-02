import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import glob


for filename in glob.glob(os.path.join( '/home/sverrir/Documents/Python/depth_26.png')):
#for filename in glob.glob(os.path.join( '*.png')):

    gray_image = cv2.imread(filename, -1)
    img = gray_image.astype(np.uint8)
    cv2.imwrite(filename,cv2.cvtColor(img, cv2.COLOR_RGB2BGR))