import os
import glob


lo = []
path = "/home/sverrir/Documents/Yolo_data/run20jan/Detections/"
num = 205
for filename in glob.glob(os.path.join(path, '*.log')):
    file = open(path+str(num)+".txt", "w")
    print(filename[-5])
    with open(filename) as f:
        for line in f.read().split("\n")[5::5]:
            lo.append(line)
            file.write(str(0)+" "+str(line)+"\n")
    num = num + 1
    file.close()
