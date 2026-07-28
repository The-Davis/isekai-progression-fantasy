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

At the sawmill, Tal breathlessly relays everything he learned from the scholar. He taps his chest, explaining that everyone possesses a "mana core," a sleeping engine of magic.
Clary rolls her eyes and tells Tal she thinks he's more likely to summon a stomach ache than a fireball.
Cord keeps his thoughts to himself, though he prods his own stomach thoughtfully. Wicket seems to be pondering something, but also keeps quiet.
Elsie is thoroughly amazed and confidently states her belief that Tal probably already has magic.
Tal asks if any of them know how to force a mana core to awaken. After some hesitation, Wicket claims he heard about a foolproof method from someone, but it was one of his pap's drinking friends, so it's probably no good. Tal's willing to try.

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


**1. The Dungeon Proposition and Debate**
*   **Tal Drops the Hook:** Tal pivots the conversation from the abstract idea of mana cores to Jasper's concrete goal: the unmapped dungeon. He excitedly explains that if they can find the dungeon's location first, they can trade that information to Jasper in exchange for learning how to awaken their magic. 
*   **Cord's Practical Resistance:** Cord frowns at the idea. As the group's best woodsman, he knows the local forests and the upper fringes of the Everdark shallows better than anyone. He points out that wandering into uncharted caves is a good way to get eaten by a cavern crawler or fall into a magma vent. Being pragmatic, Cord suggests that if they *must* look for this, they should just ask his father (the cooper) or the senior tree-fellers if they've spotted any new sinkholes or ruins on the company's timber claims. 
*   **Clary's Grounded Skepticism:** Clary strongly backs up her brother, her crush on Tal manifesting as biting sarcasm. She tells Tal he's got his head in the clouds again and is letting a fancy city dandy spin him in circles. She argues that if an actual dungeon was nearby, the adult delvers or the King's exactors would have found it years ago. She advises Tal to forget this "delver phase," stick to fishing, and leave the woods to the loggers.
*   **Wicket's Superstitious Panic:** The moment the word "dungeon" is firmly established, Wicket starts furiously rubbing a dried river-stone charm on his necklace. He frantically recites a Corvish superstition—perhaps warning Tal that talking about the Everdark in an abandoned building is bad luck and will "wake the knockers." However, Wicket's bardic curiosity battles his cowardice; he is terrified of monsters, but the thought of unearthing a real magical artifact like in his tavern songs keeps him rooted to his seat. He whines about how dangerous it is, but refuses to leave Tal's side.
*   **Elsie's Cheerful Support:** Elsie completely ignores the danger, proudly declaring that Tallow is the bravest boy in Larchleah and could easily beat up any monster in a dungeon. She eagerly asks if she can come along to hold the torch.
*   **A Compromise Reached:** Knowing Cord's pride in his wilderness skills, Tal flatters him, pointing out that none of the adult loggers know the secret hollows as well as Cord does. Cord reluctantly admits there *is* one area the feller crews strictly avoid—a treacherous ridge near the old, overgrown graveyard on the hill, where the ground frequently gives way to deep stone fissures. 

**2. The Horn and the Dash**
*   **The Interruption:** Just as Cord begins to detail the layout of the ridge near the graveyard (neatly foreshadowing where Jasper and Gobber Dob will actually go digging later), a massive, booming blast from a barge horn echoes across the river. 
*   **Tal's Confusion:** The group falls silent. Tal's brow furrows in total disbelief. He knows the barge schedules intimately; his father *just* left that morning. It takes days to go downriver to Dornon and back. A barge horn blowing now makes absolutely no sense unless there was a wreck, an emergency, or his father forgot something critical and turned the massive ship around.
*   **The Scramble:** Panic and curiosity seize the group. The dungeon debate is instantly forgotten. Clary and Cord look worried that it might be a company emergency, while Wicket mutters about river omens. 
*   **The Chapter End:** Tal leaps up from the mossy beams of the sawmill and dashes out the door, yelling for the others to follow. The chapter ends on a high-energy cliffhanger as the five kids sprint through the muddy streets of Larchleah toward the docks, hearts pounding as they race to see what has unexpectedly arrived on the River Varn. *(This perfectly sets up Chapter Seven, where Tal discovers it isn't his father, but rather a specialized Company transport bringing the new Foreman and his daughter, Rosie).*

"""
