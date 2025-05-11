from functools import reduce

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        
        HTMLNode._validate_parameters_or_rais_value_error(tag, value, children, props)

        self.value = value
        self.children = children 
        self.tag = tag 
        self.props = {} if props is None else  props 

    @staticmethod
    def _validate_parameters_or_rais_value_error(tag, value, children, props):
        if value is None and children is None:
            HTMLNode._raise_exception("value or children has to be not none")

        if HTMLNode._is_not_none_and_not_type(children, list) and HTMLNode._is_not_list_of_html_nodes(children) :
            HTMLNode._raise_exception("children has to be None or a list of at least one child")

        if HTMLNode._is_not_none_and_not_type(props, dict):
            HTMLNode._raise_exception("props has to be None or a dict")

        if HTMLNode._is_not_none_and_not_type(value, str):
            HTMLNode._raise_exception("value has to be None or a str")

        if HTMLNode._is_not_none_and_not_type(tag, str):
            HTMLNode._raise_exception("tag has to be None or a str")
      
    @staticmethod
    def _is_not_none_and_not_type(parameter, parameter_type):
        return parameter is not None and type(parameter) is not parameter_type 

    @staticmethod
    def _is_not_list_of_html_nodes(children):
        #children is list
        return len(children) == 0 or not reduce(bool.__and__, map(lambda child: isinstance(child, HTMLNode) ,children), True)
        
    @staticmethod
    def _raise_exception(message):
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
    