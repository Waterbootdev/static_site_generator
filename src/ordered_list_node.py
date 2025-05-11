from parent_node import ParentNode
from list_item_node import ListItemNode

class OrderedListNode(ParentNode):
    def __init__(self, block):
        super().__init__("ol", ListItemNode.list_item_nodes(block))