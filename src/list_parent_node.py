from parent_node import ParentNode
from list_item_node import ListItemNode

class ListParantNode(ParentNode):
    def __init__(self, tag, list_block, props=None):    
        super().__init__(tag, list(map(ListItemNode, list_block.splitlines())), props)