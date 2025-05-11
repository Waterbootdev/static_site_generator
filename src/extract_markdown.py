from commen_helpers import apply_pair
from re import findall
from textnode import TextType
from blocktype import BlockType, get_block_type
from heading_node import HeadingNode

def add_text_type_to_extract_markdown(text_type):

    def transform(text_type, extracted):
        def f(first, text, url):
            return f"{first}[{text}]({url})"
    
        @apply_pair
        def transform(text, url):
            match text_type:
                case TextType.IMAGES:
                    return f('!', text, url)
                case TextType.LINKS:
                    return f('', text, url)
                case _:
                    return ValueError(f"text_type has to be TextType.IMAGES or TextType.LINKS not{text_type}")
       
        return list(zip(extracted, map(transform, extracted)))

    def add_type(func):
        def add_type(text):
            return text_type, text, transform(text_type, func(text))
        return add_type
    return add_type

@add_text_type_to_extract_markdown(TextType.IMAGES)
def extract_markdown_images(text):
    return findall(r"!\[(.*?)\]\((.*?)\)", text)

@add_text_type_to_extract_markdown(TextType.LINKS)
def extract_markdown_links(text):
    return findall(r"\s\[(.*?)\]\((.*?)\)",text)

#extracted from tips afterwarts 
@add_text_type_to_extract_markdown(TextType.IMAGES)
def extract_markdown_images_tip(text):
    return findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

@add_text_type_to_extract_markdown(TextType.LINKS)
def extract_markdown_links_tip(text):
    return findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def markdown_to_blocks(markdown):
    return list(filter(lambda block: len(block) > 0, map(lambda block : block.strip() ,markdown.split('\n\n'))))

def select_block_type(markdown, block_type):
    blocks = [block for block in markdown_to_blocks(markdown) if get_block_type(block) == block_type]
    return blocks
def extract_titel_nodes(markdown,):
    return [node for node in map(HeadingNode, select_block_type(markdown, BlockType.HEADING)) if node.is_titel()]

def extract_titel(markdown):
    
    titel_nodes = extract_titel_nodes(markdown)
    length = len(titel_nodes)
    
    if length == 0:
        raise Exception("can't find titel")

    if length > 1:
        print("Warning more then one titel")
    
    return titel_nodes[0].value



   