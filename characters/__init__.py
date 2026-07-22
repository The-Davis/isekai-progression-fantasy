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

wicket_tully = Character(
    name="Wicket Tully",
    description="""Wicket is Tal's best friend and compatriot. He's Talmon's physical counterpart: short and dark-haired with curls and a sallow complexion.
**One-Sentence Summary of Wicket's Storyline**:
A superstitious, music-loving boy with a deadbeat father is dragged into a deadly murder plot by his adventurous best friend, forcing him to face his deepest fears of magic and monsters to save their lives.
**Wicket's Motivation (Abstract)**:
He desires an escape from his miserable home life. He uses stories, songs, and superstitions as a shield against the world and his father's neglect. Deep down, he yearns for the warmth and stability of a real family, which he vicariously experiences by shadowing Tal and spending time at the Sager household.
**Wicket's Goal (Concrete)**: 
While not afraid of throwing hands against boys twice his size, Wicket wants to survive his childhood without getting eaten by a monster or cursed by a witch, and eventually earn a cushy position as a resident bard in a warm tavern. To do this, he actively tries to talk Tal out of his foolish dreams of magic and delving, hoping to keep his best friend safely grounded in their mundane but familiar hometown.
**Wicket's Conflict**:
**External:** His father is the town drunk, meaning Wicket lives in abject poverty and relies on scraps and the charity of Tal's mother, Martha. Furthermore, he is severely hindered by his illiteracy and inability to do basic math. Later, he is hunted by a very real murderer and forced into the Everdark, bringing him face-to-face with the hazards he has spent his whole life singing cautionary tales about.
**Internal:** His deep-seated superstitions paralyze him whenever magic or monsters are involved. Wicket wears a dozen protective charms (most of them useless junk like river-stones and dried frog bones) and is terrified of the "evil eye." He deeply fears that he is destined to be a worthless, cowardly failure like his father, and worries that when the time comes, his terror will cause him to abandon Tal.
**Wicket's Epiphany**:
He realizes that the legendary heroes in his favorite songs were terrified, ordinary people who stepped forward anyway for the sake of the people they loved. He also learns that the ancient lore, nursery rhymes, and songs he thought were just "tavern fluff" hold practical power in the dangerous world of Aratta, proving he isn't just a useless tagalong.
**One-Paragraph Summary of Wicket's Storyline**:
Wicket Tully is the son of the town drunk, a boy who compensates for his mother's death and his father's neglect by filling his head with every song, myth, and fireside superstition he can memorize from the passing river bargemen.
While he is hopeless at reading or doing basic math, he can perfectly recall a ballad or a piece of local lore after hearing it only once. He acts as a colorful, bardic counterpart to his best friend Tal, though he is terrified of Tal's ambitions regarding magic and the Everdark.
When he and Tal witness a brutal murder, Wicket's terror drives him to beg Tal for their pact of silence, desperate to keep the killer's gaze off them.
When the boys flee into the wilderness, Wicket's superstitions pale in comparison to the very real dangers of starvation. When Tal's conscience demands they return to save a framed man, Wicket reluctantly follows his best friend back into the jaws of danger.
When the escaped killer returns months later and hunts the boys into the magically active, monster-filled Everdark shallows, Wicket is trapped in his literal worst nightmare.
Wicket finally steps out of Tal's shadow; using his perfect recall of an ancient dwarven song about the cavern's echoes, he helps Tal lay a trap that defeats their pursuer, proving he is no coward and earning his own ticket to Dornon alongside his best friend.
**Extra Flavor Notes for Wicket**:
*   **The Superstitions:** Wicket can be a great vehicle for worldbuilding. Instead of info-dumping, you can have Wicket frantically reciting Corvish superstitions: *"Don't whistle near a cave mouth, Tal, you'll wake the knockers!"* or *"Cross your fingers when you mention the Everdark, or the shadows will hear you."*
*   **The Foil to Simm:** While Simm (Tal's brother) is a rule-abiding kiss-up with a stable home who secretly resents Tal, Wicket is a rule-breaking outcast with a broken home who deeply loves Tal. This creates a great dynamic where Wicket is a better "brother" to Tal than his actual brother.
*   **Elsie's Ally:** Because Wicket practically lives at the Sager house to avoid his own father, he and Elsie likely have a very sweet relationship. He sings her the songs he learns on the docks, and she likely sneaks him extra food when Martha isn't looking (though Martha definitely knows and pretends not to notice, feeling pity for the motherless boy).
""",
)

