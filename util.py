import os
import shutil
import time
import platform

home = "c:\\test"

def prepare_destination(name):
    directory = os.path.join(home, name)
    if not os.path.exists(directory):
        os.makedirs(directory) 
        return directory
    
def transfer(files):
  for aFile, createdDate in files: 
    des = prepare_destination(createdDate)
    shutil.move(aFile, des)
    
def get_file_create_date(src):
    return time.strftime('%m/%d/%Y', _get_file_created_date_long(src))

def _get_file_created_date_long(src):
    if platform.system() == 'Windows':
        return os.path.getctime(src)
    else:
      stat = os.stat(src)
    try:
        return stat.st_birthtime 
    except AttributeError: 
        return stat.st_mtime
        
def scan_cr2(base):
    for root, dirs, files in os.walk(base):
        for file in files:
            if file.upper().endswith(".CR2"):
                yield os.path.join(root, file), get_file_create_date(file)
                
def test():
  transfer(scan_cr2("c:\\tmp"))
