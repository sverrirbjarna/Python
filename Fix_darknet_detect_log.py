import os
import glob


lo = []
path = "/home/sverrir/Documents/Yolo_data/Training_5feb_yolo3cfg_rgbdata/Testset_detection/"
num = 1
for filename in glob.glob(os.path.join(path, '*.log')):
    file = open(path+filename[-6:-4]+".txt", "w") #les stafi -6 til -4 í nafninu til að fá 01 - 30
    #print(filename)
    #print(filename[-7:-4])
    with open(filename) as f:
        for line in f.read().split("\n")[1::1]: #Sleppi fyrstu línu og les hverja línu eftir það
            lo.append(line)
            if len(line) == 35: # ef línan er 35 á leng þá er hún á réttu formi : 0.520663 0.378275 0.373944 0.930884
                file.write(str(0)+" "+str(line)+"\n") # Bæti 0 fyrir framan til þess að það sé í classa 1 þarf að endurskoða ef það koma fleiri
                #print(num)
                #print(line)
    num = num + 1
    file.close()
