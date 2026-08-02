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

Tal denies Cord's suggestion that Jasper is lying for fun by focusing on the scholar's stated goal: the unmapped dungeon. He explains that if they can find the dungeon's location first, they can trade that information to Jasper in exchange for learning how to awaken their magic. Imagine being wizards.
Cord frowns at the idea. Just about everyone in town agrees that he knows the local forests and even a few caves leading to the Everdark better than anyone. If anyone could find an unmapped dungeon, he could but Cord points out that wandering into uncharted caves is a good way to get eaten by a cavern crawler or fall into a miles-deep crevice.Cord suggests that if they *must* look for this, they should just ask the loggers if they've spotted any new sinkholes or ruins on the company's timber claims.
Clary strongly backs up her brother, her crush on Tal manifesting as biting sarcasm. She tells Tal he's got his head in the clouds again and is letting a fancy city dandy spin him in circles. She argues that if an actual dungeon was nearby, the adult delvers or the King's exactors would have found it years ago. She advises Tal to forget this whole thing and leave the woods to the loggers. Or better yet, start earning his keep by swinging an axe. Tal does not like this idea at all.
Wicket should look nervous through the whole exchange (insert a reaction or two before now) and finally speaks up. He says there are all sorts of haints and spooks besides cavern crawlers to worry about. The Everdark is no joke. Tal plies him with the idea of treasure, and Wicket has to admit treasure would be nice.
Elsie blithely agrees that they'll find the treasure for sure, proudly declaring that Tallow will beat up any monster in a dungeon. She eagerly asks if she can come along.
Tal pushes Cord one more time, flattering his skills by pointing out that none of the adult loggers know the secret hollows as well as Cord does, so Clary's suggestion is a waste of time (earning a scowl from her). Cord reluctantly admits there *is* a stretch of woods atop a treacherous ridge near the old graveyard. The loggers avoid it since the ground frequently gives way to deep stone fissures. One of those fissures *might* go down to the Everdark.

You can stop there and we'll edit before I provide the next section.



Please write this section following the outline, maintaining consistency with the established world and characters, and using the following writing style:
You are writing in the first-person retrospective ("I"). You are writing as Talmon Sager, a man reborn into a series of ringworlds. The prospect of a second life full of adventure is exciting and appealing.
You use simple, workmanlike prose most of the time, but occasionally switch to longer and more poetic sentences, particularly when being sentimental (especially about women) or discussing serious matters.
You are not of this world and you know it. Describe your exceptional abilities matter-of-factly and without false modesty.
Thank you."""
    return output


write_file(generate_chapter_prompt())

"""
You can stop there and we'll edit before I provide the next section.

We'll end the chapter on that note.



**2. The Horn and the Dash**
*   **The Interruption:** Just as Cord begins to detail the layout of the ridge near the graveyard (neatly foreshadowing where Jasper and Gobber Dob will actually go digging later), a massive, booming blast from a barge horn echoes across the river. 
*   **Tal's Confusion:** The group falls silent. Tal's brow furrows in total disbelief. He knows the barge schedules intimately; his father *just* left that morning. It takes days to go downriver to Dornon and back. A barge horn blowing now makes absolutely no sense unless there was a wreck, an emergency, or his father forgot something critical and turned the massive ship around.
*   **The Scramble:** Panic and curiosity seize the group. The dungeon debate is instantly forgotten. Clary and Cord look worried that it might be a company emergency, while Wicket mutters about river omens. 
*   **The Chapter End:** Tal leaps up from the mossy beams of the sawmill and dashes out the door, yelling for the others to follow. The chapter ends on a high-energy cliffhanger as the five kids sprint through the muddy streets of Larchleah toward the docks, hearts pounding as they race to see what has unexpectedly arrived on the River Varn. *(This perfectly sets up Chapter Seven, where Tal discovers it isn't his father, but rather a specialized Company transport bringing the new Foreman and his daughter, Rosie).*

"""
