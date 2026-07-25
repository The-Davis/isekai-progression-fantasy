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

Sure enough, the new boy doesn't take Tal's threat sitting down, and he jeers right back that he bets he could whoop him. He follows it up with a fistful of river muck that catches Tal right in the face.
Tal shoves him, the boy shoves back, and it quickly escalates into a tumble. It's a clumsy, flailing fight, the sort of boyhood nonsense that quickly boils over. Unfortunately, the pair manage to roll right into the rushing current.
Forget grundylows, the Varn has its claws on them

We'll end the chapter on that note.



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


**Scene 4: A Scuffle on the Docks (Meeting Wicket)**
*   **Instant Friendship:** Shocked by the cold, they sit up in the water and look at each other. The absurdity of it hits them, and they burst into laughter. Wicket introduces himself and immediately scolds Tal for laughing too loudly, rattling off a Corvish superstition: *"Quiet down, Tallow, or you'll invite the river-hags to steal your teeth!"* Tal realizes he has just met a kindred spirit.

**Scene 5: The Cover-Up and the Stars**
*   **Sneaking Back:** The sun begins to set, and the boys realize they are freezing and covered in mud. Wicket, wanting to avoid his drunk father, tags along with Tal back to the Sager house.
*   **The Wing-Woman:** They attempt to sneak through the back window, but are caught by Elsie, Tal's sweet-tempered younger sister. Instead of screaming for their mother, Elsie takes pity on them. She fetches an old rag to wipe them down, hides the ruined boots under a loose floorboard, and smuggles Wicket a leftover sweet-roll from the pantry.
*   **Resolution:** Safely in his room, Tal looks out the window at the night sky. With his new best friend sleeping on the floor next to his bed and his sister keeping his secrets, Tal feels a deep sense of contentment. He looks up at the faint, glowing arch of the Rings of Aratta visible in the sky, feeling that familiar spark of divine yearning. He vows to one day unlock his mana, become a true delver, and see the wonders of the world—blissfully unaware of the deadly trials that are rapidly approaching.


**Scene 4: A Scuffle in the Mud (Meeting Wicket)**
*   **The Bond:** After both boys end up on their backs, covered in mud, exhausted and panting, a passing barge-man yells at them to quiet down. Wicket suddenly recites a hilariously crude, rhyming limerick about the barge-man's mother. Tal bursts out laughing, and Wicket joins in. The hostility vanishes instantly. Tal learns Wicket's dad is at the tavern, leaving the boy to fend for himself. Tal decides right then and there that Wicket is his new best friend.

**Scene 5: Sneaking Home (Resolution)**
*   **The Return:** The sun begins to set. The boys part ways, with Wicket promising to teach Tal a song about a haunted sawmill tomorrow. Tal sneaks back to the Sager house under the cover of twilight.
*   **Elsie to the Rescue:** He manages to climb through a window, but his sweet younger sister, Elsie, catches him. Instead of yelling, she giggles at his black eye and muddy state. She quickly hands him a damp rag and hides his muddy boots under a floorboard so Martha won't see them.
*   **Looking to the Future:** Washed and in bed, Tal listens to the sound of his mother bustling in the kitchen and Simm complaining in the next room. He looks out his small window at the starry sky, rubbing his bruised cheek. He smiles.


**Scene 4: A Territorial Dispute (Meeting Wicket)**
*   **The Truce:** They eventually tire out, both panting and covered head-to-toe in foul-smelling mud. Wicket makes a biting, sarcastic comment about Tal looking like a "swamp-goblin." Tal laughs. Wicket laughs. 
*   **The Introduction:** The tension breaks. Wicket introduces himself, explaining he just moved to town. Tal splits his stolen chunk of bread with him. In the span of ten minutes, they go from mortal enemies to blood brothers. Wicket nervously asks if there are actually monsters in the nearby caves; Tal enthusiastically promises to show him. 

**Scene 5: Taking the Lumps**
*   **Sneaking Home:** The sun begins to set. Tal knows he can't hide forever and sneaks back home with Wicket trailing behind, fascinated by his new brave friend. 
*   **The Ambush:** Tal tries to slip through the front door, but little Elsie is waiting. She tries to hide him behind her tiny frame, but it's useless—he smells like a swamp. 
*   **The Punishment:** Martha descends upon him. Wicket watches from the window as Tal bravely takes his scolding and his extra chores without complaining. Tal glances out the window and shoots Wicket a muddy grin. 
*   **Closing Note:** Tal reflects that while his mother’s punishments were a terror in his youth, and the town was small and mundane, having a best friend made it all feel like the start of a true adventure. It was a perfect, cozy life... right up until the night they found the dead man in the graveyard.

"""
