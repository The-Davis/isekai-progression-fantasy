import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Presently, the dragoon returns with one of the house servants, who takes over the escort. They are presented to Laird Lachlan MacTavish. The barrel-chested, mutton-chopped man is seated at a heavy oak table in some sort of dining hall, enthusiastically devouring a bowl of hearty stew.
At first, he acts a little haughty, but he recognizes Father Sydney's collar and affords the priest proper respect. He calls for chairs and food and starts treating Sydney and Trip like guests. Banjo despairs when he isn't offered anything.
Sydney graciously declines hospitality and begs for the dragoons to relieve their village. Lachlan sighs and explains that Glenrowan and its surrounding crofts were also hit hard by gnolls. He is reluctant to risk his cavalry by sending them across the open moor when he might need them to defend his own walls tonight.
Sydney warns that there is far worse lurking near the chapel of ease. He asks Trip to tell what he witnessed. Trip describes the dead gnoll they had to drag out into the sunlight. Father Sydney confirms the beast was animated by violet moon magic.
Lachlan drops his spoon. The stew is forgotten. He realizes this isn't just a bold pack of Everdark scavengers at all. This is an incursion driven by necromancy. He immediately launches a prayer in the Elvish tongue and invokes Saint Michael in Latin, then bellows for his lieutenants. As soon as they arrive, he orders them to have the dragoons to saddle up at once.
While barking orders, Lachlan fishes a massive, dripping chunk of venison from his soup bowl and tosses it to Banjo, praising the hound's handsome blue-tick markings. Banjo snaps it out of the air, swallows it whole, and instantly declares Lachlan the greatest human alive (second only to Trip). Lachlan says he likes hounds and wonders if Banjo is available to stud. Banjo asks what that means. Trip prefers not to explain, and politely turns down the request for now, seeing as they have a village to save.
The excitable clan laird agrees, matters of hunting and hounds can wait when there's fighting to be done. He notes the poor quality of the smoothbore militia musket Trip is carrying. He asks if Trip is a marksman. Trip replies with his usual modesty, noting he usually hits what he aims at, but without proper rifling in the barrel, he can't promise much past fifty yards.
Lachlan proudly reveals that he recently acquired a crate of Strohl-Martin rifles. He explains that the grooved barrel makes it deadly accurate at long range, though it takes a fair bit more elbow grease and time to load. He offers one to Trip, seeing as his dragoons are poorly suited to the long barrel. Trip promises to put it to good use. He does find it to be a fine weapon, close in weight to his granddaddy's Winchester, though still only a single-shot muzzle loader.
The courtyard is a flurry of organized chaos as twenty dragoons mount up. Lachlan offers horses to Trip and Father Sydney.
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