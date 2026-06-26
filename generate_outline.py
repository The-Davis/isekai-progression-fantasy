import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter 5. I don't know precisely what we're going to do, but I do have goals I need to accomplish:
We need to introduce the stat system to Trip and Banjo, preferably through organic conversation. Perhaps a comment from the the kids to Father Sydney about Trip's prowess leading to Sydney asking about Trip being tested and Trip admitting he doesn't know what that means.
We can make it clear through this interaction that outworlders like Trip are known to the church, but it's a bit of a secret. Sydney probably takes Trip out of earshot of the kids, perhaps to tend to his injured feet (and Trip would insist on getting Banjo taken care of as well).
We need to establish that outworlders coming to this world (Rhul) is a known phenomena. Usually, they come in numbers and are very disruptive with the new knowledge they bring. Once, centuries ago, nearly a hundred men from the "British East India Company" arrived together, bringing knowledge of firearms that seriously upset the balance of power. It's why the Corvish kingdom exists at all instead of being yet another elvish realm.
We can also establish that the "Corvish" language is English with a slight drift, but the written language is the odd flowing script of the elves. No one writes with Latin letters. Sydney explains that the elves cursed that alphabet to suppress knowledge from the other world. Write anything with them, and the paper will rot away in seconds.
We also establish that Trip's origins are not something he should talk about. King Calador is only half-elf, but he shares the elvish loathing of offworlders (mostly thanks to the East India Company's disruption, but also because the Canthican church is such a disruptive religion), so nobles seeking his favor would likely have Trip imprisoned or worse. Sydney cautions Trip to hide his nature. This will be a later source of anxiety and danger for Trip, since he doesn't know this world and will have to come up with a believable cover story.
Stats have potential maximums and current ranks and are on a 0 to 100 scale. Magic exists and is part of everyday life, but not too many people can simply wield it. Trip can deduce that his bond with Banjo is some sort of magic, but he can't figure out how to control it.
That's a lot of material to cover, and we can do it while Sydney tends to their wounds. We can use that to establish that while healing potions exist, they're saved for life-threatening injuries. Trip's wounds, once healed, get bound with a sort of healing glue that binds the skin together to heal on its own.
We should cut the infodump off with Banjo warning that he smells the big coons again. The door is intact, but Trip hears their yipping somewhere, growing louder. Father Sydney says they must have found the tunnel. We'll use that as a chapter cliffhanger: the gnolls have broken in.
"""

"""
We can keep the chapter brief and action-packed, then have a brief chance to rest in the next chapter, build the world a bit, and introduce more of the litrpg and fantasy elements.

Trip and Banjo are in the Bannoch region of the Corvish Isles. They don't know this and won't learn it right away.
This is where we reveal the stat system and Lachlan's motivation. If Trip has high enough stats and potential stats, he could serve in the army. If he qualifies for one of the king's elite units, he could be Glenrowan's entire levy for the year.
1. 

4. 
Trip tests high enough to qualify for army service. His physical stats are enough to qualify for dragoon or ranger training. We can world build and discuss the army roles here. Trip, being a hunter, gravitates towards the rangers.
Lachlan strikes a bargain: serve as Glenrowan's levy, and he will be found not guilty of trafficking. The sentence for the other two crimes will be his first year's wages in the army.
Trip asks what the sentence would be otherwise. Lachlan reveals the stick to the earlier carrot: trafficking is a capital crime. He'd have to be shipped to a proper magistrate in Wodenburgh for sentencing, where he'd face anything from mutilation and transportation to death by hanging.
When Lachlan puts it that way, Trip accepts. He's locked up for the night and will be shipped off to the army in the morning.
Throughout this chapter, he should get a mental tugging telling him Banjo isn't far, but he can't hear the hound's thoughts. This builds up some of the limitations of their bond and keeps Banjo in mind.
"""

write_file(generate_outline_prompt(next_section=next_section))
