import sys
sys.dont_write_bytecode = True
from story import current_story
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters


def generate_character_prompt(character_info: str) -> str:
    output = "You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.\n\n"
    output += "This is an isekai progression fantasy story with a male protagonist, and a world that's a mix of magical fantasy and Napoleonic War era tech. We are aiming for a mix of the \"Cozy Violent\" found in \"A Soldier's Life\" (AlwaysRollsAOne) crossed with some of the gritty adventure of Sharpe's Rifles.\n"
    output += "You are an expert in this genre and have a deep understanding of storytelling and worldbuilding techniques.\n\n"
    output += "You also have keen insight into character development and narrative structure, particularly in developing compelling and interesting characters and understanding their motivations.\n\n"
    
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
    
    output += "Your task is to brainstorm a new character for this story. Here is the basic information about this character:\n\n"
    output += f"{character_info}\n\n"
    output += "Please propose a character that fills this role and fits into the the world I've provided.\n"
    output += "Thank you."
    return output

