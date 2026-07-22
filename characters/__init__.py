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

tom_sager = Character(
    name="Long Tom Sager",
    description="""While he only makes brief appearances in the story, Tal's father, "Long" Tom Sager, is an important figure in Tal's life. The man works as a barge-man for the loggers of their town.
He is usually downstream with a load of timber. The times when he returns are times of plenty and celebration for the Sager family.
Tom is the source of Tal's height. He is not a particularly intelligent man, and he has little wisdom to pass on to his sons, but he does his best to set a good example of industry, sober living, and kind authority.""",
)

martha_sager = Character(
    name="Martha Sager",
    description="""Tal's mother is the primary source of Tal's domestic conflict before the murder plot kicks in. She is the one catching him sneaking out, assigning him chores as punishment, and constantly comparing him to his more compliant (and rival) older brother.
When Tom is away on the river, she is the unquestioned ruler of the roost. However, beneath her scolding exterior is a woman who will defend her children and who worries that Tal's brilliant mind will get him killed in a world that doesn't take kindly to ambitious commoners.
**One-Sentence Summary of Martha's Storyline**:
Martha is a stern and overworked matriarch ruling her meager household with an iron hand. She tries everything she can to discipline her daydreaming middle son into accepting a safe, honest life on the logging barges, only to realize she must let him go when he proves he is meant for a life beyond the river.
**Martha's Motivation (Abstract)**:
She wants security, moral uprightness, and stability for her family. Martha is driven by an anxious love for her children. Deeply practical and fearful of the deadly perils of the wider world, she believes that hard work, strict discipline, and staying safely within their social station are the only ways to keep her children alive and out of poverty. She loves Tal fiercely, but expresses that love through scolding, chores, and trying to keep him grounded.
**Martha's Goal (Concrete)**:
She wants to squash Tal's foolish dreams of magic and adventuring before they get him killed. She wants to force him to behave, stop wandering off to explore caves and ruins, and accept his place working on the river alongside his father and older brother.
**A few extra flavor notes to keep in mind**:
*   **The Wooden Spoon:** Martha rules the roost with a heavy sigh and a wooden spoon. She constantly suspects Tal of mischief (usually correctly) but feels a pang of guilt whenever she has to punish him.
*   **Hidden Softness:** Though she complains endlessly to her neighbors about her "wayward, yellow-haired trial of a boy," she is secretly proud of his sharp wits and is terrified of anything bad actually happening to him. 
*   **Domestic General:** With her husband away on the barges for long stretches, Martha bears the load of keeping the children fed, clothed, and out of the river, which hardens her demeanor.
""",
)

simmon_sager = Character(
    name="Simmon Sager",
    description="""Simmon, or "Simm", is Tal's smug, rule-abiding older brother who relishes his role as the "perfect son" and constantly attempts to get Tal in trouble.
**Simm's Motivation (Abstract)**:
He desires approval, stability, and a sense of superiority over his younger brother. Lacking Tal's imagination and secretly intimidated by the world, Simm embraces the life of the logging town because it offers a clear hierarchy where he can succeed simply by doing as he is told.
**Simm's Goal (Concrete)**:
He wants to secure his place as his father's reliable right-hand man on the logging barges, and he actively looks for ways to tattle on Tal—ensuring their mother catches Tal in every rule-breaking scheme so Simm looks better by comparison.
""",
)

elsie_sager = Character(
    name="Elsie Sager",
    description="""Elsie is Tal's sweet-tempered and loyal younger sister who  serves as his biggest cheerleader and moral anchor. Her unwavering belief in his innate goodness pushes him to actually become the brave hero she already thinks he is.
**Elsie's Motivation (Abstract)**:
She wants harmony, love, and joy within her family. She possesses a deep well of empathy and a romanticized view of the world that aligns with Tal's dreams. She wants to see the good in everyone and desperately wants her family to stop arguing.
**Elsie's Goal (Concrete)**:
She wants to protect her favorite brother from their mother's wooden spoon by helping him finish his chores and hiding his muddy boots from their mother's sight. She eagerly awaits the stories he brings back from his secret explorations of the local ruins and caves.
""",
)


"""

"""

_characters: list[Character] = [
    talmon_sager,
    tom_sager,
    martha_sager,
    simmon_sager,
    elsie_sager,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
