from parent_node import ParentNode
from list_item_node import ListItemNode

class ListParantNode(ParentNode):
    def __init__(self, tag, list_block, props=None):
        super().__init__(tag, ListItemNode.list_item_nodes(list_block), props)