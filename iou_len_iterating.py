from collections import namedtuple
import cv2
from scipy.spatial import distance
import argparse

nr = 1
hp = 720
wp = 1280
for nr in range(1, 30):
    print(str(nr).zfill(2))
    pathg = "/home/sverrir/Documents/Yolo_data/Testset/"+str(nr).zfill(2)+".txt"
    #pathp = "/home/sverrir/Documents/Yolo_data/Testset/"+str(nr)+".txt"
    pathp = "/home/sverrir/Documents/Yolo_data/training_darknet_3_feb/Testset_detection/"+str(nr).zfill(2)+".txt"

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--groundpath', action='store',
                        default=pathg,
                        dest='groundpath', help='Path to ground truth text file')
    parser.add_argument('-p', '--predpath', action='store',
                        default=pathp,
                        dest='predpath', help='Path to prediction text file')

    args = parser.parse_args()
    groundpath = args.groundpath
    predpath = args.predpath

    Detection = namedtuple("Detection", ["image_path", "gt", "pred"])
    photopath = "/home/sverrir/Documents/Yolo_data/Testset/"+str(nr).zfill(2)+".png"

    with open(groundpath) as textFile:
        groundtxt = [line.split() for line in textFile]

    with open(predpath) as textFile:
        prediicttxt = [line.split() for line in textFile]

    tmp = []
    temp = 0
    for i in groundtxt:
        d = 0
        for j in prediicttxt:
            d_tmp = distance.euclidean((int(wp * float(i[1])), int(hp * float(i[2]))),
                                    (int(wp * float(j[1])), int(hp * float(j[2]))))
            if d_tmp < d:
                temp = 0
        tmp.append(j)
    #print(tmp)
    #print(groundtxt)

    nr_bbox = len(groundtxt)

    #print(groundtxt, prediicttxt)

    #max_length = max(len(groundtxt), len(prediicttxt))
    #groundtxt += ['0' '0' '0' '0' '0'] * (max_length - len(groundtxt))
    #prediicttxt += ['0' '0' '0' '0' '0'] * (max_length - len(prediicttxt))
    d = 1000
    d_best=[]

    image = cv2.imread(photopath)
    examples = []
    for i, j in zip(groundtxt, prediicttxt):
        gt = [float(i[1]), float(i[2]), float(i[3]), float(i[4])]
        pred = [float(j[1]), float(j[2]), float(j[3]), float(j[4])]

        xgt = int((wp * gt[0]) - ((wp * gt[2]) / 2))
        ygt = int(hp * gt[1] - ((hp * gt[3]) / 2))
        wgt = int(((wp * gt[0]) - ((wp * gt[2]) / 2)) + wp * gt[2])
        hgt = int((hp * gt[1] - ((hp * gt[3]) / 2)) + hp * gt[3])

        xpr = int((wp * pred[0]) - ((wp * pred[2]) / 2))
        ypr = int(hp * pred[1] - ((hp * pred[3]) / 2))
        wpr = int(((wp * pred[0]) - ((wp * pred[2]) / 2)) + wp * pred[2])
        hpr = int((hp * pred[1] - ((hp * pred[3]) / 2)) + hp * pred[3])

        example = Detection(photopath, [xgt, ygt, wgt, hgt], [xpr, ypr, wpr, hpr])
        examples.append(example)

        cv2.circle(image, (int(wp * gt[0]),
                        int(hp * gt[1])), 2, (255, 0, 0), 2)
        #print(int(wp * gt[0]), int(hp * gt[1]))
        cv2.circle(image, (int(wp * pred[0]),
                        int(hp * pred[1])), 2, (0, 0, 255), 2)

        d_tmp = distance.euclidean((int(wp * gt[0]), int(hp * gt[1])),
                                (int(wp * pred[0]), int(hp * pred[1])))

        #d = d + d_tmp
        #print(d_tmp)
        if d_tmp < d:
            d = d_tmp
            d_best = [(int(wp * gt[0]), int(hp * gt[1])), (int(wp * pred[0]), int(hp * pred[1]))]

    #print(examples)


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
        # [int(1280 * 0.616144), int(720 * 0.537147),int(0.091191),int(0.453694)])]
    # loop over the example detections


    iou = 0


    for detection in examples:
        # load the image
        #print(tuple(detection.pred[:])[1])
        # draw the ground-truth bounding box along with the predicted
        # bounding box
        cv2.rectangle(image, tuple(detection.gt[:2]),
                    tuple(detection.gt[2:]), (255, 0, 0), 2)
        cv2.rectangle(image, tuple(detection.pred[:2]),
                    tuple(detection.pred[2:]), (0, 0, 255), 2)
        # compute the intersection over union and display it
        iou_tmp = bb_intersection_over_union(detection.gt, detection.pred)
        #d_tmp = distance.euclidean((int(wp * gt[0]), int(hp * gt[1])),
        #                           (int(wp * pred[0]), int(hp * pred[1])))

        iou = iou + iou_tmp
        #d = d + d_tmp
        #print(d_tmp/nr_bbox)
        #if d_tmp < d:
        #    print(d)
        #    d = d_tmp
        #    d_best = [(int(wp * gt[0]), int(hp * gt[1])), (int(wp * pred[0]), int(hp * pred[1]))]

    #print(d_best)
    cv2.circle(image, d_best[1], 2, (0, 255, 0), 2)
    iou = iou / nr_bbox

    cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    #print("{}: {:.4f}".format(detection.image_path, iou))

    cv2.putText(image, "Distance: {:.4f}".format(d), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)
    #print("{}: {:.4f}".format(detection.image_path, d))

    # show the output image
    #cv2.imshow("Image", image)
    cv2.imwrite("/home/sverrir/Documents/Yolo_data/IOU"+str(nr)+".png", image)
    # cv2.waitKey(0)
