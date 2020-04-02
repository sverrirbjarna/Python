import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/sverrir/Documents/Python/dep.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[10000],[0,10000])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()