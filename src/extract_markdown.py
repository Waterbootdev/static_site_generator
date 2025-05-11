from commen_helpers import apply_pair
from re import findall
from textnode import TextType

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




