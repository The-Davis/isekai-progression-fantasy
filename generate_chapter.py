import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Trip tunes out the noise of the battle, aligns the iron sights on the center of the robed figure's chest, breathes out, and squeezes the trigger.
It's like he can follow the path of the speeding ball. It zips across the space of the football field and a half of distance and hits the necromancer dead center. Violet light flares from the impact. Limbs flail, putting an end to the robe full of ducks theory seeing as there's no feathers, and the staff clatters to the ground.
To Trip's shock, the necromancer doesn't die. It scrambles to its feet and starts backing away. Did that flare of light absorb the worst of it? Trip can't really tell, and without the light near the spellcaster, he can no longer make out any details. One good thing has happened: the undead gnolls attacking the barricade collapse back into lifeless heaps. The necromancer scuttles away, leaving Trip with the uneasy feeling that he'll cross paths with this unknown fiend again.
Up on the ridge, Lachlan bellows a battle cry, and the dragoons thunder down the hill. The regular gnolls, already nervous with their leader fled and their undead meat-shields collapsed, are completely shattered by the cavalry charge. It's a glorious, one-sided clash of steel and black powder against disorganized monsters.
Trip climbs down from his perch, where he is rejoined by a very smug Banjo who reiterates that he's no garden variety coon hound. Trip agrees. He and the hound stroll into the village, where they're welcomed like heroes.
Banjo asks if heroes get snacks. Trip, realizing he's been awake since the morning he and Banjo disappeared from Earth, wishes more for a nap. Banjo tells Trip he should prioritize: he himself has taken like, a billion naps since moon got himself a girlfriend. Be more like a hound.
Trip agrees that this is good advice, and sees about finding a place to catch a few winks.
We'll end the chapter on that victorious note, unless you can think of a better way to end it.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.










They meet up with Hamish, Bider John, and Father Sydney at the village barricades. The village is battered but saved. There is much back-slapping and camaraderie amidst the lingering gunsmoke.
*   **The Laird's Measure:** Lachlan rides up, dismounts, and heartily offers Trip a pull from his silver flask of fine Bannish whiskey. The laird is thoroughly impressed by Trip's stealth and marksmanship. 


"""