import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_un_eq_text(self):
        node = TextNode("This is a tet node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_un_eq_type(self):
        node = TextNode("This is a node", TextType.ITALIC)
        node2 = TextNode("This is a node", TextType.IMAGES)
        self.assertNotEqual(node, node2)
    def test_un_eq_url(self):
        node = TextNode("This is a node", TextType.LINKS)
        node2 = TextNode("This is a node", TextType.LINKS, "")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()