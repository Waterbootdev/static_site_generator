from leaf_node import LeafNode
from commen_helpers import trim_left_first

class QuoteBlockNode(LeafNode):
    def __init__(self, block):
        def trim_quote(line):
            return trim_left_first('>', line)

        value = ''.join(map(lambda t: t[1], map(trim_quote, block.splitlines())))

        super().__init__('blockqoute', value)