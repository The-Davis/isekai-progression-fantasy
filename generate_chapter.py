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

Tal and Cord maneuver the skiff downstream and work together to haul a half-drowned, coughing Wicket out of the river.
Tal slaps the smaller boy on the back and helps him cough up the water while Cord rows them to a muddy bank about a mile downstream from the logging town.
The adrenaline fades, leaving Tal and Wicket shivering. Looking at each other, they share a laugh, and the grudge evaporates. Introductions are made between the three boys. Talmon and Cord both proudly share what their fathers do. Wicket shares that he just moved into town with his Pap, who means to try his hand at logging. He rolls his eyes as he says this, and Tal gets the feeling that Wicket has a low opinion of his father.
Tal starts to ask about Wicket's mother, but the boy interrupts him to go over to the riverbank. He makes a show of thanking the river for not eating them.
Tal, ever curious, asks what he means. Wicket breathlessly explains the tales he's been told: the river's undertow is caused by vents connecting the Varn to flooded portions of the Everdark, and if the current is just right, it can suck you right down. Wicket claims someone on the barge they rode into town heard there's a spirit of the river that chooses if you get swallowed up or not, and Wicket thought it best to thank her for not eating them. Pay's to be courteous, you know.
Cord disagrees with Wicket and says it's just a fast current, and he's never heard any such tale and he's lived here all his life, eleven years, which is practically forever. Wicket perists that one can't be too cautious with monsters and spirits, and he proudly shows them his necklace of frog bones and river stones, explaining how it protects you from drowning.
Tal and Cord are skeptical. Wicket points out that he didn't drown. They claim it's because they fished him out. Wicket shrugs and says as long as he isn't drowned, that means it works.
Before they can argue further, a horn echoes across the water. A massive barge is laboring up the river toward the logging town, riding high and empty. Tal recognizes the markings and, more importantly, spots the tall figure of his father, "Long" Tom Sager, at the tiller. Tal is overjoyed—his father's returns are a time of celebration for his family.

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


*   **To the Skiff!:** Shouting and waving from the muddy bank, Tal begs Cord to row them out to meet the barge before it docks. Cord obliges, expertly pushing the skiff back into the water. Wicket eagerly jumps in, swept up in Tal's excitement and happy to be included in a family moment he sorely lacks at home.

**Scene 4: The Alibi**
*   **The Realization:** As Cord rows them toward the barge, the initial rush of excitement wears off, leaving Tal to look down at his feet. The river swallowed one of Simm’s stolen, mud-caked boots. He is only wearing one. 
*   **The Guilt:** His father’s impending arrival brings a sudden wave of shame. Long Tom represents kind authority and honest living. Tal realizes that destroying his brother’s prized boots to save his own skin was a petty, spiteful thing to do. Coming home with *one* ruined boot means he can’t even pretend they just went missing—his crime is obvious, and his father will be disappointed.
*   **Wicket’s Fix:** Wicket notices Tal sulking and asks what’s wrong. Tal sheepishly confesses the whole story about Simm, the mud, and the botched plan to drown the evidence. Wicket listens, his eyes lighting up with mischievous genius. "I can fix that, easy," Wicket declares. 
*   **The Toss:** Before Tal can react, Wicket grabs the remaining boot, unlaces it, and cheerfully chucks it over the side of the skiff. It sinks instantly into the Varn.
*   **Boy Logic:** Tal is horrified, demanding to know how destroying the other boot helps anything. Wicket flashes his chipped-tooth grin and explains the beauty of the loophole: Now, Tal can go home and look his mother and brother in the eye, and *truthfully* claim that the new boy in town threw Simm’s boot into the river, and that Tal gave him a whooping for it. 
*   **The Spark of Friendship:** Tal realizes the sheer, brilliant audacity of the half-truth. He didn't say *which* boot the new boy threw in, nor the order of events. Tal's lingering guilt gives way to a wide grin. He realizes this superstitious, curly-haired river rat operates on the exact same wavelength he does. 
*   **Chapter Wrap-up:** As they pull alongside Long Tom's barge to the sound of his father's booming, welcoming laugh, the narrative zooms out with a warm, nostalgic closing thought: *And that was how I met Wicket Tully.*

"""
