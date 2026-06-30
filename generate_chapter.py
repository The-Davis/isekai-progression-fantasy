import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Down in the basin, Hamish and Bider John's makeshift barricades are already under assault. There are even more gnolls than before. Worse, a pile of gnoll corpses (the militia is clearly hard at work) is glowing with a sickly violet light. The dead are beginning to twitch and rise. The necromancer must be there now, but where?
Well behind the gnoll lines stands a figure shrouded in dark robes, channeling purple light from a twisted staff. Trip squints through the gloom. He can't tell if it's a mutated gnoll, an evil human, or—as he jokes to the reader—a flock of ducks standing on each other's shoulders in a trench coat. He concedes the ducks are unlikely, but on a world with elves, dwarves, and hyena monsters, he's ruling nothing out.
Laird Lachlan MacTavish draws his saber, ready to lead a thunderous charge down the hill. However, the dragoons' horses are tossing their heads, showing the whites of their eyes, and refusing to advance. Lachlan grunts in frustration, explaining that horses are highly sensitive to necrotic magic. Some are newly trained and might break formation if forced to charge into that violet aura. They will likely lose a few men in the charge.
Trip steps up, patting his new Strohl-Martin rifle. He volunteers to take out the "head of the snake." Lachlan is skeptical—the necromancer is surrounded by a dozen elite, heavily-muscled gnoll bodyguards. A squad of line infantryman could take them. In daylight, perhaps Trip could manage to pick them off at a distance.
Trip explains he's spent his whole life hunting, mostly at night. He and Banjo can slip right through the dark and he can pick the necromancer off at a distance, even if there were no moon. If the gnolls catch wind of him, well... that's what Banjo's for. Lachlan agrees to give him ten minutes, then he'll chance a charge anyway.
Trip and Banjo slip into the heather, bypassing the main assault. Banjo's incredible nose detects the scent and location of the gnoll sentries, and he guides Trip to an ideal spot to get the drop on them. Trip uses all his hunting skills to move silently. This should be tense. He knows he can take out one with his fine new rifle, but he won't have time for a second shot. He wasn't quick reloading the smoothbore musket, there's no way he'll manage the tricky rifle if the bodyguards charge him.
Trip finds a rock formation jutting out of the heather about a hundred yards from the necromancer. It's hard to climb up into it, but it's a great perch. Thanks to the glowing magical aura of the being, he can see it clearly. He rests the heavy octagonal barrel of the rifle on the stone and takes aim.
He quickly realizes a problem: if he fires, the the flash and smoke will instantly give away his position, and the bodyguards will tear him apart before he can reload or extract himself and flee. He shares this problem with Banjo.
Banjo happily volunteers to solve the problem. He compares it to baiting an angry bear. He promises to make a ruckus they can't ignore so Trip can shoot.
Banjo darts out of the brush, crosses the gap between Trip's position and the bodyguard perimeter, snaps at a gnoll's heels, and takes off. He draws most of the furious gnolls away from the necromancer. It isn't all of them, but Trip decides to chance the shot.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.





*   **Taking the Shot:** Trip tunes out the noise of the battle, steadying his breathing just like his granddaddy taught him. He aligns the iron sights on the center of the robed figure's chest, breathes out, and squeezes the trigger.
*   **The Impact:** The Strohl-Martin roars. The heavy lead ball hits the necromancer dead center. The figure is thrown violently backward, its staff clattering to the rocks. 
*   **The Retreat:** To Trip's shock, the necromancer doesn't die. A flare of violet light (a magical *Essence* shield or unnatural *Endurance*) seems to have absorbed the worst of it. However, its concentration is completely broken. The undead gnolls instantly collapse back into lifeless heaps of ash and bone. Clutching its chest, the wounded necromancer scuttles away into the Everdark. Trip feels a cold knot in his gut—he just made a powerful enemy, and he knows they'll cross paths again. 

**Scene 5: The Rout**
*   **The Charge:** With the necrotic magic broken, the horses calm instantly. Up on the ridge, Lachlan bellows a Bannish battle cry, and the dragoons thunder down the hill.
*   **Breaking the Horde:** The regular gnolls, already panicking because their leader fled and their undead meat-shields collapsed, are completely shattered by the heavy cavalry charge. It's a glorious, one-sided clash of Corvish steel and black powder against disorganized monsters.

**Scene 6: The Aftermath and the Cover Story**
*   **Reunion:** Trip climbs down from his perch, rejoining a very smug Banjo who is demanding payment in the form of treats for his flawless distraction.
*   **Victory at the Barricades:** They meet up with Hamish, Bider John, and Father Sydney at the village barricades. The village is battered but saved. There is much back-slapping and camaraderie amidst the lingering gunsmoke.
*   **The Laird's Measure:** Lachlan rides up, dismounts, and heartily offers Trip a pull from his silver flask of fine Bannish whiskey. The laird is thoroughly impressed by Trip's stealth and marksmanship. 
*   **Talking Stats:** Lachlan asks Trip what his *Finesse* and *Agility* stats are, assuming they must be incredibly high to pull off that maneuver. Trip, remembering Sydney's cover story, casually takes a sip of whiskey and admits he doesn't actually know. "Up in Fenshire, we don't do much in the way of testing. A man's worth is what he can do, not a number."
*   **A Job Offer:** Lachlan laughs, accepting the "rustic Fenshire" excuse perfectly. He advises Trip to get himself formally tested by the Church or a coda-glass scholar, noting that the Corvish Army pays very well for marksmen of his caliber. He extends an open invitation for Trip to join his retainers once the dust settles. 


"""