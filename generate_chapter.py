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

After his shouting and waving fails to draw his father's attention, Tal begs Cord to row him out to meet the barge before it docks. Cord obliges and pushes the skiff back into the water. Wicket eagerly jumps in, swept up in Tal's excitement and happy to be included.
As Cord rows them toward the barge, Wicket comments that he can see why Tal's excited to see his pa if he's the sort of man who doesn't get sore for losing such nice boots.
This prompts Tal to look down at his feet. The river swallowed one of the boots he stole from Simm. He's only wearing one. He didn't even notice in all the excitement of pulling Wicket out of the water.
His father's impending arrival brings a sudden wave of shame. Tal reflects on how  destroying his brother's prized boots to save his own skin was a petty and spiteful thing to do. Alas, the older narrating Tal reflects, he didn't learn quite the right lesson at the time. At the time, all he worried about was the fact that coming home with *one* ruined boot meant his crime would be obvious, and his father would be disappointed.
Wicket manages to get the story out of Tal, who tells about Simm, the mud, and the botched plan to drown the evidence. Wicket listens, and his eyes light up with mischief and he announces he can fix it if Tal gives him the remaining boot.
When Tal hands it over, Wicket immediately chucks it over the side of the skiff. It sinks instantly into the Varn.
Tal is horrified and demands to know how destroying the other boot helps anything. Wicket explains that now, Tal can go home and look his mother and brother in the eye, and *truthfully* claim that the new boy in town threw Simm's boots into the river, and that Tal gave him a whooping.
Tal appreciates the audacity of the half-truth. He could leave out the order of events and let his mother her draw her own conclusions. The older narrating Tal reminds the reader again that he was a rascal, and it would take time before he started remembering the proper lessons of his first life.
As they pull alongside Long Tom's barge, the narrative zooms out with a warm, nostalgic closing thought of that being how Tal met Wicket Tully and established the pattern of life for several years. It all changed the year of the murder.

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
