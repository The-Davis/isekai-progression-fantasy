import sys
sys.dont_write_bytecode = True
from models.character import Character


tbd = Character(
    name="TBD",
    description="""
""",
)


talmon_sager = Character(
    name="Tal",
    description="""Tall, yellow-haired Talmon Sager, known as "Tallow" to his annoyance for his resemblance to a candle, is our viewpoint character.
Tal's first memory, strangely, is of dying and being brought to the Rings of Aratta by a mysterious being. Throughout his youth, he has experienced vague dreams of a warm deific presence urging him to 

**One-Sentence Summary of Tal's Storyline**:
A reincarnated boy with a connection to a forgotten god must overcome his paralyzing guilt over a deadly secret to survive a murderer's revenge and earn his way into a magical academy.

**Tal's Motivation (Abstract)**:
He wants to understand his soul's divine connection and experience the wonders of the world. Driven by subconscious memories of Earth and a mysterious God, he feels alienated by the gods of Aratta and craves a sense of divine purpose, freedom, and exploration.

**Tal's Goal (Concrete)**:
Tal wants to become a delver and escape his destiny of working the logging barges. To do this, he must unlock an ability to channel mana and earn a coveted spot in the kingdom's training lyceum in the capital of Dornon.

**Tal's Conflict**:
**External:** He is trapped by his social station. His father is constantly away on the logging barges, his mother rules their meager household with an iron hand, and his older brother serves as a constant rival. He lacks the money, status, or magical ability to become the adventuring delver he wishes to be. Later, a murderer actively hunting him becomes a highly lethal roadblock.
**Internal:** His instinct for self-preservation and fear of ruining his already slim chances at a future. When he witnesses the murder, his fear causes him to stay silent. He battles immense guilt as an innocent man takes the fall, torn between doing what is right (testifying) and keeping himself and his friends safe.

**Tal's Epiphany**:
Tal realizes one might find adventure through escaping a boring life to seek thrills, but a hero, the sort of man people remember, needs the courage to stand firm against injustice.
He realizes that he cannot run away from danger. He must become an unshakeable rock and take moral responsibility even when he is terrified.

**One-Paragraph Summary of Tal's Storyline**:
Born into a poor family in a riverside logging town on the River Varn, Talmon—known to his adoring little sister and close friends as "Tallow"—spends his days dodging his strict mother, clashing with his rival older brother, and playing protective hero to his adoring younger sister.
His days of cozy riverside mischief and exploring the local sawmills take a dark turn when he and his friends witness a murder and swear a pact of silence out of terror.
Terrified of the killer and fearing they'll be next to keep them silent, Tal and his friends flee town, inadvertently allowing an innocent man to be blamed for the murder.
Surviving the hardships of the wilderness strips away his romanticized views of adventure, forcing an epiphany: he must return to stand against injustice and testify at the trial.
Though his testimony frees the innocent man, the true killer escapes, returning months later to hunt Tal and his friend into a dangerous stretch of the Everdark shallows.
Tal is forced to step into the role of the adventurer he always dreamed of being. Relying on his wits and his friends, he outsmarts his pursuer, using the dungeon's own hazards to defeat the killer.
Emerging battered but victorious, Tal claims the dungeon's undiscovered treasure, thus securing the funds he needs to leave his logging town behind and enroll in Dornon's prestigious training lyceum.
""",
)

"""




Armed only with his wits and his raw, untested magic, Tal turns the dungeon's hazards against the assassin, claiming a hidden cache of treasure that finally secures his passage to Dornon and a seat at the royal training lyceum. 


**A One-Paragraph Summary of the Character's Storyline**

In doing so, he claims the dungeon's treasure, finally securing his ticket to the royal training lyceum in Dornon.
"""


_characters: list[Character] = [
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
