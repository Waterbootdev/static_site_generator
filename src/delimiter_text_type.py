from enum import Enum
from textnode import TextType

class DelimiterTextType(Enum):
    BOLD = ("**", TextType.BOLD)
    ITALIC = ("_", TextType.ITALIC)
    CODE = ("`", TextType.CODE)

    def delimiter_text(delimiter_text_type):
        return delimiter_text_type.value[0]
    def text_type(delimiter_text_type):
        return delimiter_text_type.value[1]
    
    @staticmethod
    def get_delimiter_text_type(delimiter_text, text_type):
        match (delimiter_text, text_type):
            case ("**", TextType.BOLD):
                return DelimiterTextType.BOLD
            case ("_", TextType.ITALIC):
                return DelimiterTextType.ITALIC
            case ("`", TextType.CODE):
                return DelimiterTextType.CODE
            case _:
                raise ValueError(f"no DelimiterTextType for {(delimiter_text, text_type)}") 
    
