import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from constants import STORY_DESCRIPTION


def generate_character_prompt() -> str:
    output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.\n\n
{STORY_DESCRIPTION}
You are an expert in this genre and have a deep understanding of storytelling and worldbuilding techniques.\n\n"
You also have keen insight into character development and narrative structure, particularly in developing compelling and interesting characters and understanding their motivations."""
    
    if get_codex():
        output += "Here are some details about the world our story is set in:\n\n"
        for entry in get_codex():
            output += entry.about() + "\n\n"

    if get_characters():
        output += "Here are some notes about the characters in the story:\n\n"
        for character in get_characters():
            output += character.about() + "\n\n"

    if get_all_chapters():
        output += "Here is the story so far:\n\n"
        for chapter in get_all_chapters():
            output += chapter.prompt_entry() + "\n\n"
    
    output += """Your task is to brainstorm a new character for this story. Here is the basic information about this character:\n\n

Please propose a character that fills this role and fits into the the world I've provided.\n"
Thank you."""
    return output


write_file(generate_character_prompt())