rosamund_winslow = Character(
    name="Rosie Winslow",
    description="""Rosamund Winslow is an elfkin girl who contrasts the muddy, rough-and-tumble of a river logging town. This daughter of a human and a half-elf has inquisitive hazel eyes, faint freckles across her nose that she tries to shade with a parasol, gently-pointed ears from her mother's side, and rich chestnut hair kept in ribbon-tied curls. She favors pristine dresses in pastel blues, yellows, and greens—garments completely unsuited for exploring, though she hitches her skirts up to do just that anyway.
**One-Sentence Summary of Rosie's Storyline**:
The sheltered daughter of the new logging company foreman arrives from the capital, inadvertently inspiring Tal's heroic ambitions while discovering that the rustic "adventures" she romanticizes carry dangerous consequences.
**Rosie's Motivation (Abstract)**:
She desires intellectual freedom, a sense of wonder, and to experience the "romance" of the world. Raised on a diet of imported books and societal expectations, Rosie yearns to step out of the rigid confines of upper-middle-class expectations and experience the unpolished world for herself. She wants to see the magic and history she has only ever read about.
**Rosie's Goal (Concrete)**:
Before her father's temporary contract ends and they return to Dornon, Rosie wants to catalog the local flora, map the nearby shallow ruins, and record the regional folklore. To do this, she enlists Tal and Wicket as her "local guides," treating them as her own personal adventuring party, which gives Tal the perfect excuse to show off, act brave, and spend time with her.
**Rosie's Conflict**: 
**External:** Her status-conscious father keeps her under a watchful eye, explicitly forbidding her from wandering the woods or fraternizing with "river rats" and common laborers. Furthermore, she lacks any practical survival skills; the actual dangers of the wilderness and the Everdark shallows are far more lethal than the sanitized adventures in her books.
**Internal:** She battles her own naiveté and timidity. She likes the *idea* of adventure but is easily frightened by the reality of it. When the town is rocked by the murder plot, Rosie is forced to reconcile her romanticized view of the world with its violent realities, ultimately having to find her own brand of courage.
Extra Flavor Notes for Integrating Rosie into the Story:
Rosie should be the classic feminine ideal for this era—always wearing a clean ribbon in her hair, perhaps playing a spinet piano her father had shipped up the river, and smelling of lavender. Her father treats her as an extension of the status her late mother imparted him, as elves and half-elves are of higher social class than humans. Tal will absolutely try to "show out" for her, walking on fences, doing minor physical stunts and exaggerating his knowledge of the local caves to win her admiration.
*   **Tal's Moral Compass:** Rosie has a very black-and-white view of justice. When Tal is agonizing over his guilt and fear about testifying at the murder trial, Rosie can be the unknowing catalyst for his epiphany. He realizes he can't look her in the eye and pretend to be the brave hero she thinks he is if he lets an innocent man hang. He wants to *be* the man she believes him to be.
*   **Relationship with Wicket:** Wicket probably thinks she's a prissy snob at first, but is quickly won over when he realizes she will sit in rapt attention to listen to his songs and folklore. She might even try to teach Wicket how to write his name, though this should comically fail.
*   **Relationship with Elsie:** Rosie, having no siblings, likely finds Elsie adorable and treats her like a living doll, giving her hand-me-down ribbons or sneaking her sweets from the foreman's pantry. Elsie, in turn, idolizes Rosie and acts as Tal's wing-woman, constantly (and embarrassingly) telling Rosie how great her older brother is.
*   **Martha's View:** Martha Sager would be conflicted by Rosie. On one hand, she demands Tal show the girl the utmost respect due to her father's station. On the other hand, she resents Rosie for putting "airs and foolishness" into Tal's head and making him dream of a life in Dornon that Martha feels he can never safely achieve.
""",
)

