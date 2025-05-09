import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType

from random import randint

class TestHTMLNode(unittest.TestCase):
    
    def test_is_not_list_of_html_nodes_true(self):
        b = True
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([]), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes({}), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([9]), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes(["htmlnode"]), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([TextNode("a", TextType.LINKS, url="https://www.google.com")]), b)
        node = HTMLNode(value="") 
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([node, 8]), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([node, "hs;fkjh", node]), b)
      
    def test_is_not_list_of_html_nodes_false(self):
        b = False
        node = HTMLNode(value="") 
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([node]), b)
        self.assertEqual(HTMLNode._is_not_list_of_html_nodes([node, node, node]), b)
    
    @staticmethod
    def props_node(props):
        return HTMLNode(value="",props=props)

    def test_none_props(self):
        self.assertEqual(TestHTMLNode.props_node(None).props_to_html(),"")        

    def test_example(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        excepted = " href=https://www.google.com target=_blank"
        node = TestHTMLNode.props_node(props)
        self.assertEqual(excepted, node.props_to_html())

    def test_count(self):
        n = randint(3, 10)

        props = {k:str(k) for k in range(0, n)}

        expected = n * 4

        self.assertEqual(expected, len(TestHTMLNode.props_node(props).props_to_html()))
    
    
        
if __name__ == "__main__":
    unittest.main()
    
        

