import sys
sys.dont_write_bytecode = True
from story import current_story
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters


def generate_chapter_prompt(chapter_outline: str, style: str) -> str:
    output = "You are a creative writing assistant helping me write a chapter of my story.\n"
    output += "This is an isekai progression fantasy story with a male protagonist, and a world that's a mix of magical fantasy and Napoleonic War era tech. We are aiming for a mix of the \"Cozy Violent\" found in \"A Soldier's Life\" (AlwaysRollsAOne) crossed with some of the gritty adventure of Sharpe's Rifles.\n"
    output += "You are an expert in adventure fantasy and have a deep understanding of storytelling techniques, character development, and worldbuilding.\n"

    if get_codex():
        output += "Here are the most relevant details about the world for this specific task:\n"
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
    
    output += "Now I need you to write the next section. Here is the outline:\n"
    output += f"{chapter_outline}\n"
    output += "Please write this section following the outline, maintaining consistency with the established world and characters, and using the following writing style:\n"
    output += f"{style}\n"
    output += "Thank you."
    return output
