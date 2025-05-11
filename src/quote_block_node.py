from none_list_parent_node import NoneListParentNode
from commen_helpers import trim_left_first

class QuoteBlockNode(NoneListParentNode):
    def __init__(self, block):
        def trim_quote(line):
            return trim_left_first('>', line)[1].strip()

        text = ''.join(map(trim_quote, block.splitlines()))

        super().__init__('blockquote', text)