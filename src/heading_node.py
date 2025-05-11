from leaf_node import LeafNode
from commen_helpers import trim_left_first

class HeadingNode(LeafNode):
    def __init__(self, block):
        number, value = trim_left_first(' ', block)
        super().__init__(f"h{number}", value.strip())
        self.heading_number = number

    def is_titel(self):
        return self.heading_number == 1