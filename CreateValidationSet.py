import os
import shutil
import random

root_dir = '/run/media/chinmay/DATA/Chinmay/Chinmay/Passions/DeepLearning/Projects/DevanagariChars/DevanagariHandwrittenCharacterDataset/train/'
out_dir = '/run/media/chinmay/DATA/Chinmay/Chinmay/Passions/DeepLearning/Projects/DevanagariChars/DevanagariHandwrittenCharacterDataset/valid/'
ref = 1

for root, dirs, files in os.walk(root_dir):
    if len(dirs) == 0:
        break
    else:
        for i in range(len(dirs)):
            fromdir = root_dir+dirs[i]
            todir = out_dir+dirs[i]
            print(fromdir)
            for j in range(290):     
                randfile = os.listdir(fromdir)
                file = random.choice(randfile)
                fromfile = fromdir + '/' + file
                tofile = todir + '/' + file
                if os.path.isfile(fromfile) == True:
                    #shutil.move(fromfile,tofile) Chukun run kela tar vaat lagte mhanun
                    print(fromfile)
                    print(tofile)

print("Done")