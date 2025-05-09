import unittest

import extract_markdown

class TestExtractMarcdown(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        images_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown.extract_markdown_images(images_text), extract_markdown.extract_markdown_images_tip(images_text))

    def test_extract_markdown_links(self):
        links_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown.extract_markdown_links(links_text), extract_markdown.extract_markdown_links_tip(links_text))
        
    def test_extract_markdown_images_no_match(self):
        links_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown.extract_markdown_images(links_text), extract_markdown.extract_markdown_images_tip(links_text))

    def test_extract_markdown_links_no_match(self):
        images_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown.extract_markdown_links(images_text), extract_markdown.extract_markdown_links_tip(images_text))
 
 
if __name__ == "__main__":
    unittest.main()
    
        