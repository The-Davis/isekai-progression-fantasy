import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from constants import STORY_DESCRIPTION


def generate_chapter_prompt() -> str:
    output = f"""You are a creative writing assistant helping me write a chapter of my story.
{STORY_DESCRIPTION}
You are an expert in adventure fantasy and have a deep understanding of storytelling techniques, character development, and worldbuilding.
"""

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
    
    output += """Now I need you to write the next section. Here is the outline:

Elsie asks Cord to tell about the ridge. Is it haunted? Graveyards are scary. Tal encourages this as well, focusing on more practical things like how to get to the ridge.
Just as Cord begins to detail the layout of the ridge near the graveyard, a blast from a barge horn echoes across the river. 
The group falls silent and Tal's brow furrows in total disbelief. He knows the barge schedules intimately; his father *just* left that morning. It takes days to go downriver to Dornon and back. A barge horn blowing now makes absolutely no sense unless there was a wreck, an emergency, or his father forgot something critical and turned the massive ship around.
The dungeon debate is forgotten as panic and curiosity seize the group. Clary and Cord look worried that it might be a company emergency, while Wicket mutters about bad omens.
Tal leaps up from the sawmill and dashes out the door, yelling for the others to follow.
The chapter ends on a high-energy cliffhanger as the five kids sprint through the muddy streets of Larchleah toward the docks, hearts pounding as they race to see what has unexpectedly arrived on the River Varn: a fancy company riverboat under full sail.

We'll end the chapter on that note.



Please write this section following the outline, maintaining consistency with the established world and characters, and using the following writing style:
You are writing in the first-person retrospective ("I"). You are writing as Talmon Sager, a man reborn into a series of ringworlds. The prospect of a second life full of adventure is exciting and appealing.
You use simple, workmanlike prose most of the time, but occasionally switch to longer and more poetic sentences, particularly when being sentimental or discussing serious matters.
You are not of this world and you know it. Describe your exceptional abilities matter-of-factly and without false modesty.
Thank you."""
    return output


write_file(generate_chapter_prompt())

"""
You can stop there and we'll edit before I provide the next section.

We'll end the chapter on that note.




"""
