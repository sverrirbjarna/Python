from __future__ import print_function
from PIL import Image
import cv2 as cv
alpha = 0.2
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')
#input_alpha = float(raw_input().strip())
#if 0 <= alpha <= 1:
#    alpha = input_alpha
# [load]
src1 = cv.imread(cv.samples.findFile('rgb_13.png'))
src2 = cv.imread(cv.samples.findFile('depth_13.png'))

src2 = cv.resize(src2, (0,0), fx=1.45, fy=1.45)

width, height = src2.shape[1],src2.shape[0]
y = (height-720)/2
x = (width-1280)/2
print(x,y)
src2 = src2[160:160+720, 255:255+1280]
print(width,height)
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
beta = (1.0 - alpha)
dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()