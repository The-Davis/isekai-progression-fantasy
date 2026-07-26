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

To Tal's frustration, Jasper taps the side of his nose and refuses to say. He puts his disc artifact away and starts walking down the road. Tal quickly follows, then takes the lead again towards his house.
He tries to pester Jasper further, asking if he could use the disc. Jasper's good mood remains and he humors Tal's questions, but tells him no. He does tell him about how he got his, by taking it from a shallow dungeon delve near the Rhondda Taf mountains in the west.
Jasper adds that these appraisal tools aren't particularly rare, and Tal could get one of his own easily enough if he took up dungeon delving. If it were a truly unique or highly powerful artifact, the Corvish Crown in Dornon would have confiscated it upon discovery. He admits, albeit grudgingly, that the King's exactors at least pay a fair market price in silver bobs and gold nobs when they expropriate dungeon loot.
As they near the hill where Tal's house sits, Jasper comments on the dense woods and stony cave mouths dotting the hillsides. He drops a tantalizing hint: he didn't come to Larchleah for the fresh air. He's following an obscure snippet of Corvish lore about an unmapped dungeon that could hold an undiscovered artifact. He casually asks Tal if he knows the local woods well, to which Tal eagerly nods, seeing an opportunity for an adventure.
They arrive at the Sager house just as Martha Sager is coming out to dump a bucket of soapy water. Tal presents Jasper and his bags, praying his mother is in a good mood.
Jasper turns up his charm to the maximum. He is exquisitely polite, wipes his boots thoroughly, and praises Martha's tidy home. More importantly, he produces a silver shilling to pay his rent upfront.
Martha is grateful for the coin. Tal notices how her eyes follow it, and he files that away. She directs Tal to haul the bags into the spare room immediately.
The heavy bags finally get the better of Tal as he hauls them up the stairs to the second floor. He stumbles, but to his surprise Simmon comes to help him. His brother rarely does anything nice for him, and Tal uncharitably assumes it's to look good for their mother.
When Tal sets the bags on Jasper's bed, the scholar tosses Tal the promised second copper penny and shoos him out of his room.
Tal rushes outside before his mother or brother can press him to do any other chores. He finds a quiet spot and stares at the two copper coins.
His mind racing, but not on the coins, despite them being more wealth than he's ever seen. The cosmic mystery of the Eidolith has finally been made tangible. He knows magic is real, he knows he needs to awaken a mana core to use it, and he knows there are artifacts he needs to find.
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



"""
