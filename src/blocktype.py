from enum import Enum
from re import match
from functools import reduce
from commen_helpers import apply_pair

class BlockType(Enum):
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDEREDLIST="unordered_list"
    ORDEREDLIST="ordered_list"
    PARAGRAPH="paragraph"
    
def is_match_line(r, line):
    return True if match(r, line)  else False

def is_heading_line(line):
    return is_match_line(r"#{1,6}+\s", line)

def is_heading_block(_, block):
    return is_heading_line(block)


# Code blocks must start with 3 backticks and end with 3 backticks.
# but solution says a code clock has at least 2 lines and the first aswel the last line starts with 3 backticks 
# but then the following woud be a empty code block (without leading #)

# ```jkas;dhjkhs;kjhs;jhd
# ```h;uihyihsihfhsihfi   


def is_code_line(line):
    return False

def is_code_block(lines, block):
    return is_match_line(r"^`{3}", lines[0]) and is_match_line(r"^`{3}", lines[-1]) 

def is_qoute_line(line):
    return line.startswith('>')

def all_lines_are(is_block_type_line, lines):
     return reduce(lambda is_block_type , line: is_block_type and is_block_type_line(line), lines, True)

def is_qoute_block(lines, _):
    return all_lines_are(is_qoute_line, lines)

def is_unordered_line(line):
    return is_match_line(r"-\s", line)

def is_unordered_block(lines, _):
    return all_lines_are(is_unordered_line, lines)

@apply_pair
def is_ordered_line(line, n):
    return is_match_line(f"{n}." + r"\s", line)

def is_ordered_block(lines, _):
    return reduce(lambda is_block_type , line: is_block_type and is_ordered_line(line), zip(lines, range(1, len(lines) + 1)), True)


def is_first_ordered_line(line):
    return is_match_line(r"1.\s", line)

def is_paragraph_line(_):
    return True
def is_paragraph_block(_, __):
    return True


def get_block_type_line(line):
    @apply_pair
    def get_block_type(is_block_type, block_type):
        def get_block_type(line):
            return  block_type if is_block_type(line) else None
        return get_block_type

    is_block_type_line = [is_heading_line, is_code_line, is_qoute_line, is_unordered_line, is_first_ordered_line, is_paragraph_line]
    block_types = [block_type for block_type in BlockType]

    return reduce(lambda block_type, func_block_type: block_type if block_type else get_block_type(func_block_type)(line), zip(is_block_type_line, block_types), None)


def get_block_type_lines(lines, block):
    @apply_pair
    def get_block_type(is_block_type, block_type):
        def get_block_type(lines, block):
            return  block_type if is_block_type(lines, block) else None
        return get_block_type

    is_block_type_line = [is_heading_block, is_code_block, is_qoute_block, is_unordered_block, is_ordered_block, is_paragraph_block]
    block_types = [block_type for block_type in BlockType]

    return reduce(lambda block_type, func_block_type: block_type if block_type else get_block_type(func_block_type)(lines, block), zip(is_block_type_line, block_types), None)


def get_block_type(markdown_block):
    
    lines = markdown_block.splitlines()

    return get_block_type_lines(lines, ''.join(lines)) if len(lines) > 1 else get_block_type_line(lines[0])
