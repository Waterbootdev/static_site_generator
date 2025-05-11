from os import path, listdir, mkdir
from shutil import copy, rmtree
from commen_helpers import apply_pair
from enum import Enum

class FileMode(Enum):
    CREATE="x"
    APPEND="a"
    WRITE="w"





def copy_static_to_public():

    def remove_dest_dir(p='public'):
        if path.exists(p):
            rmtree(p)
        mkdir(p)

    def copy_to_dest(source='static', dest='public'):
        def paths(name):
            return path.join(source, name), path.join(dest, name)
    
        @apply_pair
        def copy_paths(source, dest):
            if path.isfile(source):
                copy(source, dest)
            else:
                mkdir(dest)
                copy_to_dest(source, dest)
    
        list(map(copy_paths, map(paths, listdir(source))))  

    remove_dest_dir()
    copy_to_dest()

def read_file(file_path):
    if path.exists(file_path) and path.isfile(file_path):
        return read_existing_file(file_path)
    else:
        return None

def read_existing_file(file_path):
    file = open(file_path)
    content = file.read()
    file.close()
    return content

def write_file(file_path, content, mode=FileMode.CREATE):
    if isinstance(mode, FileMode):        
        
        mkdirectory(path.dirname(file_path))
        
        file = open(file_path, mode.value)
        file.write(content)
        file.close()

    else:
        ValueError(f"{mode} is not a FileMode") 

def mkdirectory(dir_path):
    if len(dir_path) > 0:
        dir = path.dirname(dir_path)
        mkdirectory(dir)
        if not path.exists(dir_path):
            mkdir(dir_path)


