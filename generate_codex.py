import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex


def generate_codex_prompt() -> str:
    output = """You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.

You are an expert in this genre and have a deep understanding of storytelling and worldbuilding techniques.
current_story.setting_notes}\n"""

    if get_codex():
        output += "Here are the current \"codex\" entries about the setting/world for this story:\n\n"
        for entry in get_codex():
            output += entry.about() + "\n"        

    output += """Your task is to help me write a codex entry for an element of the world. Here are my notes for this codex entry:

Please write a codex entry that fulfill this need, fits the general theme and vibe of the world so far, and doesn't contradict any of the existing codex entries I have provided you here.
Thank you."""
    return output


write_file(generate_codex_prompt())
