import glob
import os

current_dir = "/home/sverrir/Documents/Yolo_data/Biersdorf_split/split_to_ten/Split/15/10/"# PATH TO IMAGE DIRECTORY
# Percentage of images to be used for the valid set
percentage_test = 100
# Create train.txt and valid.txt
file_train = open(current_dir +'train.txt', 'w')
file_test = open(current_dir +'test.txt', 'w')
# Populate train.txt and valid.txt
counter = 1
index_test = round(100 / percentage_test)
print(index_test)
print(current_dir + '*.png')
for file in glob.iglob(os.path.join(current_dir, '*.png')):
    print(file)
    if counter == index_test:
        counter = 1
        file_test.write(file + "\n")
    else:
        file_train.write(file + "\n")
        counter = counter + 1
file_train.close()
file_test.close()