clarice_cooper = Character(
    name="Clary Cooper",
    description="""Clarice Cooper is sturdy, healthy, and  pretty in a very grounded way. She has strong, capable hands from working alongside her father (the town's barrel-maker), and thick chestnut-brown hair that she keeps tied back in a messy braid. She usually smells of toasted oats, river-reeds, and fresh sawdust.
**One-Sentence Summary of Clary's Storyline:** 
A pragmatic local girl with a long-standing crush on Tal watches her childhood bond unravel when a wealthy city girl arrives, forcing her to accept that the boy she envisioned a happy future with is destined for a life she cannot share.
**Clary's Motivation (Abstract)**:
She desires stability, community, and the quiet of a life well-lived among her own people. Unlike Tal, who looks at the river and wonders where it goes, Clary looks at the river and is grateful for the life it provides. Having grown up in the same muddy streets as Tal, she values loyalty, shared history, and the comfort of the familiar, believing that the best things in life are built through honest work rather than chasing foolish fantasies.
**Clary's Goal (Concrete)**:
She wants to eventually marry Tal, combine their families' meager resources, and build a comfortable, respectable life in the logging town. She actively tries to pull Tal back down to earth, poking fun at his grand ambitions in hopes that he will outgrow his "delver phase," accept a job on the logging barges, and settle down with her.
**Clary's Conflict:** 
**External:** The arrival of Rosie Winslow, the elfkin girl who captivates Tal and feeds his dreams of magic and adventuring. Clary lacks the money, the delicate beauty, and the worldly education to compete for Tal's attention in the same way. Clary lacks the magic, the wealth, or the desire to follow Tal into the life he desires.
**Internal:** Her pride prevents her from chasing after a boy who is clearly starry-eyed over someone else. She refuses to change who she is, put on "airs," or pretend to care about magic and ruins just to win him back, masking her quiet heartbreak with biting sarcasm and eye-rolling.
**Extra Flavor Notes for Integrating Clary into the Story*:
**Mutual Jealousy:** The dynamic between Clary and Rosie is a great source of friction. Clary is deeply jealous of Rosie's wealth, her pristine dresses, and the way Tal trips over his own feet to impress her. *However*, Rosie is secretly jealous of Clary, too. Rosie envies Clary's easy, unfiltered camaraderie with Tal and Wicket, their shared jokes, and the fact that Clary can effortlessly hike up her skirts and jump across river stones without fear of ruining her clothes or breaking a sweat.
**Wicket's Confidante:** Because Clary is part of their original trio/social circle, Wicket complains to her about Tal's new obsession with Rosie. Clary and Wicket share a mutual exasperation over Tal acting like an idiot for the new elfkin city girl, giving them a fun, commiserating dynamic.
**Martha's Favorite:** Martha Sager absolutely adores Clary. In Martha's eyes, Clary is the ideal match for Tal in her eyes thanks to her work ethic and lack of interest in magic. Martha likely invites Clary over for supper frequently, intentionally trying to push the two together, which deeply embarrasses Tal now that he's trying to impress Rosie.
""",
)

cordin_cooper = Character(
    name="Cord Cooper",
    description="""Corwdin Cooper is Clary's older brother by just eleven months (making them "Galish twins," a Corvish term for siblings born within a year of each other). He shares Clary's sturdy build and thick chestnut-brown hair, which he keeps tied back with a leather cord. He has a quiet gaze and moves with a grace unlike Tal's impulsive energy or Wicket's frantic fidgeting. He wears homespun wool and usually smells of pine resin and damp earth.
**One-Sentence Summary of Cord's Storyline**:
A pragmatic local boy witnesses a murder after being dragged into an adventure by his ambitious best friend, forcing him to use his wilderness skills to keep them alive and realize that protecting those he loves requires facing the darkness he'd rather avoid.
**Cord's Motivation (Abstract)**:
He desires stewardship, localized mastery, and a balance between woodland thrills and domestic peace. Cord loves the idea of delving and adventuring, but only in his own backyard. He feels a connection to the River Varn and the surrounding forests. He doesn't want to conquer the world or see Dornon; he just wants to know every cave, deer trail, and shallow ruin within a ten-mile radius of his home.
**Cord's Goal (Concrete)**:
Cord wants to become the town's premier tracker and woodsman. He wants to map the local woods and the safest upper fringes of the Everdark shallows to harvest magically infused timber for his father's coopering business. He wants to make a respectable living locally so he can stay close to his family.
**Cord's Conflict**:
**External**: The murder rips him out of his comfortable routine. When they are forced to flee into the wilderness, the burden of actually keeping Tal and Wicket from starving to death or being eaten by local wildlife falls on his shoulders.
**Internal**: He battles resentment toward Tal for disrupting their peaceful lives. Cord is torn between his loyalty to his friends and his desire to just stay out of trouble. He struggles with the fact that Tal's boundless ambition and Rosie's romanticized foolishness have brought danger to his family's doorstep.
**Cord's Epiphany**:
Cord realizes that you cannot build a fence around your home and expect evil to respect the boundary. He learns that true stewardship is about protecting the life you love by stepping into the dark to hunt the monsters before they can reach your home. He also learns to accept that letting his friend go is an act of brotherly love he needs to make.
**One-Paragraph Summary of Cord's Storyline**:
While Cord enjoys local delves into shallow caves and ruins, he is frustrated by Tal's obsession with leaving their logging town for the capital. When the trio witnesses a brutal murder, it is Cord's survival skills that keep them alive when they flee into the treacherous wilderness.
The realities of life on the run strain his friendship with Tal, as Cord resents being dragged into a conspiracy that threatens his family and his sister, Clary. However, when Tal decides they must return to free an innocent man, Cord reluctantly steps up as their protector.
In the aftermath, as Tal secures his ticket to Dornon, Cord chooses to remain behind, parting ways with Tal on good terms.
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
    wicket_tully,
    rosamund_winslow,
    clarice_cooper,
    cordin_cooper,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
