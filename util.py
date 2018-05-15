import os
import shutil
import datetime
import platform

home = "C:\\Users\\Arun Soman\\Pictue"\


def prepare_destination(name):
    directory = os.path.join(home, name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def transfer_and_del(files):
    for aFile, createdDate in files:
        des = prepare_destination(createdDate)
        shutil.move(aFile, des)
#        os.remove(aFile)

def _get_file_created_date_long(src):
    if platform.system() == 'Windows':
        return os.path.getctime(src)
    else:
        stat = os.stat(src)
    try:
        return stat.st_birthtime
    except AttributeError:
        return stat.st_mtime


def get_file_create_date(src):
    return datetime.datetime.fromtimestamp(_get_file_created_date_long(src)).strftime('%d-%m-%y')


def scan_cr2(base):
    for root, dirs, files in os.walk(base):
        print(root)
        for file in files:
            if file.upper().endswith(".CR2"):
                uri= os.path.join(root, file)
                yield uri,get_file_create_date(uri)
        for dir in dirs:
            scan_cr2(dir)


def test():
    transfer_and_del(scan_cr2("D:"))

test()
