import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Not too long afterwards, they find themselves looking down into the village. Trip is immediately struck by how primitive and isolated it looks. There are no paved roads, no phone or power poles, not even a wide wagon track connecting it to the broader world.
Trip remarks on how deep in the sticks they are. Maisie explains that her clan purposefully settled in this harsh, remote Highland valley to be far away from the "elves and elf-friends." 
Trip is bewildered. "Elves? Like the fellas making toys at the North Pole?" Maisie looks at him like he's crazy and explains that the elves are terrifying, powerful beings who rule the mainland and dictate terms to the King. The human nobles who kiss up to them—the "elf-friends"—get all the rich, fertile, rolling green lands down south in Corvland. The Bannish Highlanders are shoved into the freezing mountains because they refuse to bow.
Trip says that's news to him. He'd never even heard of an elf where he's from. Maisie looks up at him with wide eyes and whispers, "Nae elves? Ye must come from Heaven itself, Mr. Trip."
As they near the village outskirts, navigating between dark, silent stone cottages, Banjo suddenly freezes. His hackles rise stiff as a wire brush, and he lets out a low, rumbling growl that Trip can feel in his mind.
Banjo warns that the smells are changing. Trip asks if it's more gnolls. Banjo confirms that it is, but there's something else, something like a root cellar that ain't been opened in a hundred years, or maybe a meat locker. Cold dirt, old blood, and dried bones. Ain't no living critter smells like that, Trip.
Trip tells Banjo to stay quiet. No baying at it. Banjo grumbles that sneaking is for cats and a proper hound announces his business. But alright, we'll do it your way, boss.
The trio creeps to the edge of the village square, hiding behind a low, mortarless stone wall. Trip peers over the top to get a look at the church. 
The church matches Maisie's description. It's a sturdy, imposing stone building with a heavy slate roof and stained glass windows, looking like a fortress of civilization amidst the rustic village. 
The square is packed with gnolls—dozens of them, armed to the teeth and covered in blood. However, they aren't howling, looting, or trying to batter down the heavy oak doors of the church. Instead, they are standing in silence and perfectly still, almost as if they are in a trance. It completely contradicts the bestial nature Trip witnessed at the farmstead.
In the center of the gnoll pack, bathed in the eerie light of the purple moon, stands a tall figure draped in sweeping, dark robes. Even though Trip has never seen the living dead, not once, it's as if his very soul recognizes it for what it is. Undead.
He ducks back behind the wall, realizing they are completely cut off from their only sanctuary.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.





"""
