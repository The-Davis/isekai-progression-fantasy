import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter 2. Here's the basics I have in mind:
Trip and Banjo have arrived in the Bannoch region of the Corvish Isles. They don't know this and won't learn it right away.
The gnolls (Trip doesn't know what they are, but the hyena-things are gnolls) were raiding a Bannish farmstead. This happens every so often. Trip and Banjo were too late to save most of the farm family, but they'll save the two they've seen so far.
While Banjo fights most of the gnolls (dodging clumsy spear thrusts), Trip grapples one that attacks with a cleaver. Gnolls use weapons and tools, but not well. Their bestial instincts take over. The gnoll keeps trying to bite, getting in close and losing the advantage of its size and the weapon it has. Trip's able to snatch up the weapon from the one Banjo killed, and he kills the gnoll, but not before getting a nasty bite.
The gnolls who have survived go in search of easier prey. It's obvious there are other farms in the area and other victims, as fires blossom in the distance in multiple directions.
We should ease the tension with a smidge of humor between Banjo and Trip and make light of Trip's appearance: nude, covered in blood, breathing like an adrenaline-addled berserker.
Of the two survivors, the girl is fine, but the boy is badly wounded. This is where we can learn that the people here speak English. Or, actually, Corvish, which is practically the same thing. The girl should marvel over how well Trip fought, and speculate on one of his physical attributes (this will worldbuild that they exist and common people know about them, but Trip will just be confused by the term)
Trip notices the brogue and thinks they sound like Scrooge McDuck, so Scottish, or Irish, or whatever he was (Trip's not too educated, after all).
The girl helps Trip get some clothes off the dead raiders. Her father is dead right outside the house. His kilt is about the right size for Trip, but she cries and wails when he suggests borrowing them. He settles on some gnoll loincloths. Other than that, they only wear harnesses and belts, so he doesn't look much better, but at least he isn't flapping in the breeze.
Now equipped, Trip ponders what to do. With all the fires around them and what's clearly a major raid going on, help isn't coming, and the creatures are probably coming back. The boy, though weak, musters enough strength to identify them as gnolls. He suggests making for the church, but he groans and stops talking.
The girl picks up the line of thinking: the church is the only stone building in the village, and the vicar keeps muskets there for the militia. He might even have a healing potion or two. These two mentions will world-build the tech level. Trip doesn't catch on that "healing potion" is something special, but Banjo wonders about it, like if it's the same as the pills Trip's nana used to take (Trip can briefly recall his nana lived with him until her death last year).
Finally, Trip agrees on the church as a destination. He debates briefly with Banjo if the dog should pull the boy on a litter or if Trip should carry him. Banjo makes fun of Trip's senses and says a whole herd of coons could sneak past him. He says it's best to let him scout while Trip carries the kid. Trip grumbles that raccoons don't have "herds" and the creatures aren't racoons anyway, the boy said they're gnolls, but Banjo is already nose to the ground and heading out.
Getting the boy moved safely is the next challenge, and we need a harrowing ordeal for Trip since he still doesn't have proper footwear, even if his everything isn't flapping in the breeze anymore. They can reach the church, only to be blocked by raiders who are trying to break down its heavy door.
That's probably a good cliffhanger for the end of chapter two.
"""

"""
This is where we reveal the stat system and Lachlan's motivation. If Trip has high enough stats and potential stats, he could serve in the army. If he qualifies for one of the king's elite units, he could be Glenrowan's entire levy for the year.
Lachlan brings in the local vicar, who has a relic that can test and record stats. We can use this for several world-building elements:
1. While the "Corvish" language is clearly English with a slight drift, the written language is an odd flowing script. There isn't a Latin letter among them.
2. Stats have potential maximums and current ranks and are on a 0 to 100 scale.
3. Magic and devilry are two different concepts. Magic exists and is part of everyday life.
4. Trip's origins are not something he should talk about. King Calador is only half-elf, but he shares the elvish loathing of offworlders (humanity formed the rebellious Canthican church, after all), so nobles seeking his favor would likely have Trip imprisoned or worse. Lachlan pointedly strikes any mention of Earth and West Virginia from the record (he can't offer Trip up as the town's levy if he's dead) and cautions Trip to hide his nature. This will be a later source of anxiety and danger for Trip, since he doesn't know this world and will have to come up with a believable cover story.
Trip tests high enough to qualify for army service. His physical stats are enough to qualify for dragoon or ranger training. We can world build and discuss the army roles here. Trip, being a hunter, gravitates towards the rangers.
Lachlan strikes a bargain: serve as Glenrowan's levy, and he will be found not guilty of trafficking. The sentence for the other two crimes will be his first year's wages in the army.
Trip asks what the sentence would be otherwise. Lachlan reveals the stick to the earlier carrot: trafficking is a capital crime. He'd have to be shipped to a proper magistrate in Wodenburgh for sentencing, where he'd face anything from mutilation and transportation to death by hanging.
When Lachlan puts it that way, Trip accepts. He's locked up for the night and will be shipped off to the army in the morning.
Throughout this chapter, he should get a mental tugging telling him Banjo isn't far, but he can't hear the hound's thoughts. This builds up some of the limitations of their bond and keeps Banjo in mind.
"""

write_file(generate_outline_prompt(next_section=next_section))
