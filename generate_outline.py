import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section ="""Let's work out the outline for chapter eleven. This will deal with Trip, Banjo, and Sydney resolving the standoff with the dragoons, meeting the clan laird, and getting help for the unnamed village.
I think this should cover it, but see if it needs anything more, please:
The dragoons arrive at the ridge overlooking the village at dusk. The barricades Hamish and Bider John built are under heavy assault by a massive horde of gnolls and a pile of their bodies are glowing with violet magic and starting to twitch. In the back line stands an indistinct creature in a dark robe, sending purple light from a staff into the pile.
Lachlan prepares for a heavy cavalry charge down the basin, but notes how horses are easily spooked by dark magic. It'd be a whole lot better if that necromancer were destracted. Trip volunteers to take out the magic-user.
Trip and Banjo slip through the dark, bypassing the main horde. We see the synergy of Earth-hunting tactics applied to fantasy warfare. Banjo causes a distraction by tearing through the necromancer's bodyguard while Trip sets up a sniper position. He uses his new rifled musket, takes a breath, and puts a lead ball cleanly through the necromancer's chest.
It doesn't fall, but its magic fails. The undead gnolls collapse into lifeless ash and bone, while the wounded necromancer flees into the night. Trip feels certain it will return eventually. Not for any particular reason, he just knows it in his gut. The regular gnolls panic, moreso when Lachlan and the dragoons thunder down the hill and break the horde in a glorious clash.
The aftermath is full of camaraderie, smoking powder, and back-slapping. Hamish and the village are saved. Lachlan MacTavish shares a flask of good whiskey with Trip. He asks Trip about his attributes, which Trip admits he doesn't know. He improvises the excuse that Fenshire doesn't do much in the way of testing. Lachlan suggests he get himself tested. If his attributes are sufficient, there's a future for a man of his talent in the Corvish Army.
"""


"""Let's work out the outline for the next chapters:
The rest of the story is going to be episodic, "cozy violence" that mixes "A Soldier's Life" with "Sharpe's Rifles": no-system, stats-lite LitRPG with a loop of action, power ups, loot, socializing, and slice of life set in a Napoleonic/Georgian era of tech and conflict.
Trip and Banjo need to wind up as scouts (well, one scout who has a dog) in the Corvish military, but that hasn't been introduced, so we need to get them to the military.
I plan to have them help Father Sydney cross the moor and get help from the military's dragoons at the local laird's manor.
After doing so, Trip will return with an army detachment to rescue the village and then they join up to do some good.

I figure we have two to three chapters of material to finish up this act:
1. Covering the stat system and finishing the moor crossing, only to run headlong into a social challenge involving the laird's men that cliffhangs/hooks the next chapter.
2. Get escorted the rest of the way to the manor, then meet the laird and gain his trust and aid, largely social challenge again.
3. Ride back with the dragoons and arrive just in time to crush the gnoll warband at twilight, causing the necromancer to retreat into the Everdark. It may be a future threat.
"""

write_file(generate_outline_prompt(next_section=next_section))
