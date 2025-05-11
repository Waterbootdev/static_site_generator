from leaf_node import LeafNode
from commen_helpers import trim_left_first

class ListItemNode(LeafNode):
    def __init__(self, line):
        super().__init__('li', trim_left_first(' ', line)[1])

    @staticmethod

    def list_item_nodes(block):
        map(ListItemNode, block.splitlines())