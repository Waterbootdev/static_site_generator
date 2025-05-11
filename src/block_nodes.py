from code_block_node import CodeBlockNode
from quote_block_node import QuoteBlockNode
from ordered_list_node import OrderedListNode
from unordered_list_node import UnorderedListNode
from paragraph_node import ParagraphNode
from heading_node import HeadingNode

from blocktype import get_block_type, BlockType

def block_to_html_node(block):
    match get_block_type(block):
         case BlockType.PARAGRAPH:
              return ParagraphNode(block)
         case BlockType.ORDEREDLIST:
              return OrderedListNode(block)
         case BlockType.UNORDEREDLIST:
              return UnorderedListNode(block)
         case BlockType.QUOTE:
              return QuoteBlockNode(block)
         case BlockType.CODE:
              return CodeBlockNode(block)
         case BlockType.HEADING:
              return HeadingNode(block)
         case _:
              raise NotImplementedError()
          
def blocks_to_html_nodes(blocks):
     return list(map(block_to_html_node, blocks))    
