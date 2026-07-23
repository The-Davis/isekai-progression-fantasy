import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from constants import STORY_DESCRIPTION


def generate_character_prompt() -> str:
    output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.\n
{STORY_DESCRIPTION}
You are an expert in this genre and have a deep understanding of storytelling and worldbuilding techniques.
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
    
    output += """Your task is to brainstorm a new character for this story.

The first major plot point in this story involves a murder that Tal and the other boys witness in secret.
We need to flesh out the murderer. He's going to be the source of the boy's nightmares throughout the story. "Goblin" Dob has a proper name, (Mr. Dobbin to those who bother to remember), but most people just call him Goblin.
He's an ugly, mean-spirited logger who many people think is half-goblin. With his bandy legs and crooked limbs, this might be true. The loggers tolerate him because he's an excellent topper (he can climb like a squirrel). Pretty much everyone else in town hates him.
He enjoys picking on children. He ends up murdering Jasper Moray for an artifact and framing Old Man Hollis for it.

Let's come up with:

The character's name and basic appearance
A one-sentence summary of the character's storyline
The character's motivation (what does he/she want abstractly?)
The character's goal (what does he/she want concretely?)
The character's conflict (what prevents him/her from reaching this goal?)
The character's epiphany (what will he/she learn, how will he/she change?
A one-paragraph summary of the character's storyline
Please propose a character that fills this role and fits into the the world I've provided.
No need to go into too much detail. He's more than scenery, but not by too much.
Include a dozen alternate names, please.
Thank you."""
    return output


write_file(generate_character_prompt())

"""

Injun Joe
Joe is the primary antagonist in The Adventures of Tom Sawyer, and is described as a "half-breed", being mixed Native American and white. At Dr. Robinson's request, he, Muff Potter, and Robinson visit the town cemetery one night to steal a body from a grave. Injun Joe then kills Robinson to settle an old grudge and frames Potter for the crime, unaware that Tom and Huck have witnessed it. When the case comes to trial, Tom testifies on Potter's behalf and identifies Injun Joe as the actual killer, prompting Joe to flee the courtroom. He and another confederate later find a hoard of stolen gold and hide it in a cave, where Tom briefly encounters him while trying to find a way out with Becky Thatcher. After Tom and Becky escape the cave, Becky's father has it sealed; Injun Joe is later found just inside the entrance, having starved to death.

Judge Thatcher
Although Judge Thatcher plays a minor role in The Adventures of Tom Sawyer, he plays a substantial role in The Adventures of Huckleberry Finn. Judge Thatcher shares responsibility for Huckleberry Finn with the Widow Douglas, and it is to Judge Thatcher that Huckleberry Finn signs over his fortune in order to keep it from his father.

Mr. Dobbins
The hated schoolmaster at Tom's school, who has taken the job after failing to become a doctor. He is easily angered and is described as "short-tempered." He is a victim of a plot by his pupils, who secretly paint his bald head gold while he is napping and then use a cat to remove his toupee during a public display of his pupils' knowledge. When Becky Thatcher accidentally tears a page in Mr. Dobbins' anatomy book, Tom takes the blame and receives a spanking in her place, winning her admiration.
"""