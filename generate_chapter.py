import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters


def generate_chapter_prompt() -> str:
    output = """You are a creative writing assistant helping me write a chapter of my story.
This is an isekai progression fantasy story with a male protagonist, and a world that's a mix of magical fantasy and Napoleonic War era tech.
We are aiming for a mix of the "Cozy Violent" found in "A Soldier's Life" (AlwaysRollsAOne) crossed with some of the gritty adventure of Sharpe's Rifles.
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



Please write this section following the outline, maintaining consistency with the established world and characters, and using the following writing style:
For style, please use a first person, past tense narrative voice, from the point of view of our narrator, Trip Coberly.
Even in dire circumstances, the tone should be that of a classic adventure with a dash of sincere humor. Use a varied sentence structure.
Employ short, punchy sentences for emotional impact or to punctuate a thought, and contrast these with longer, more complex sentences that weave together description, action, and internal reflection into a single, flowing thought.
When describing settings, characters, or objects, vary between direct descriptions, flowery and poetic ones, and anthropomorphized where comedic timing is appropriate.
In times like these, particularly when making observations about social conditions or inserting some humorous levity, we should draw upon Mark Twain.
In his style, descriptions should be vivid and appeal to the senses but should avoid becoming static or overly dense.
Mix in some archaic turns of phrase, such as "by and by" where appropriate. These should not overwhelm the reader, but should be present frequently enough to lend older-fashioned charm to the prose.
Focus on specific, evocative details to make the world feel tangible and grounded, even when events become mysterious or fantastical.
Dialog is the primary engine for characterization and plot advancement. Each character must possess a highly distinct voice and cadence. If a character's "about" section specifies a speech style, use that. Respect any standard for that character if any appearances are already in previous chapters.
Dialog should be brisk and often witty, featuring clever banter and verbal sparring, especially between the narrator and his best friend.
Use dialog to convey essential background information and history in a dynamic way that feels like a natural conversation rather than an info-dump.
Dialog should sound authentic, employing contractions, interruptions, and hesitations to mimic real speech patterns.
Keep dialog tags largely simple and unobtrusive, allowing the characters' unique voices to carry the interaction.
We should lean towards the wit and sincerity of yesteryear in dialog and avoid modern quips, sarcasm, and irony.
When deciding what details to focus on and which to skim over, consider carefully the details I have provided about the viewpoint character.
Thank you."""
    return output


write_file(generate_chapter_prompt())

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.

"""
