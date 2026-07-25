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

Chapter three opens in the chaotic rush of the churning water, right where chapter two left off. The freezing water shocks Tal's adult sensibilities back into his ten-year-old brain, and his reincarnated instincts keep him from panicking. He's a strong swimmer, and he fights his way to the surface. He gasps for air as he breaches.
Just as Tal breaks the surface, a sturdy oar extends toward him and a friendly voice calls out in greeting. It's Cordin, the cooper's son, one of Tal's friends in the logging town. (Note: Cordin is about a year older than Tal, so roughly 11 in this chapter).
Cord was out fishing in a small skiff, and he hauls the sputtering Tal over the gunwales. Cord is amused by his catch. He went fishing with a pole, but all he caught was a beanpole. Tal grins and slugs him in the arm, but then he thinks of the new boy.
Tal scans the water, half-ready to jump back in and finish the whooping he started. When he spots the new boy flailing wildly, he realizes the smaller boy is struggling to stay afloat. He's being dragged down by his waterlogged clothes, and he clearly isn't a good swimmer.
Tal's petty anger vanishes. He and Cord maneuver the skiff downstream and work together to haul a half-drowned, coughing Wicket out of the river.

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


**Scene 2: Truces and River Lore**
*   **Washing Ashore:** Cord rows them to a muddy bank about a mile downstream from the logging town to catch their breath. The adrenaline fades, leaving Tal and Wicket shivering in the mud. Looking at each other—covered in muck, bruised, and nearly drowned over a box of worthless sea glass—the ridiculousness of boyish pride takes over. They share a breathless laugh, and the grudge evaporates. Introductions are made: Talmon and Wicket. 
*   **Worldbuilding Through Superstition:** Wicket, shivering, frantically touches his remaining bone and stone charms, reciting a rhyming Corvish warding song under his breath to ward off "the evil eye" and thank the river for not eating them. 
*   **The Conversation:** Tal, ever curious, asks about the song. Wicket breathlessly explains local folklore—insisting that the river's undertow is caused by the deep, dark vents connecting the Varn to the Everdark shallows, where shadows try to pull boys down to the crust of the ring. Cord rolls his eyes and pragmatically points out that it’s just a fast current, though he concedes that the water *is* unnaturally warm in spots due to deep-crust mana veins warming the bedrock. This brief exchange establishes Cord’s practical localized knowledge against Wicket’s superstitious (but vast) memory of lore.

**Scene 3: The Return of Long Tom**
*   **A Distraction:** Before they can argue further about what lives in the Everdark, a deep, resonant horn echoes across the water. A massive timber barge is laboring *up* the river toward the logging town. 
*   **Joyful Reunion:** Tal recognizes the markings and, more importantly, spots the tall, broad-shouldered figure of his father, "Long" Tom Sager, at the tiller. Tal is overjoyed—his father's returns are rare and mark a time of celebration and plenty for his family.
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
