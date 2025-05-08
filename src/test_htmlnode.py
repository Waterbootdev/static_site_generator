import unittest

from htmlnode import HTMLNode

from random import randint

class TestHTMLNode(unittest.TestCase):
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
    
        

