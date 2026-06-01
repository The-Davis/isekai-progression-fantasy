import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Given the five acts of the story, please expand each act with a little more detail.
"""

write_file(generate_outline_prompt(next_section=next_section))
