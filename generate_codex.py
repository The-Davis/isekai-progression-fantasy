import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from constants import STORY_DESCRIPTION


def generate_codex_prompt() -> str:
    output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.
{STORY_DESCRIPTION}
You are an expert in this genre and have a deep understanding of storytelling and worldbuilding techniques.
"""

    if get_codex():
        output += "Here are the current \"codex\" entries about the setting/world for this story:\n\n"
        for entry in get_codex():
            output += entry.about() + "\n"        

    if get_characters():
        output += "Here are some notes about the characters in the story:\n"
        for character in get_characters():
            output += character.about() + "\n"
    
    if get_all_chapters():
        output += "Here is the story so far:\n"
        for chapter in get_all_chapters():
            output += chapter.prompt_entry() + "\n"

    output += """Your task is to help me write a codex entry for an element of the world. Here are my notes for this codex entry:

We've established that Tal (our viewpoint character) lives in a logging town on the Varn, far upriver from Dornon. We need to build a bit of information around this town.
I'm thinking it's a company town, mostly running on scrip and barter, with some coin for side gigs.
    
Please write a codex entry that fulfill this need, fits the general theme and vibe of the world so far, and doesn't contradict any of the existing codex entries I have provided you here.
Thank you."""
    return output


write_file(generate_codex_prompt())
