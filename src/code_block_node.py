from leaf_node import LeafNode
from parent_node import ParentNode

class CodeBlockNode(ParentNode):
    def __init__(self, block):
        super().__init__('pre', [LeafNode('code', '\n'.join(block.splitlines()[1:-1])+'\n')])

