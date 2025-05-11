from list_parent_node import ListParantNode

class UnorderedListNode(ListParantNode):
    def __init__(self, block):
        super().__init__("ul", block)