from io_helpers import copy_static_to_public, get_basepath
from template_type import generate_pages_recursive
import sys



def main():    
    public = 'docs'
    basepath = get_basepath(sys.argv)
    print(f"basepath = {basepath}")
    copy_static_to_public(public=public)
    generate_pages_recursive("content", "template.html", public, 'https://Waterbootdev.github.io/static_site_generator/')

main()

    

