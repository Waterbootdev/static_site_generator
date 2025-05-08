from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):    
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return self.add_html_begin_and_end_tag(self.value)
