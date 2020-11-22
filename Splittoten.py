import os
import random
import shutil

for i in range (1 , 16):
    current_dir = "/home/sverrir/Documents/Yolo_data/Biersdorf_split/split_to_ten/" + str(i) + "/"

    for j in range (1 , 11):
        new_dir = "/home/sverrir/Documents/Yolo_data/Biersdorf_split/split_to_ten/Split/"+ str(i) + "/" + str(j) + "/"
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        file_train = open(new_dir + 'train.txt', 'w')
        file_test = open(new_dir + 'test.txt', 'w')

        if j <=5 :
            for k in range(1, 16):
                file = random.choice(os.listdir(current_dir)) #change dir name to whatever
                print(file[0:-4])

                shutil.move(current_dir + file[0:-4] + ".txt", new_dir + file[0:-4] + ".txt")
                shutil.move(current_dir + file[0:-4] + ".png", new_dir + file[0:-4] + ".png")
                file_test.write(new_dir + file[0:-4] + ".png" + "\n")
        else:
            for d in range(1, 15):
                file = random.choice(os.listdir(current_dir))  # change dir name to whatever
                print(file[0:-4])

                shutil.move(current_dir + file[0:-4] + ".txt", new_dir + file[0:-4] + ".txt")
                shutil.move(current_dir + file[0:-4] + ".png", new_dir + file[0:-4] + ".png")
                file_test.write(new_dir + file[0:-4] + ".png" + "\n")

exit(0)