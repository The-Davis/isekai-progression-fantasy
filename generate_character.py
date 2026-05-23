import sys
sys.dont_write_bytecode = True
from prompts.character import generate_character_prompt
from util.files import write_file


character_info = """


"""

write_file(generate_character_prompt(character_info=character_info))
