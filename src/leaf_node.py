from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):    
        super().__init__(tag=tag, value=value, props=props)

    def to_html_end_tag(self):
        return "" if self.tag is None else f"</{self.tag}>"
    
    def to_html_begin_tag(self):
        return "" if self.tag is None else f"<{self.tag}{self.props_to_html()}>"

    @staticmethod 
    def taged_value(tag, value):
        return f"{value}" if tag is None else f"<{tag}>{value}</{tag}>" 

    def to_html(self):
        return f"{self.to_html_begin_tag()}{self.value}{self.to_html_end_tag()}"
