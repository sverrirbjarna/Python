from collections import namedtuple
import cv2
from scipy.spatial import distance
import argparse
import os


hp = 720
wp = 1280

path = "last_Biersdorf12_10_12_7_8_13_yolov3"

photo_directory = "/home/sverrir/Documents/Yolo_data/Biersdorf97-48/48Testset/"
ground_directory = "/home/sverrir/Documents/Yolo_data/Biersdorf97-48/48Testset/"
predict_directory = "/home/sverrir/Documents/Yolo_data/Biersdorf97-48/"+ path+ "/"
source = "/home/sverrir/Documents/Yolo_data/Biersdorf97-48/"+ path+ "_IOU/"

if os.path.exists(source+"Detect_info.txt"):
  os.remove(source+"Detect_info.txt")
  print("File deleted")
else:
  print("The file does not exist")

if os.path.exists(source+"toExcel.csv"):
  os.remove(source+"toExcel.csv")
  print("File deleted")
else:
  print("The file does not exist")

file2 = open(source +"toExcel.csv", "a")  # append mode
file2.write(
        "Image nr" + "," + "Filename" + "," + "Bottles" + "," + "Detections" + "," + "True positive" + "," + "False positive" +
        "," + "IOU" + "," + "Min distance" + "," + "Max distance" + "," + "Average distance" + "\n")
file2.close()

gt_list = []
pred_list = []

for filename in os.listdir(ground_directory):
    if filename.endswith(".txt"):
        gt_list.append(filename)
        gt_list.sort()
        continue
    else:
        continue

#for filename in os.listdir(predict_directory):
#    if filename.endswith(".txt"):
#        pred_list.append(filename)
#        continue
#    else:
#        continue


