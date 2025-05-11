from parent_node import ParentNode
from block_nodes import blocks_to_html_nodes
from extract_markdown import markdown_to_blocks


class DivNode(ParentNode):
    def __init__(self, markdown):
        super().__init__('div', blocks_to_html_nodes(markdown_to_blocks(markdown)))



     





