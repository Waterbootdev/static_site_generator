from re import findall

    
def extract_markdown_images(text):
    return findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return findall(r"\s\[(.*?)\]\((.*?)\)",text)

#extracted from tips afterwarts 
def extract_markdown_images_tip(text):
    return findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links_tip(text):
    return findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
