import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section ="""Let's work out the outline for chapter nine. This will deal with Trip, Banjo, and Sydney crossing the moor, discussing attributes, from this unnamed village to the larger town of Glenrowan.
I think this should cover it, but see if it needs anything more, please:
Father Sydney explains the atrributes as a natural philosophy of measuring capability. He explains that trained clerics and mages can use a specialized lens (a "coda glass") or specific diagnostic spells to measure a person's raw capabilities on a standardized scale.
He explains the 3x5 grid: Physical, Mental, and Magical attributes, each measured by Power, Control, Speed, Capacity, and Recovery (e.g., Might is Physical Power, Endurance is Physical Capacity).
The average adult human baseline is around 10, representing a healthy but lazy adult. People who work hard can easily double that, while athletes and trained soldiers are often triple. Sydney suggests that Trip's Physical stats are likely in that range, as he fights with such ease.
Banjo completely misunderstands the concept, insisting his "Snack Capacity" is at least a hundred, and arguing that "Snooze Recovery" is the only metric that matters for a working hound.
Throughout this, Trip pays attention and asks relevant questions. He learns the theoretical maximum is 100, but this is exceedingly rare. A paragon among elves might have Finesse of 100, while the hardiest dwarf might have Endurance of 100, but both are unlikely for either and nigh impossible for humans. Trip is interested that dwarves are a thing. He knows such things appear in books and fairy tales on Earth, and he wonders if other beings out of tales are on Rhule.
One thing learned through questioning is that while the typical way to increase these attributes is through rigorous hard work, aging, and training, there are rumorsthat the elves have magical means of artificially enhancing attributes. Sydney has never witnessed it and does not know the details.
Give Banjo at least one other thing to comment on during this sequence.
The trip comes to an end when Banjo alerts to a scent. Horses and black powder.
A pair of horsemen crest a hill, cutting off their path. They are rough-looking cavalrymen armed with carbines and sabers. 
The men are in uniform, and Sydney recognizes them as Corvish Dragoons, but they do not know or recognize him. The lead rider demands Trip hand over his musket and submit to being bound for the ride to the Laird. 
Trip reacts poorly to the demand, leading the men to draw their carbines. Banjo moves to Trip's side, a low growl rumbling in his chest. We end on a standoff cliffhanger.
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
