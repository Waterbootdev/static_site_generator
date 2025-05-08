class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        
        if(value is None and  children is None):
            HTMLNode.raise_exception()
        
        self.value = value # string
        self.children = children # list of HTMLNode's
        self.tag = tag # string
        self.props = {} if props is None else  props if type(props) is dict else HTMLNode.raise_exception() 
        # dict key-value pairs representing attributes

    @staticmethod
    def raise_exception():
        raise Exception()

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return ''.join([f" {key}={value}" for key, value in self.props.items()])

    def __repr__(self):
        print(self)

     

