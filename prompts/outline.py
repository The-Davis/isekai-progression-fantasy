import sys
sys.dont_write_bytecode = True
from story import current_story
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from outline import get_outline


def generate_outline_prompt(next_section: str) -> str:
    output = """You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.
I am working on a planar progression fantasy adventure story with no working title. We're setting up a larger story where Earth is being integrated into a multi-planar economy and society, but our introduction story is much more down-to-Earth.
Other dimensions are real. Magic is real. The vastness of the cosmos is overwhelming. This is pretty much Planescape/Spelljammer with the labels peeled off and replaced."""
    
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

    output += "Your task is to create a broad outline for an upcoming section of the story. Here is what we have to work out now:\n"
    output += f"\n{next_section}\n"
    output += "Please ensure that the outline fits into the world I've provided, provides the characters with interesting challenges and dynamic scenes, and doesn't contradict anything in the notes or story so far.\n"
    output += "Thank you."
    return output
