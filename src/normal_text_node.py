from textnode import TextNode, TextType
from commen_helpers import apply_pair, alternated_seq, reduce_lists, is_odd, apply_tripple
from delimiter_text_type import DelimiterTextType
from extract_markdown import extract_markdown_images_tip, extract_markdown_links_tip
class NORMALTextNode(TextNode):

    def __init__(self, text):
        super().__init__(text, TextType.NORMAL)

    def __repr__(self):
        return f"NORMALTextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def split_node_delimiter(self, delimiter):
        return NORMALTextNode.split_node_text_delimiter(self.text, delimiter)

    @staticmethod
    def split_node_text_delimiter(node_text, delimiter):
        if not isinstance(delimiter, DelimiterTextType):
            raise ValueError("delimiter has to be a DelimiterTextType")

        def split_node_text():
            splitted = node_text.split(delimiter.delimiter_text())
            return splitted, len(splitted)

        @ apply_pair
        def add_text_type(splitted, length):
            def do_not_split_up():
                return [(TextType.NORMAL, node_text)]
        
            def add_text_type():
                alternated_text_types = alternated_seq(TextType.NORMAL, delimiter.text_type(), length)
                return zip(alternated_text_types, splitted)

            return add_text_type() if is_odd(length) else do_not_split_up()  

        def filter_non_empty(seq):
            return filter(lambda x: len(x[1]) > 0 , seq)

        @ apply_pair
        def to_text_node(text_type, text):
            match text_type:
                case TextType.NORMAL:
                    return NORMALTextNode(text)
                case _:
                    return TextNode(text=text, text_type=text_type)  
        
        return list(map(to_text_node, filter_non_empty(add_text_type(split_node_text()))))   

    @staticmethod   
    def text_nodes_to_normal_text_nodes(nodes):
            return map(lambda node: NORMALTextNode(node.text) if node.text_type == TextType.NORMAL else node, nodes)
     
    @staticmethod
    def split_nodes_delimiter(nodes, delimiter_text_type):
        def split_node_delimiter(node):
            return node.split_node_delimiter(delimiter_text_type) if isinstance(node, NORMALTextNode) else [node] 
        return reduce_lists(map(split_node_delimiter, nodes))

    @staticmethod
    def apply_split_node(split_node):
        def apply_split_node(node):
            return split_node(node) if isinstance(node, NORMALTextNode) else [node]
        return apply_split_node
    
    @apply_split_node
    @staticmethod
    def _split_node_image(node):
        return node.split_node_image()    
    
    @apply_split_node
    @staticmethod
    def _split_node_link(node):
        return node.split_node_link()    

    @ apply_tripple
    @staticmethod
    def split_extracted(text_type, text, extracted):
        nodes = []

        def append_text_node(text):
            if len(text) > 0:
                nodes.append(NORMALTextNode(text))

        @apply_pair
        def append_text_type_node(text, url):
            nodes.append(TextNode(text=text, text_type=text_type, url=url))

        for current in extracted:
            current_splited = text.split(current[1], maxsplit=1)
            append_text_node(current_splited[0])
            append_text_type_node(current[0])
            text = current_splited[1]
        append_text_node(text)
    
        return nodes

    def split_node_image(self):
        return NORMALTextNode.split_extracted(extract_markdown_images_tip(self.text))
    
    def split_node_link(self):
        return NORMALTextNode.split_extracted(extract_markdown_links_tip(self.text))
 
    @staticmethod
    def apply_split_nodes(split_node, nodes):
        return reduce_lists(map(split_node, nodes))
      
    @staticmethod
    def split_nodes_image(nodes):
        return NORMALTextNode.apply_split_nodes(NORMALTextNode._split_node_image, nodes)
    
    @staticmethod
    def split_nodes_link(nodes):
        return NORMALTextNode.apply_split_nodes(NORMALTextNode._split_node_link, nodes)
    
