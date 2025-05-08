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
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_boold_italic_code(self):
        self.assertEqual(TextNode("test", TextType.BOLD, "hjk'dlhjíalkjhdsil").text_node_to_html_node().to_html(), "<b>test</b>")
        self.assertEqual(TextNode("test", TextType.ITALIC, "hjk'dsil").text_node_to_html_node().to_html(), "<i>test</i>")
        self.assertEqual(TextNode("test", TextType.CODE, "hjk'dsil").text_node_to_html_node().to_html(), "<code>test</code>")

    def test_links(self):
        node = TextNode("anchor text", TextType.LINKS, url="https://www.boot.dev/lessons/80ddb6c5-8324-4850-a28c-0c6207596857")
        self.assertEqual(node.text_node_to_html_node().to_html(),"<a href=https://www.boot.dev/lessons/80ddb6c5-8324-4850-a28c-0c6207596857>anchor text</a>")   
    def test_images(self):
        node = TextNode("alt text", TextType.IMAGES, url="https://www.europosters.nl/vector-illustration-of-crossed-axes-with-woodgrain-texture-and-metallic-red-blades-for-emblem-designs-f999848926")
        self.assertEqual(node.text_node_to_html_node().to_html(),"<img src=https://www.europosters.nl/vector-illustration-of-crossed-axes-with-woodgrain-texture-and-metallic-red-blades-for-emblem-designs-f999848926 alt=alt text></img>")   

if __name__ == "__main__":
    unittest.main()