from normal_text_node import NORMALTextNode
from parent_node import ParentNode
from commen_helpers import trim_left_first

class QuoteBlockNode(ParentNode):
    def __init__(self, block):
        def trim_quote(line):
            return trim_left_first('>', line)[1].strip()

        text = ''.join(map(trim_quote, block.splitlines()))

        super().__init__('blockquote', NORMALTextNode.text_to_html_nodes(text))