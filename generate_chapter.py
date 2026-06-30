import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """The two dragoons who initially escorted Trip and Sydney return. Lachlan orders them to fetch their captain and have a score of men saddle up at once.
While barking orders, Lachlan idly takes his soup bowl and sets it in front of Banjo, taking a moment to praise the hound's fine figure and handsome blue-tick markings. Banjo dives into the stew and instantly declares Lachlan the greatest human alive (second only to Trip). Lachlan says he likes hounds and wonders if Banjo might be available to hunt after all this is finished. Banjo begs Trip to say yes. Trip agrees, but says he'd prefer to focus on the village.
The excitable clan laird agrees, matters of hunting and hounds can wait when there's fighting to be done. He notes the poor quality of the smoothbore militia musket Trip is carrying. He asks if Trip is a marksman. Trip replies with his usual modesty, noting he usually hits what he aims at, but without proper rifling in the barrel, he can't promise much past fifty yards.
Lachlan proudly reveals that he recently acquired a crate of Strohl-Martin rifles. He explains that the grooved barrel makes it deadly accurate at long range, though it takes a fair bit more elbow grease and time to load. He offers one to Trip, seeing as his dragoons are poorly suited to the long barrel. Trip promises to put it to good use. He does find it to be a fine weapon, close in weight to his granddaddy's Winchester, though still only a single-shot muzzle loader.
The courtyard is a flurry as twenty dragoons mount up. Lachlan offers horses to Trip and Father Sydney.
Trip sheepishly admits he's a lot more comfortable on his own two feet (or behind the wheel of a truck, though he keeps that part to himself). Father Sydney, surprisingly adept, gives Trip a quick and bare-bones lesson on how to stay in the saddle without breaking his neck.
Banjo bounds eagerly around the horses, ready for a fight. The shadows in the courtyard are stretching long. Trip looks up to see the sun beginning to dip behind the jagged mountain peaks, meaning the yellow and violet moons will soon rise.
With Lachlan at the head of the column, Trip clinging awkwardly but determinedly to his saddle, and Banjo leading the charge, the cavalry rides out of Glenrowan to save the village just as dusk begins to fall.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.






"""