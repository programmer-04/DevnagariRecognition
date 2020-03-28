import os
import shutil
import random
from Config import root_dir, out_dir
copycount = 290

for root, dirs, files in os.walk(root_dir):
    if len(dirs) == 0:
        break
    else:
        for i in range(len(dirs)):
            fromdir = root_dir+dirs[i]
            todir = out_dir+dirs[i]
            print(fromdir)
            for j in range(copycount):     
                randfile = os.listdir(fromdir)
                file = random.choice(randfile)
                fromfile = fromdir + '/' + file
                tofile = todir + '/' + file
                if os.path.isfile(fromfile) == True:
                    #shutil.move(fromfile,tofile) Chukun run kela tar vaat lagte mhanun
                    print(fromfile)
                    print(tofile)

print("Done")