from normal_text_node import NORMALTextNode
from parent_node import ParentNode

class ParagraphNode(ParentNode):
    def __init__(self, block):
        super().__init__('p', NORMALTextNode.text_to_html_nodes(' '.join(block.splitlines())))






