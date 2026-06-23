import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for the rest of chapter 3. Here's the basics I have in mind:
The chapter is close to done, but we need to worldbuild a smidge.
The purple moon changes colors based on the type of magic that is "in ascent". Purple is a bad omen, because necromantic magic is stronger. Maisie doesn't understand the different types of magic, but she knows her Mum and Da always feared the purple moon. She's still sad about her parents' death, of course. Banjo should try to comfort her, and while she can't hear him she can appreciate the waggy dog.
We should briefly describe the village and show how isolated it is. There isn't even a major road. Trip can comment on it and Maisie can explain her clan wanted to live somewhere free of elves and elf-friends. Trip is surprised by this and asks about it. She says elves rule everything, and only elf-friends own the good land. How is it you don't know that? Trip says there are no elves where he's from. She comments that it must be heaven.
They can reach the church, only to be blocked by raiders. They're strangely peaceful, having surrounded it. As bestial as the gnolls are, Trip would expect them to be trying to break down its door. Instead, a tall figure in dark robes seems to be directing them.
That's probably a good cliffhanger for the end of chapter three.
"""

"""
Trip and Banjo are in the Bannoch region of the Corvish Isles. They don't know this and won't learn it right away.
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
