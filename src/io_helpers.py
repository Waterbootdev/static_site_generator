from os import path, listdir, mkdir
from shutil import copy, rmtree
from commen_helpers import apply_pair
from enum import Enum

class FileMode(Enum):
    CREATE="x"
    APPEND="a"
    WRITE="w"

def copy_static_to_public(public='public'):

    def remove_dest_dir(public):
        if path.exists(public):
            rmtree(public)
        mkdir(public)

    def copy_to_dest(source='static', dest='public'):
        def paths(name):
            return path.join(source, name), path.join(dest, name)
    
        @apply_pair
        def copy_paths(source, dest):
            if path.isfile(source):
                print(dest)
                copy(source, dest)
            else:
                mkdir(dest)
                copy_to_dest(source, dest)
    
        list(map(copy_paths, map(paths, listdir(source))))  

    remove_dest_dir(public)
    copy_to_dest(dest=public)

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


def get_files(dir_path, ext):

        path.splitext        
        file_paths, dir_paths = list_dir_group(dir_path, ext)

        def extend_(current):
            file_paths.extend(current)

        list(map(extend_, map(lambda next: get_files(next, ext), dir_paths)))

        return file_paths      
      
def list_dir_group(dir_path, ext):
    paths =[path.join(dir_path, p) for p in  listdir(dir_path)]
    return [p for p in paths if path.isfile(p) and path.splitext(p)[1]==ext], [p for p in paths if path.isdir(p)]

def change_path_root(file_path, current_root, root):
    splitted = file_path.split(current_root, maxsplit=1)
    new_path = f"{root}{splitted[1]}"
    return new_path

def change_file_ext(file_path, ext):
    splitted = path.splitext(file_path)
    return f"{splitted[0]}{ext}"



def get_basepath(args):
    return f"{path.dirname(path.dirname(args[0]))}/" if isinstance(args, list) and len(args) > 0 else '/'

    












