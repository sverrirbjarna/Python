import shutil
import os

my_file = open("/home/sverrir/Documents/Yolo_data/Biersdorf_split/Joined/Biersdorf_all/test10p.txt", "r")
content_list = my_file.read().splitlines()

print(content_list)

for f in content_list:
    shutil.copy(f, '/home/sverrir/Documents/Yolo_data/Biersdorf_split/Joined/test10pall')