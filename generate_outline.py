import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for the rest of chapter 2. Here's the basics I have in mind:
the lawmen aren't quite as superstitious as the shepherds, but some of them see Banjo as a devilish familiar given how well he minds Trip (despite mental grumbels to him protesting the choice of not fighting). One of them decides to shoot Banjo to be on the safe side.
Trip slams into the man, throwing off his shot, and Banjo gets away. Another lawman shoots Trip. We demonstrate the first "hands on" magic when one of them pulls out a healing potion and patches Trip up. Thhis should be a wonder and a marvel to Trip, but nothing special to the guards.
They haul him off to the Glenrowan jail to face the justice of the peace for vagrancy, assaulting a peace officer, and trafficking with devils. He is given a horse blanket to wear in the meantime.
Lachlan is our justice. He hears the testimony of the lawmen, decides the case is cut and dry, and finds Trip guilty of vagrancy and assault. Trip tries to claim the dog is just a dog, not a devil. Lachlan looks like he's about to find Trip guilty of this anyway, but instead he asks if any of the lawmen have evidence of devilry. When none is forthcoming, he decides to hold that verdict in abeyance and discuss sentencing.
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
