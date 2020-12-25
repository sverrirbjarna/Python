import os
import random
import shutil

for i in range (1 , 16):
    current_dir = "/home/sverrir/Documents/Yolo_data/Biersdorf_split/97_48/97/" + str(i) + "/"


    new_dir = "/home/sverrir/Documents/Yolo_data/Biersdorf_split/97_48/97/train/"+ str(i) + "/"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    file_train = open(new_dir + 'train_97' + str(i) + '.txt', 'w')


    for k in range(1, 98):
        file = random.choice(os.listdir(current_dir)) #change dir name to whatever
        print(file[0:-4])

        shutil.move(current_dir + file[0:-4] + ".txt", new_dir + file[0:-4] + ".txt")
        shutil.move(current_dir + file[0:-4] + ".png", new_dir + file[0:-4] + ".png")
        file_train.write(new_dir + file[0:-4] + ".png" + "\n")


exit(0)