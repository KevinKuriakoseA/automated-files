import os 
import shutil

from_dir = "/home/kevin/Downloads"
to_dir = "/home/kevin/cool"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,ext = os.path.splitext(files)
    
    if ext == "":
        continue
    if ext in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + files
        path2 = to_dir + '/' + 'documents'
        path3 = to_dir +'/' + 'documents' + '/' + files
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    


    #print(name)
    #print(ext)
