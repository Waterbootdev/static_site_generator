import unittest
from extract_markdown import markdown_to_blocks
from blocktype import get_block_type, BlockType 


class TestBlockType(unittest.TestCase):
    def test_get_block_type(self):
        markdown="""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

1. hjguuiyiio
3. kjguigtiujo
2. kjguigtiujo

```
lguihyuyhuiyh
jkguhgu
```
>```
>lguihyuyhuiyh
>jkguhgu
>``

## heading
- hjguuiyiio
- kjguigtiujo

## heading
1. hjguuiyiio
2. kjguigtiujo

- hjguuiyiio
- kjguigtiujo

1. hjguuiyiio


1. hjguuiyiio
2. kjguigtiujo

```auyhgduhgau```

```
lguihyuyhuiyh
jkguhgu
```

>```
>lguihyuyhuiyh
>jkguhgu
>```
"""
        blocks = markdown_to_blocks(markdown)

        test = [BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.PARAGRAPH, BlockType.HEADING, BlockType.HEADING, BlockType.UNORDEREDLIST, BlockType.ORDEREDLIST, BlockType.ORDEREDLIST, BlockType.CODE, BlockType.CODE, BlockType.QUOTE]

        self.assertListEqual(list(map(get_block_type, blocks)), test)
        
