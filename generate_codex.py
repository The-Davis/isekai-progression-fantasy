import sys
sys.dont_write_bytecode = True
from prompts.codex import generate_codex_prompt
from util.files import write_file


aspect_to_improve = """We need to flesh out the Druthi and the Ozkur a little bit mor
"""
write_file(generate_codex_prompt(codex_prompt=aspect_to_improve))
