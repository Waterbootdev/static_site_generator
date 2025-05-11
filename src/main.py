from io_helpers import copy_static_to_public
from template_type import generate_pages_recursive



     


def main():
    copy_static_to_public()
    generate_pages_recursive("content","template.html","public")

main()

    

