import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Banjo is enthusiastic about the prospect of breakfast. Back in the vestry, the exhausted children are resting, but they are eager enough at the prospect of food as the priest breaks out some rations for everyone. Banjo relishes these but the children find unappetizing. Trip tucks in without complaint: calories are calories, and his body is starving.
To cure Trip's shivering, Father Sydney goes through a militia chest in the vestry. He apologizes for not seeing to it sooner, but so much has happened so fast. At least with the sun rising, they'll have a respite until the next evening. Gnolls almost never attack in daylight. The chest is stocked with more emergency supplies. Trip is overjoyed to finally put on some clothes: a thick green-and-brown flannel shirt, sturdy woolen breeches, and heavy leather boots (which, thankfully, fit his now-healed feet).
Trip feels like a new man, but Dougal and Maisie find his outfit hilarious. Dougal points out that wearing tight Corvishman breeches instead of a proper Bannish kilt is restrictive, confidently stating that "a proper man needs to let himself air out." Maisie thinks he looks like a prancy southerner, so no one will suspect his Might attribute of being as high as it must be, given how fierce a fighter he is.
Banjo chimes in, noting that while Trip still smells a bit like a dead possum, at least he no longer looks like a plucked chicken.
Outside, there are shouts in the village. Father Sydney unbars the heavy front doors to greet a handful of armed villagers who have finally mustered. The gnolls are entirely gone; they have retreated with the sun, confirming they are nocturnal raiders.
There are some introductions. Trip meets Hamish, a burly militiaman who also serves as the village chief. Also among the arrivals is Bider John, a gruff, practical man who serves as the church's porter (guard of the door) and Sydney's assistant. He's ashamed he wasn't there to help defend the church, but he'd been tending to a sick widow on a farm a mile away and had defended the place all night. Trip is impressed by the man, as is Banjo.
In a small comical aside, Father Sydney learns Trip's full name and the fact that "Trip" is just short for "triple", as in "the third" in "Wayne Coberly III". Hamish comments that he's never heard of such a nickname. Trip thinks to explain his origin as an Outworlder, but to his surprise Father Sydney interrupts him and redirects the conversation. Trip holds his tongue, figuring he can ask the priest why later.
Trip learns a bit more about the Canthican structure here: Father Sydney is only a Vicar, not the parish priest. Because the population is so spread out, this church serves as a "chapel of ease" for locals who can't hike to the main parish building miles away, where the parish priest holds Mass.
As the locals come in, Bider John surveys the damage. He is dismayed by the ruined altar, the shattered windows, and the collapsed crypt, but Sydney firmly tells him the building served its holy purpose by protecting the flock.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.


**Scene 4: The Violet Moon's Curse**
*   **Planning the Relief:** Trip, Father Sydney, and a burly militiaman named Hamish begin discussing how to safely check the outlying farmsteads for survivors. 
*   **The Interruption:** Bider John calls out in a panic from the center aisle. One of the gnolls—specifically the dazed one Trip had brained with a rock at the end of the battle—is twitching.
*   **The Undead:** The group rushes over. The gnoll's head is caved in, yet it is dragging itself across the floor, its eyes burning with a sickly violet light. Maisie’s earlier warning about the violet moon "bringing back the worst beasties" is realized. 
*   **The Struggle:** Father Sydney is horrified, recognizing the taint of Everdark necromancy. They realize they need to get it into the sunlight. It takes Trip, Hamish, Bider John, and Father Sydney to drag the thrashing, unnaturally strong corpse out the front doors onto the steps.
*   **The Exorcism:** Even in the sunlight, the creature snaps and snarls. Father Sydney reaches into a small golden pyx he carries, retrieves a consecrated Canthican communion wafer (the Host), and shoves it into the beast's snapping jaws while invoking Saint Michael. The undead gnoll immediately shrieks, combusting into a pile of foul-smelling gray dust.
*   **Comic Relief:** Banjo, having watched this with great interest, telepathically asks Trip if he can have one of those magic crackers. Upon seeing the gnoll turn to dust, Banjo quickly withdraws the request, deciding he's not *that* hungry.

**Scene 5: The Road to the Laird**
*   **The Dire Truth:** The mood turns grim. Father Sydney explains that gnolls are normally cowards; for them to attack in such numbers, and for the dead to rise, means a powerful Everdark villain or necromancer is driving them from the shadows. Hamish dourly admits the local militia can handle regular gnolls, but they can't fight an army of monsters that refuse to stay dead.
*   **The Plan:** Their only saving grace is the daylight, but the violet moon will rise again tonight. Father Sydney announces they need professional soldiers. He will travel to Glenrowan to petition Lachlan MacTavish, the clan laird, who has a company of dragoons attached to his estate. If the dragoons can't handle it, they can send word to the larger city of Wodenburgh.
*   **The Volunteers:** Trip, feeling responsible for Dougal and Maisie and wanting to see this through, volunteers to escort the priest. Plus, it gives him a chance to have a long walk to ask Father Sydney about this world, his magic translated speech, and how LitRPG stats actually work. Banjo agrees to go, mostly because he assumes a "Laird" is someone who has a well-stocked kitchen.
"""
