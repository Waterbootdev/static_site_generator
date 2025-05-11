from io_helpers import copy_static_to_public, get_basepath
from template_type import generate_pages_recursive
import sys

def main_public(public, basepath):
    copy_static_to_public(public=public)
    generate_pages_recursive("content", "template.html", public, basepath)

def main():    
   
    main_public('public', '/') #local
    main_public('docs', '/static_site_generator/') #github
   
main()

    

