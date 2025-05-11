from os import path, listdir, mkdir
from shutil import copy, rmtree
from commen_helpers import apply_pair

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