from enum import Enum
from heading_node import HeadingNode
from div_node import markdown_to_html
from functools import reduce
from io_helpers import read_file, write_file, FileMode

class TemplateType(Enum):
    TITEL='{{ Title }}'
    CONTENT='{{ Content }}' 

def replace_template_type_value(template_type, template, value):
    splited = template.split(template_type.value)
    return f"{splited[0]}{value}{splited[1]}"

def extract(template_type, markdown):
    match template_type:
        case TemplateType.TITEL:
            return HeadingNode.extract_titel(markdown)
        case TemplateType.CONTENT:
            return markdown_to_html(markdown)
        case _:
            raise ValueError(f"{template_type} is not a TemplateType")

def replace_template_type(template_type, template, markdown):
    return replace_template_type_value(template_type, template, extract(template_type, markdown))
    
def replace_template_types(template, markdown, *template_types):
    return reduce(lambda current_template, template_type: replace_template_type(template_type, current_template, markdown) ,template_types,template)

def read_template(template_path):
    template = read_file(template_path)

    if not template:
        raise ValueError(f"{template_path} is not a template file")
    return template

def read_markdown(from_path):
    markdown = read_file(from_path)

    if not markdown:
        raise ValueError(f"{from_path} is not a markdown file")
    return markdown

def replace_template(from_path, template_path):
    
    markdown = read_markdown(from_path)

    template = read_template(template_path)
    
    return replace_template_types(template, markdown, TemplateType.TITEL, TemplateType.CONTENT)

def generate_page(from_path, template_path, dest_path):
    write_file(dest_path, replace_template(from_path, template_path), FileMode.CREATE)    
    
    

