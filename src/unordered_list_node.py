from list_parent_node import ListParentNode

class UnorderedListNode(ListParentNode):
    def __init__(self, block):
        super().__init__("ul", block)