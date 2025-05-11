from parent_node import ParentNode
from normal_text_node import NORMALTextNode

class NoneListParentNode(ParentNode):
    def __init__(self, tag, children_text, props=None):
        super().__init__(tag, NORMALTextNode.text_to_html_nodes(children_text), props)