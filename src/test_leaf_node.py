import unittest

from leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_example_1(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node, expected)

    def test_example_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = "<a href=https://www.google.com>Click me!</a>"       
        self.assertEqual(node, expected)

    def test_constructor(self):
        node = None
        raised = False
        try:
            node = LeafNode(None, None, None)
        except ValueError:
            raised = True
        self.assertTrue(raised and node is None)


if __name__ == "__main__":
    unittest.main()