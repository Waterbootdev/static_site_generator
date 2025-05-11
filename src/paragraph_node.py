from none_list_parent_node import NoneListParentNode

class ParagraphNode(NoneListParentNode):
    def __init__(self, block):
        super().__init__('p', ' '.join(block.splitlines()))






