import cv2
import matplotlib.pyplot as plt 

image = cv2.imread("/home/sverrir/Documents/Python/dep.png", -1)
img_scaled = cv2.normalize(image, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)
#plt.imshow(image, cmap="gray", vmin=0, vmax=4096)
#plt.show()
#plt.imshow(img_scaled, cmap="gray")
#plt.show()

f = plt.figure()
f.add_subplot(1,2, 1)
plt.imshow(image, cmap="gray", vmin=0, vmax=4096)
f.add_subplot(1,2, 2)
plt.imshow(img_scaled,cmap="gray")
plt.show(block=True)