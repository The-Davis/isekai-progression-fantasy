import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Father Sydney and Hamish begin discussing how to safely check the outlying farmsteads for survivors. Bider John heads into the sanctuary to survey the damage. Feeling a little guilty at the havoc he caused, Trip follows.
The bider ignores Trip's hurried explanation of the makeshift bomb, and focuses his attention on the gnolls. Specifically, he examines the one Trip brained with a rock at the end of the battle. It's twitching, despite having its head caved in.
Banjo comments that that don't look right. Even the most ornery coon shouldn't be moving without a brain to tell it what to do, even if coons is mostly ornery clever rather than proper smart. Indeed, the dead gnoll is dragging itself across the floor. Its dead eyes being burning with a sickly violet light.
Trip recalls Maisie's earlier warning about the violet moon allowing the worst beasties, the dead ones, to come out. Bider John recognizes it as necromancy. He yells at Trip to help him drag it into the sunlight. He also warns him not to let his hound bite it, the flesh of the undead is tainted.
John and Trip struggle with the dead creature. Its claws dig into the stone, and it resists. Yelling for help, they rally Hamish and Father Sydney, and it takes the four of them to drag the thrashing corpse out the front doors onto the steps.
Even in the sunlight, the creature snaps and snarls. Father Sydney reaches into a small golden pyx he carries, retrieves a consecrated Canthican communion wafer (the Host), and shoves it into the beast's snapping jaws while invoking Saint Michael.
Banjo watches this with interest, and asks Trip if he can have a snack since the priest is handing them out. The undead gnoll shrieks as the wafer passes its maw and combusts, quickly reduces to a pile of foul-smelling ash. Banjo quickly declares that he doesn't want a snack that does that to a body.
Hamish is shocked by what he witnessed and doesn't know what to make of it. The two church men are familiar, however. Father Sydney explains that though it is rare, some creatures of the Everdark can use the magic of the violet moon to raise and direct the dead. He thought this to be an unusually large and persistent raid, as gnolls are normally cowards, but if their dead are animated, he fears something powerful is driving them.
Hamish dourly admits the local militia can handle regular gnolls, but they can't fight an army of monsters that refuse to stay dead. He briefly considers evacuating the glen and heading for Glenrowan, which has a wall and a clan laird with proper men at arms. Bider John points out that some folks like Widow MacGregor aren't well enough to travel, and doubtless many took wounds in the night. If they flee, they'll be caught on the open moor when the moon rises tonight.
Father Sydney decides that he will travel to Glenrowan to petition Lachlan MacTavish, the clan laird, for aid. His men at arms includes a company of dragoons. If the dragoons can't defend the glen and put down the monsters, they can at least escort the people as they evacuate.
Trip, feeling responsible and wanting to see this through, volunteers to escort the priest. Plus, it gives him a chance to have a long walk to ask Father Sydney about this world and why the priest wants his Outworlder identity kept secret. Banjo also wants to go, mostly because he assumes a "Laird" is someone who has a well-stocked kitchen.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.

Trip learns a bit more about the Canthican structure here: Father Sydney is only a Vicar, not the parish priest. Because the population is so spread out, this church serves as a "chapel of ease" for locals who can't hike to the main parish building miles away, where the parish priest holds Mass.
"""
