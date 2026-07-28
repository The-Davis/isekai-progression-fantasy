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

**Scene 3: Wicket's Hogwash Ritual**
*   **The Setting:** The group heads to the edge of town, just where the unpaved streets give way to the imposing, ancient pine stands. 
*   **The Ridiculous Instructions:** Wicket confidently dictates the "ritual" to wake the inner fire. It is absolute hogwash. He tells Tal he must smear cold river mud directly over his heart (where the core sits), eat a bitter, green pinecone to "shock" the spirit, spin in a circle to mimic an eddy, and recite a specific nursery rhyme backward.
*   **The Comedic Failure:** Tal is so desperate for magic that he completely ignores his dignity (and the intellect of his past life). He actually performs the ritual. 
*   **The Result:** Cord and Clary are practically doubled over with laughter. Tal chokes on the bitter pine sap, gets dizzy from spinning, and falls flat on his back in the dirt. No magic happens; he just gets a dizzy spell and a bad taste in his mouth. Clary ribs him mercilessly, while sweet Elsie pats his muddy head and tells him he looked very magical while falling. 


*Scene 3: Wicket's Hogwash Ritual**
*   **Into the woods:** Wicket refuses to do the ritual in town where "the iron horseshoes on the road will scatter the magic." He leads the skeptical group to a secluded clearing just past the tree line of the oak and pine forest.
*   **The ridiculous requirements:** Wicket's ritual is a hodgepodge of Corvish folklore and utter nonsense. It involves Tal rubbing river mud on his forehead, holding a specific dried frog bone, standing on one leg, and chanting a rhyming Corvish nursery song backward while visualizing a fire in his belly.
*   **The attempt:** Desperate enough to try anything, Tal actually does it. The scene plays for maximum comedy. Tal is red-faced, straining his willpower, hopping on one leg, and chanting gibberish.
*   **The embarrassment:** Clary and Cord are laughing so hard they are leaning against each other. Elsie tries to mimic Tal's one-legged stance in solidarity but keeps falling over. Tal finally gives up, exhausted, muddy, and feeling utterly humiliated. He realizes Wicket's folklore is completely useless, and the system of this world requires a real key, not children's games.

"""
