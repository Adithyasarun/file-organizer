import os
import shutil
from_dir = "C:/Users/PC/Downloads" 
to_dir = "C:/Users/PC/Downloads/imgdow"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext == "":
        continue
    if(ext in ['.png','.jpg',".jpeg",".gif",".webp"]):
        path1 = from_dir +'/'+file_name
        path2 = to_dir +'/'+"images_files"
        path3 = to_dir +'/'+"images_files"+"/"+file_name
        if(os.path.exists(path2)):
            print("moving"+"/"+file_name+"...")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving"+"/"+file_name+"...")
            shutil.move(path1,path3)
