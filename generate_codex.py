import sys
sys.dont_write_bytecode = True
from prompts.codex import generate_codex_prompt
from util.files import write_file


aspect_to_improve = """This setting is meant for military adventures that recreate the politics (and to a lesser degree the culture) of the colonial powers of the 19th century.
"""
write_file(generate_codex_prompt(codex_prompt=aspect_to_improve))
