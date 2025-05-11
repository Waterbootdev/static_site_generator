from none_list_parent_node import NoneListParentNode
from commen_helpers import trim_left_first

class ListItemNode(NoneListParentNode):
    def __init__(self, line):
        super().__init__('li', trim_left_first(' ', line)[1])

    