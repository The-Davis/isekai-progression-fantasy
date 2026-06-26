import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter 4. I don't know precisely what we're going to do, but I do have goals I need to accomplish:
We need to get Trip, Banjo, and the kids inside the church. We need action and danger. We need to show heroics and introduce the Vicar.
I'm thinking we keep it simple: they near the church, and Banjo disobeys Trip, saying he'll never outrun those coons. Banjo turns and charges them. Trip almost drops Dougal to go help his hound. He loves that dog, but he always takes care of people before animals. Always.
Trip will get Dougal and Maisie inside and find the Vicar asleep. Maybe drunk? I want the Vicar to have a small moral failing that will make him feel guilty for failing to raise the alarm. He'll work to redeem himself, helping Dougal and ringing the church bell to rouse the village.
Trip will grab a pair of muskets and go to help Banjo. He kills two gnolls, gets Banjo into the church, and they bar the door.
We can keep the chapter brief and action-packed, then have a brief chance to rest in the next chapter, build the world a bit, and introduce more of the litrpg and fantasy elements.
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
