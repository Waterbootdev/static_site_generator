from normal_text_node import NORMALTextNode
from parent_node import ParentNode
from commen_helpers import trim_left_first

class ListItemNode(ParentNode):
    def __init__(self, line):

        super().__init__('li', NORMALTextNode.text_to_html_nodes(trim_left_first(' ', line)[1]))

    @staticmethod
    def list_item_nodes(block):
        return list(map(ListItemNode, block.splitlines()))