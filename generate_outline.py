import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section ="""Let's work out the outline for chapter ten. This will deal with Trip, Banjo, and Sydney resolving the standoff with the dragoons, meeting the clan laird, and getting help for the unnamed village.
I think this should cover it, but see if it needs anything more, please:
While Father Sydney tries to broker peace, it doesn't get the dragoons to give in. Trip is moved by the priest's words and decides to deescalate. He leans into his new "Fenshire" identity and claims that over a gun to a stranger is a severe breach of manners where he comes from.
He offers a compromise: he'll unprime his pan and hand over his powder horn. A gun without powder is just a club, and Corvish dragoons ain't afraid of a man with naught but a club, are they?
With their courage on the line, the dragoons grudgingly accept this display of good faith, though they also take Trip's bag of shot.
They are escorted the rest of the way to Glenrowan. Banjo trots alongside the cavalry horses, critiquing the dragoons' to Trip and providing running commentary.
They arrive at a fortified manor house sitting on the outskirts of a mid-sized town and surrounded by a small military camp. We get a little slice-of-life scene: soldiers cleaning muskets, campfires, the drone of distant bagpipes, and the smell of roasting meats. Banjo nearly loses his mind at the scent of the mess tents.
They are brought into the manor house and presented to Laird Lachlan MacTavish. The Laird is barrel-chested, mutton-chopped, eating a hearty stew, and blending aristocratic authority with rustic Bannish charm. Unlike the dragoons, he recognizes and respect's Father Sydney's position, though he doesn't know the man personally.
MacTavish is sympathetic to the village's plight, but deploying his dragoons is a risk. He explains that gnolls hit his own lands and many surrounding farms, and he fears it may happen again.
He interrogates Trip, testing the man's mettle. He tries to browbeat Trip, but Trip's lack of modern deference—meeting the Laird eye-to-eye and speaking plainly—wins MacTavish's respect.
Trip describes the necromancy. MacTavish stops eating. Sydney confirms the use of violet moon magic. 
MacTavish realizes this isn't a mere raid but an Everdark incursion. He orders the dragoons to saddle up.
MacTavish fishes a thick chunk of venison from his stew and tosses it to Banjo, praising the dog's markings. Banjo instantly declares MacTavish the greatest human alive (next to Trip).
The laird notes the poor quality of Trip's musket and asks if he's a marksman. Trip says that he usually hits what he aims at, but without proper rifling he can't do much at range. MacTavish proudly reports that he has some of the new Strohl-Martin rifles (a Corvish equivalent to the Baker rifle), which is highly accurate but slower to load. He suggests that Trip carry one on their foray.
Lachlan offers Trip and Father Sydney horses. Trip admits he's no rider, but the priest gives him a basic lesson. The laird and the two men ride out with twenty dragoons to save the glen, just as the sun begins to set.
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
