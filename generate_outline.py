import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for the rest of chapter eight. This will deal with Trip, Banjo, and Sydney crossing the moor from this unnamed village to the larger town of Glenrowan.
I think this should cover it, but see if it needs anything more, please:
We do a quick summary of their remaining preparations (among them being Trip getting a new tricorn hat, because I like tricorn hats), goodbyes to the kids, and the townsfolk planning to bring the outlying crofters into the village and set up barricades for the coming night.
Afterwards Trip, Banjo, and Father Sydney set out across the rugged Bannish moorlands. The morning air is crisp, and the sweeping glens are beautiful but desolate. Banjo is happily trotting ahead, sniffing out grouse and complaining that they don't have time to stop and hunt them.
Trip presses Sydney on why he lied to the village chief about his origins. Sydney explains the grim reality of Rhule (this world): Elves rule. Elves view Outworlders as existential threats. The last time a large group of humans from Earth arrived (the British East India Company, 400 years ago), they brought black powder and firearms, violently disrupting the elven magical supremacy and allowing Corvland to carve out a free kingdom on the Corvish Isles.
Elvish influence has crept back over the isles. Nowadays, if the elves or their human sympathizers ("elf-friends") learn Trip is an Outworlder, they will likely send assassins. Trip agrees to play the part of a "southern frontiersman" to keep his head attached to his shoulders. Sydney suggests he pretend to be from Fenshire, a boggy land with fewer than five hundred occupants. He's very unlikely to meet anyone from there to spot him as a fraud.
We do a quick summary of some other important facts. The Canthican Church upholds the religion of Christ. It's been here on Rhule for close to two thousand years. It was outlawed by the elves until Corvland declared independence and legalized it. Restrictions on the religion eased after that, but the Church continues to protect and help Outlanders in defiance of the elves. This help must be kept secret.
Trip asks about the attributes the priest and the kids kept talking about. Sydney explains that it's a sort of formalized "natural philosophy" to gauge physical, mental, and magical abilities. The elves can measure attributes through rituals. The Church can do readings as well. Mostly, the only way to improve attributes is through hard work, but there are some magical means of enhancement. Father Sydney has never witnessed the latter.
We summarize how they chatted a bit more, mostly focusing on Corvish terms and customs so Trip could blend in as a man of the fens. As it's approaching noon, the fog on the moor, which should have blown away, suddenly grows thicker.
Banjo's hackles go up. He warns Trip that he smells wet fur and bad meat. The air grows unnaturally cold. 
Out of the mist step three massive shapes. Father Sydney recognizes them as Cu-Sith (or Black Dogs)—magically warped hounds native to the moors, the size of calves, with glowing red eyes. Banjo squares up, barking a challenge at his demonic counterparts, and the massive beasts lunge just as the chapter ends.
"""


"""Let's work out the outline for the next few chapters:
The rest of the story is going to be episodic, "cozy violence" that mixes "A Soldier's Life" with "Sharpe's Rifles": no-system, stats-lite LitRPG with a loop of action, power ups, loot, socializing, and slice of life set in a Napoleonic/Georgian era of tech and conflict.
Trip and Banjo need to wind up as scouts (well, one scout who has a dog) in the Corvish military, but that hasn't been introduced, so we need to get them to the military.
I plan to have them help Father Sydney cross the moor and get help from the military's dragoons at the local laird's manor.
After doing so, Trip will return with an army detachment to rescue the village and then they join up to do some good.

I figure we have two to three chapters of material to finish up this act:
1. (the rest of chapter 8) Mostly crossing the moor, but covering things about this world Trip needs to know, including rule #1: don't let an elf, elf friend, or anyone who might gossip to the others know you're an Outworlder. They should also run afoul of something on the moor that they can't handle and cliffhang the chapter on that. An ogre? A pack of black dogs?
2. Get rescued by a few dragoon scouts and escorted the rest of the way to the manor, then meet the laird and gain his trust and aid.
3. Ride back with the dragoons and arrive just in time to crush the gnoll warband at twilight, causing the necromancer to retreat into the Everdark. It may be a future threat.
"""

write_file(generate_outline_prompt(next_section=next_section))
