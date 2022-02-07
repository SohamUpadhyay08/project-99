import os
import shutil
import time

def remove_folder(path) : 
    if not shutil.rmtree(path) :
        print("folder removed sucessfully")
    else :
        print("unable to delete the folder")
    
def remove_file(path) :
    if not os.remove(path) :
        print("file removed sucessfully")
    else :
        print("unable to delete the file")

def get_file_or_folder_age(path) : 
    ctime = os.stat(path).st_ctime
    return ctime

path = "./Backups/"
days = 30
seconds = time.time() - (days*24*60*60)
deleted_folder_count = 0
deleted_file_count = 0
if os.path.exists(path) : 
    for root_folder,folders,files in os.walk(path) : 
        if seconds >= get_file_or_folder_age(root_folder) :
            remove_folder(root_folder)
            deleted_folder_count+=1
            break
        else :
            for folder in folders :
                folder_path = os.path.join(root_folder,folder)
                if seconds >= get_file_or_folder_age(folder_path) :
                    remove_folder(folder_path)
                    deleted_folder_count+=1
            for file in files :
                file_path = os.path.join(root_folder,file)
                if seconds >= get_file_or_folder_age(file_path):
                    remove_file(file_path)
                    deleted_file_count+=1
        
else :
    print("no path exists")
    deleted_file_count +=1
    