for nr in range(0, len(gt_list)):

    pathg = ground_directory + gt_list[nr]
    pathp = predict_directory + pathg[-8:-4] + ".png.txt"
    photopath = photo_directory + pathg[-8:-4] +".png"
    #print("pathg: " + pathg)
    #print("pathp: " + pathp)
    if os.path.exists(pathp):
        print(str(nr).zfill(4))
        print(gt_list[nr])
    else:
        print("No Detection")

        parser = argparse.ArgumentParser()
        parser.add_argument('-g', '--groundpath', action='store',
                            default=pathg,
                            dest='groundpath', help='Path to ground truth text file')

        args = parser.parse_args()
        groundpath = args.groundpath

        with open(groundpath) as textFile:
            groundtxt = [line.split() for line in textFile]

        nr_ground = len(groundtxt)

        file1 = open(source + "Detect_info.txt", "a")  # append mode
        file2 = open(source + "toExcel.csv", "a")  # append mode
        file1.write(str(nr+1) + "\n")
        file1.write("File name: " + pathg[-8:-4] + "\n")
        file1.write("IoU: " + str(0) + "\n")
        file1.write("Min Distance: " + str(0) + "\n")
        file1.write("Max Distance: " + str(0) + "\n")
        file1.write("Average Distance: " + str(0) + "\n")
        file1.write("Nr of bottles: " + str(0) + "\n")
        file1.write("Nr of detections: " + str(0) + "\n")
        file1.write("True positive: " + str(0) + "\n")
        file1.write("False positive: " + str(0) + "\n")
        file1.write("\n")
        file1.close()
        file2.write(str(nr+1) + "," + str(pathg[-8:-4]) + "," + str(nr_ground) + "," + str(0) + "," + str(
            0) + "," + str(0) + "," + str(0) + "," + str(0) + "," + str(0) +
            "," + str(0) + "\n")
        file1.close()
        file2.close()

        #print(gt_list[nr])
        continue



    #pathp = source+str(nr).zfill(4)+".txt"
    file1 = open(source+"Detect_info.txt","a")#append mode
    file2 = open(source +"toExcel.csv", "a")  # append mode

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

    with open(groundpath) as textFile:
        groundtxt = [line.split() for line in textFile]

    with open(predpath) as textFile:
        prediicttxt = [line.split() for line in textFile]


    #print(tmp)
    #print(groundtxt)

    nr_ground = len(groundtxt)
    nr_bbox = len(prediicttxt)
    false_positive = len(prediicttxt) - len(groundtxt)
    if false_positive < 0:
        false_positive = 0

    true_positive = len(prediicttxt) - false_positive
    print("box: "+str(nr_ground))
    print("detections: "+str(nr_bbox))
    print("false detections: " + str(false_positive))
    true_pos = 0
    false_pos = 0
    d = 1000
    d_max = 0
    d_average = 0
    d_best=[]
    d_maxp=[]

    image = cv2.imread(photopath)
    examples = []
    for j in prediicttxt:
        pred = [int(j[0]), int(j[1]), int(j[2]), int(j[3])]
        gt = [0, 0, 0, 0]
        dist = 10000
        for i in groundtxt:
            tmp_gt = [float(i[1]), float(i[2]), float(i[3]), float(i[4])]
            dist_tmp = distance.euclidean((int(wp * tmp_gt[0]), int(hp * tmp_gt[1])),
                                (int(pred[0]+((pred[2]-pred[0])/2)), int(pred[1]+((pred[3]-pred[1])/2))))
            if dist > dist_tmp:
                gt = tmp_gt
                dist = dist_tmp


        xgt = int((wp * gt[0]) - ((wp * gt[2]) / 2))
        ygt = int(hp * gt[1] - ((hp * gt[3]) / 2))
        wgt = int(((wp * gt[0]) - ((wp * gt[2]) / 2)) + wp * gt[2])
        hgt = int((hp * gt[1] - ((hp * gt[3]) / 2)) + hp * gt[3])

        xpr = int((wp * pred[0]) - ((wp * pred[2]) / 2))
        ypr = int(hp * pred[1] - ((hp * pred[3]) / 2))
        wpr = int(((wp * pred[0]) - ((wp * pred[2]) / 2)) + wp * pred[2])
        hpr = int((hp * pred[1] - ((hp * pred[3]) / 2)) + hp * pred[3])

        example = Detection(photopath, [xgt, ygt, wgt, hgt], [int(pred[0]), int(pred[1]), int(pred[2]), int(pred[3])])
        examples.append(example)

        cv2.circle(image, (int(wp * gt[0]),
                        int(hp * gt[1])), 2, (255, 0, 0), 2)
        #print(int(wp * gt[0]), int(hp * gt[1]),wgt,hgt)
        cv2.circle(image, (int(pred[0]+((pred[2]-pred[0])/2)),
                        int(pred[1]+((pred[3]-pred[1])/2))), 2, (0, 0, 255), 2)
        #print(int(pred[0]), int(pred[1]),int(pred[2]),int(pred[3]))

        d_tmp = distance.euclidean((int(wp * gt[0]), int(hp * gt[1])),
                                (int(pred[0]+((pred[2]-pred[0])/2)), int(pred[1]+((pred[3]-pred[1])/2))))

        d_average = d_average + d_tmp
        #print(d_tmp)
        if d_tmp < d:
            d = d_tmp
            d_best = [(int(wp * gt[0]), int(hp * gt[1])), (int(pred[0]+((pred[2]-pred[0])/2)), int(pred[1]+((pred[3]-pred[1])/2)))]

        if d_tmp > d_max:
            d_max = d_tmp
            d_maxp = [(int(wp * gt[0]), int(hp * gt[1])), (int(pred[0]+((pred[2]-pred[0])/2)), int(pred[1]+((pred[3]-pred[1])/2)))]

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
        # compute the intersection over union and display it
        iou_tmp = bb_intersection_over_union(detection.gt, detection.pred)
        # d_tmp = distance.euclidean((int(wp * gt[0]), int(hp * gt[1])),
        #                           (int(wp * pred[0]), int(hp * pred[1])))
        #print(detection.gt)
        #print(detection.pred)
        #print(iou_tmp)
        iou = iou + iou_tmp
        # draw the ground-truth bounding box along with the predicted
        # bounding box
        if iou_tmp >= 0.5:
            cv2.rectangle(image, tuple(detection.gt[:2]),
                          tuple(detection.gt[2:]), (255, 0,0), 2)
            cv2.rectangle(image, tuple(detection.pred[:2]),
                          tuple(detection.pred[2:]), (0, 255, 0), 2)
        else:
            #print(iou_tmp)
            cv2.rectangle(image, tuple(detection.gt[:2]),
                          tuple(detection.gt[2:]), (255, 0, 0), 2)
            cv2.rectangle(image, tuple(detection.pred[:2]),
                          tuple(detection.pred[2:]), (0, 0, 255), 2)


        if iou_tmp < 0.5:
            #false_positive = false_positive + 1
            #true_positive = true_positive - 1
            false_pos = false_pos + 1
        else:
            true_pos = true_pos + 1
        #d = d + d_tmp
        #print(d_tmp/nr_bbox)
        #if d_tmp < d:
        #    print(d)
        #    d = d_tmp
        #    d_best = [(int(wp * gt[0]), int(hp * gt[1])), (int(wp * pred[0]), int(hp * pred[1]))]

    #print(len(d_best))

    if len(d_best)>0:
        cv2.circle(image, d_best[1], 2, (255, 255, 0), 6)

    if nr_bbox == 0:
        nr_bbox = 1
    #print(nr_bbox)
    iou = iou / nr_bbox
    d_average = d_average / nr_bbox

    file1.write(str(nr+1)+"\n")
    file1.write("File name: " + pathg[-8:-4] + "\n")
    file1.write("IoU: "+str(iou)+"\n")
    file1.write("Min Distance: "+str(d)+"\n")
    file1.write("Max Distance: "+str(d_max)+"\n")
    file1.write("Average Distance: "+str(d_average)+"\n")
    file1.write("Nr of bottles: " + str(nr_ground) + "\n")
    file1.write("Nr of detections: "+str(nr_bbox)+"\n")
    file1.write("True positive: " + str(true_pos) + "\n")
    file1.write("False positive: " + str(false_pos) + "\n")
    file1.write("\n")
    file1.close()
    file2.write(str(nr+1) + "," + str(pathg[-8:-4]) + "," + str(nr_ground) + "," + str(nr_bbox) + "," + str(true_pos) + "," + str(false_pos) +
                "," + str(iou) + "," + str(d) + "," + str(d_max) + "," + str(d_average) + "\n")
    file1.close()
    file2.close()

    cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    #print("{}: {:.4f}".format(detection.image_path, iou))

    cv2.putText(image, "Min Distance: {:.4f}".format(d), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)
    #print("{}: {:.4f}".format(detection.image_path, d))

    cv2.putText(image, "Max Distance: {:.4f}".format(d_max), (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)
    #print("{}: {:.4f}".format(detection.image_path, d))

    cv2.putText(image, "Average Distance: {:.4f}".format(d_average), (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)
    #print("{}: {:.4f}".format(detection.image_path, d))

    cv2.putText(image, "True positive: {:.4f}".format(true_pos), (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)

    cv2.putText(image, "False positive: {:.4f}".format(false_pos), (10, 130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 50), 2)
    # show the output image
    #cv2.imshow("Image", image)
    cv2.imwrite(source+"IOU"+pathg[-8:-4]+".png", image)
    #cv2.waitKey(0)
exit()