from io_helpers import copy_static_to_public
from template_type import generate_page



def main():
    copy_static_to_public()
    generate_page("content/index.md", "template.html", "public/test/test/index.html")
    generate_page("content/index.md", "template.html", "public/test/index.html")

main()

    

