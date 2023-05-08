import os 
import shutil

from_dir = "/home/kevin/Downloads"
to_dir = "/home/kevin/cool"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,ext = os.path.splitext(files)
    print(name)
    print(ext)
