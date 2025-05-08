from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        
        if tag is None:
            raise ValueError("the tag of a parent node has to be not None")
        
        super().__init__(tag=tag, children=children, props=props)

    def children_to_html(self):
        return "".join(map(lambda child: child.to_html() ,self.children))

    def to_html(self):
        return self.add_html_begin_and_end_tag(self.children_to_html())

        
        

