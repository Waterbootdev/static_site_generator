class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        
        if(value is None and children is None):
            HTMLNode.raise_exception("value or children has to be not none")

        if children is not None and (type(children) is not list or len(children) == 0):
            HTMLNode.raise_exception("children has to be a None or a list of at least one child")

        
        self.value = value # string
        self.children = children # list of HTMLNode's
        self.tag = tag # string
        self.props = {} if props is None else  props if type(props) is dict else HTMLNode.raise_exception("props has to be a dict or None") 
        # dict key-value pairs representing attributes

    
    @staticmethod
    def raise_exception(message):
        raise ValueError(message)

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return ''.join([f" {key}={value}" for key, value in self.props.items()])

    def __repr__(self):
        print(self)

    def to_html_end_tag(self):
        return "" if self.tag is None else f"</{self.tag}>"
    
    def to_html_begin_tag(self):
        return "" if self.tag is None else f"<{self.tag}{self.props_to_html()}>"
    
    def add_html_begin_and_end_tag(self, tag_value):
        return f"{self.to_html_begin_tag()}{tag_value}{self.to_html_end_tag()}"
        


     

