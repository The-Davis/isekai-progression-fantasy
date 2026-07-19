import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from outline import get_outline
from constants import STORY_DESCRIPTION

def generate_outline_prompt() -> str:
    output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.
{STORY_DESCRIPTION}

"""
    
    if get_codex():
        output += "Here are some details about the world our story is set in:\n"
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
    
    if get_outline():
        output += "Here is the outline so far:\n"
        for outline in get_outline():
            output += outline.prompt_entry() + "\n"

    output += """Your task is to create a broad outline for an upcoming section of the story. Here is what we have to work out now:

    Please ensure that the outline fits into the world I've provided, provides the characters with interesting challenges and dynamic scenes, and doesn't contradict anything in the notes or story so far.
    Thank you."""
    return output


write_file(generate_outline_prompt())
