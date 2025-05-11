from normal_text_node import NORMALTextNode
from parent_node import ParentNode
from textnode import TextNode

class ParagraphNode(ParentNode):
    def __init__(self, block):
        super().__init__('p', list(map(TextNode.text_node_to_html_node , NORMALTextNode.text_to_textnodes(' '.join(block.splitlines())))))






