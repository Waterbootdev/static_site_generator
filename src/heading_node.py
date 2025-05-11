from parent_node import ParentNode
from normal_text_node import NORMALTextNode
from blocktype import BlockType
from extract_markdown import select_block_type 
from commen_helpers import trim_left_first

class HeadingNode(ParentNode):
    def __init__(self, block):
        number, value = trim_left_first(' ', block)
        text = value.strip()

        super().__init__(f"h{number}", NORMALTextNode.text_to_html_nodes(text))
        
        self.heading_number = number
        self.text = text

    def is_titel(self):
        return self.heading_number == 1
    
    @staticmethod
    def extract_titel_nodes(markdown,):
        return [node for node in map(HeadingNode, select_block_type(markdown, BlockType.HEADING)) if node.is_titel()]

    @staticmethod
    def extract_titel(markdown):
    
        titel_nodes = HeadingNode.extract_titel_nodes(markdown)
        length = len(titel_nodes)
    
        if length == 0:
            raise Exception("can't find titel")

        if length > 1:
            print("Warning more then one titel")
    
        return titel_nodes[0].text
