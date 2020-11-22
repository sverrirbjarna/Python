from collections import namedtuple
import cv2
from scipy.spatial import distance
import argparse
import os

hp = 720
wp = 1280

source = "/home/sverrir/Documents/Yolo_data/ultratestbox/ground/"

if os.path.exists(source + "Detect_info.txt"):
    os.remove(source + "Detect_info.txt")
    print("File deleted")
else:
    print("The file does not exist")

if os.path.exists(source + "toExcel.csv"):
    os.remove(source + "toExcel.csv")
    print("File deleted")
else:
    print("The file does not exist")

for nr in range(0, 1):
    print(str(nr).zfill(4))
    pathg = "/home/sverrir/Documents/Yolo_data/ultratestbox/" + str(nr).zfill(4) + ".txt"

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--groundpath', action='store',
                        default=pathg,
                        dest='groundpath', help='Path to ground truth text file')

    args = parser.parse_args()
    groundpath = args.groundpath

    Detection = namedtuple("Detection", ["image_path", "gt"])
    photopath = "/home/sverrir/Documents/Yolo_data/ultratestbox/" + str(nr).zfill(4) + ".png"

    with open(groundpath) as textFile:
        groundtxt = [line.split() for line in textFile]

    # print(tmp)
    #print(groundtxt)

    nr_ground = len(groundtxt)
    #print("box: " + str(nr_ground))
    # print(nr_bbox)

    image = cv2.imread(photopath)
    examples = []

    for i in groundtxt:
        gt = [int(i[0]), int(i[1]), int(i[2]), int(i[3])]
        print(gt)
        xgt = int((wp * gt[0]) - ((wp * gt[2]) / 2))
        ygt = int(hp * gt[1] - ((hp * gt[3]) / 2))
        wgt = int(((wp * gt[0]) - ((wp * gt[2]) / 2)) + wp * gt[2])
        hgt = int((hp * gt[1] - ((hp * gt[3]) / 2)) + hp * gt[3])


        example = Detection(photopath, [int(i[0]), int(i[1]), int(i[2]), int(i[3])])
        examples.append(example)

        cv2.circle(image, (int(wp * gt[0]),
                       int(hp * gt[1])), 2, (255, 0, 0), 2)

        #print(examples)


        for detection in examples:
            # load the image
            #print(tuple(detection.gt[:2])[1])
            # draw the ground-truth bounding box along with the predicted
            # bounding box
            cv2.rectangle(image, tuple(detection.gt[:2]),
                        tuple(detection.gt[2:]), (255, 0, 0), 2)

            cv2.imshow("Image", image)
            cv2.imwrite(source + "IOU" + str(nr) + ".png", image)
exit()