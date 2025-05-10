import unittest

from normal_text_node import NORMALTextNode, DelimiterTextType
from textnode import TextNode, TextType
class TestNORMALTextNode(unittest.TestCase):

    def test_empty_str(self):
       
       self.assertEqual([], NORMALTextNode("").split_node_delimiter(DelimiterTextType.BOLD))
       self.assertEqual([], NORMALTextNode("").split_node_delimiter(DelimiterTextType.ITALIC))
       self.assertEqual([], NORMALTextNode("").split_node_delimiter(DelimiterTextType.CODE))
       
    def test_without_delimiters(self):
    
       text = "hjflhj" 
       
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.BOLD)) 
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.CODE)) 
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.ITALIC)) 
       
    def test_with_single_delimiters(self):
       
       text = ";sjk**hfj`hsj'kj_klf"
       
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.BOLD)) 
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.CODE)) 
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.ITALIC)) 

    def test_with_single_odd_number_delimiters(self):
       
       text = ";sj`k**h_fj`hsj'kj_jhfh**jgjk_hj**uosd`rtsklf"
       
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.BOLD))
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.CODE)) 
       self.assertListEqual([NORMALTextNode(text)], NORMALTextNode(text).split_node_delimiter(DelimiterTextType.ITALIC)) 
       
    def test_with_one_delimiter_even_number_delimiters(self):

        def test_with_one_delimiter_even_number_delimiters_sub(text, text_delimiter, text_type, delimiter_text_type):
            text_list = text.split(text_delimiter)
            self.assertListEqual([NORMALTextNode(text_list[0]), TextNode(text=text_list[1], text_type=text_type) , NORMALTextNode(text_list[2]),TextNode(text=text_list[3], text_type=text_type), NORMALTextNode(text_list[4])], NORMALTextNode(text).split_node_delimiter(delimiter_text_type))
        
        text = "ghjgg**jhlf**_ljhg_lhjj`fkfty`hjfhjfl`fyuyu`hfh_fhjg_**hjgjkhg**kjhjk"
       
        test_with_one_delimiter_even_number_delimiters_sub(text, "**",  TextType.BOLD, DelimiterTextType.BOLD) 
        test_with_one_delimiter_even_number_delimiters_sub(text, "_",  TextType.ITALIC, DelimiterTextType.ITALIC) 
        test_with_one_delimiter_even_number_delimiters_sub(text, "`",  TextType.CODE, DelimiterTextType.CODE)
    
    def test_split_images(self):
         node = NORMALTextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
         )
         new_nodes = NORMALTextNode.split_nodes_image([node])
         self.assertListEqual(
            [
                  TextNode("This is text with an ", TextType.NORMAL),
                  TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                  TextNode(" and another ", TextType.NORMAL),
                  TextNode(
                     "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                  ),
            ],
            new_nodes,
         )

    def test(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        test = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.NORMAL),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
            ]    
        
        self.assertListEqual(NORMALTextNode.text_to_textnodes(text), test)

    
if __name__ == "__main__":
    unittest.main()