# import the necessary packages
from collections import namedtuple
import numpy as np
import cv2
from scipy.spatial import distance

# define the `Detection` object
Detection = namedtuple("Detection", ["image_path", "gt", "pred"])


def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou
    # [int(1280 * 0.616144), int(720 * 0.537147), int(0.091191), int(0.453694)])]


hp = 720
wp = 1280
gt = [0.286719, 0.557639, 0.104688, 0.523611]
pred = [0.28399011, 0.5130461, 0.1406767, 0.59853404]

xgt = int((wp * gt[0]) - ((wp * gt[2]) / 2))
ygt = int(hp * gt[1] - ((hp * gt[3]) / 2))
wgt = int(((wp * gt[0]) - ((wp * gt[2]) / 2)) + wp * gt[2])
hgt = int((hp * gt[1] - ((hp * gt[3]) / 2)) + hp * gt[3])

xpr = int((wp * pred[0]) - ((wp * pred[2]) / 2))
ypr = int(hp * pred[1] - ((hp * pred[3]) / 2))
wpr = int(((wp * pred[0]) - ((wp * pred[2]) / 2)) + wp * pred[2])
hpr = int((hp * pred[1] - ((hp * pred[3]) / 2)) + hp * pred[3])

# define the list of example detections
examples = [
    Detection("/home/sverrir/Documents/Python/rgb_220.png", [xgt, ygt, wgt, hgt], [xpr, ypr, wpr, hpr])]

# loop over the example detections
for detection in examples:
    # load the image
    image = cv2.imread(detection.image_path)

    # draw the ground-truth bounding box along with the predicted
    # bounding box
    cv2.rectangle(image, tuple(detection.gt[:2]),
                  tuple(detection.gt[2:]), (255, 0, 0), 2)
    cv2.rectangle(image, tuple(detection.pred[:2]),
                  tuple(detection.pred[2:]), (0, 0, 255), 2)
    cv2.circle(image, (int(wp * gt[0]), int(hp * gt[1])), 2, (255, 0, 0), 2)
    cv2.circle(image, (int(wp * pred[0]), int(hp * pred[1])), 2, (0, 0, 255), 2)

    # compute the intersection over union and display it
    iou = bb_intersection_over_union(detection.gt, detection.pred)
    d = distance.euclidean((int(wp * gt[0]), int(hp * gt[1])), (int(wp * pred[0]), int(hp * pred[1])))
    cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    print("{}: {:.4f}".format(detection.image_path, iou))

    cv2.putText(image, "distance: {:.4f}".format(d), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    print("{}: {:.4f}".format(detection.image_path, d))

    # show the output image
    #cv2.imshow("Image", image)
    cv2.imwrite("/home/sverrir/Documents/Python/IOU.png", image)
    #cv2.waitKey(0)
