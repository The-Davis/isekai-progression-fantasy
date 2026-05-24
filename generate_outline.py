import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Given the five acts of the story, please expand each act with a little more detail.
Work in themes of:
The Absurdity of the Infinite: In a multiverse where anything is possible, the most common problems are still bureaucracy, miscommunication, and poor planning.
Home is a Relative Concept: Toby finds that he feels more at home among an eccentric crew of outsiders than he did in his predictable suburban life.
"""

write_file(generate_outline_prompt(next_section=next_section))
