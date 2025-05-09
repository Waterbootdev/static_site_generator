from enum import Enum
from textnode import TextNode, TextType
from functools import reduce

class DelimiterTextType(Enum):
    BOLD = ("**", TextType.BOLD)
    ITALIC = ("_", TextType.ITALIC)
    CODE = ("`", TextType.CODE)

    def delimiter_text(delimiter_text_type):
        return delimiter_text_type.value[0]
    def text_type(delimiter_text_type):
        return delimiter_text_type.value[1]
    
    @staticmethod
    def get_delimiter_text_type(delimiter_text, text_type):
        match (delimiter_text, text_type):
            case ("**", TextType.BOLD):
                return DelimiterTextType.BOLD
            case ("_", TextType.ITALIC):
                return DelimiterTextType.ITALIC
            case ("`", TextType.CODE):
                return DelimiterTextType.CODE
            case _:
                raise ValueError(f"no DelimiterTextType for {(delimiter_text, text_type)}") 
    

class NORMALTextNode(TextNode):
    def __init__(self, text):
        super().__init__(text, TextType.NORMAL)

    def __repr__(self):
        return f"NORMALTextNode({self.text}, {self.text_type.value}, {self.url})"
    
    @staticmethod 
    def test_split():
        text = "'code'"
        print(text.split("'"))

    @staticmethod
    def _split_node_text_delimiter_add_text_type(node_text, delimiter):
        
        splitted = node_text.split(delimiter.delimiter_text())

        length = len(splitted)

        return [(TextType.NORMAL, node_text)] if length%2 == 0 else filter(lambda x: len(x[1]) > 0 , zip(NORMALTextNode._alternated_text_type(TextType.NORMAL, delimiter.text_type(), length), splitted))

    @staticmethod
    def _alternated_text_type(even_text_type, odd_text_type, length):
        return map(lambda index: even_text_type if index%2 == 0 else odd_text_type, range(0, length))

    @staticmethod 
    def apply_pair(func):
        def from_pair(pair):
            return func(pair[0], pair[1])
        return from_pair

    
    @ apply_pair
    @staticmethod
    def _to_text_node(text_type, text):
        match text_type:
            case TextType.NORMAL:
                return NORMALTextNode(text)
            case _:
                return TextNode(text=text, text_type=text_type)  
    
    def split_node_delimiter(self, delimiter):
        if not isinstance(delimiter, DelimiterTextType):
            raise ValueError("delimiter has to be a DelimiterTextType")

        return list(map(NORMALTextNode._to_text_node, NORMALTextNode._split_node_text_delimiter_add_text_type(self.text, delimiter)))   
    
    @staticmethod
    def _split_nodes_delimiter_parameter_specs(func):
        def parameter_specs(old_nodes, delimiter, text_type):
            return func(old_nodes, DelimiterTextType.get_delimiter_text_type(delimiter, text_type))
        return parameter_specs

    @staticmethod
    def reduce_list(lists):
        return reduce(lambda x, y: x + y, lists, [])

    @_split_nodes_delimiter_parameter_specs
    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter_text_type):
        return  NORMALTextNode.reduce_list(NORMALTextNode._split_nodes_delimiter_map(old_nodes, delimiter_text_type))

    @staticmethod
    def _text_nodes_to_normal_text_nodes(nodes):
        return map(lambda node: NORMALTextNode(node.text) if node.text_type == TextType.NORMAL else node, nodes)
    
    @staticmethod
    def _split_nodes_delimiter_map(nodes, delimiter_text_type):
        return map(lambda node: [node] if not isinstance(node, NORMALTextNode) else node.split_node_delimiter(delimiter_text_type), NORMALTextNode._text_nodes_to_normal_text_nodes(nodes))
     