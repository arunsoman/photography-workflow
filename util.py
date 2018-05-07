import os
import platform
from datetime import datetime

home = '/'

def scan_cr2(base):
    for root, dirs, files in os.walk(base):
        for file in files:
            if file.upper().endswith(".CR2"):
                yield os.path.join(root, file)

def get_file_create_date(src):
    yield time.strftime('%m/%d/%Y', _get_file_created_date_long(src))

def _get_file_created_date_long(src):
    if platform.system() == 'Windows':
        yield os.path.getctime(path_to_file)
    else :
      stat = os.stat(path_to_file)
    try:
        yield stat.st_birthtime 
    except AttributeError: 
        yield stat.st_mtime

def prepare_destination(name):
    directory = os.path.join(home, name)
    if not os.path.exists(directory):
        os.makedirs(directory) 
        yield directory

def transfer(file):
    date = get_file_create_date(file) 
    des = prepare_destination(date)
    shutil.move(src, des)

def train():
    sd_loc = ''
    for a_cr2 in scan_cr2(src) transfer_file(a_cr2)
