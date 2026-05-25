import sys
sys.dont_write_bytecode = True
from models.character import Character


tad_harlan = Character(
    name="Tad Harlan",
    description="""Our viewpoint character, a Kentucky good ol' boy. Thaddeus is a tall, wiry young man. He's an excellent fisherman, decent shot, strong swimmer, and good with his hands.
Tad is very much a modern Andy Griffith type character, full of heart and moral conviction. He's more than happy to goof around with friends and family, but when push comes to shove, he's got a strong backbone and a willingness to stand up for what's right.
Has a tendency to folksy ways of speaking and thinking. "Well... how 'bout that?" is a common phrase he uses. After being enslaved as a pit fighter, his primary drive is to get free, find his brother and friends, and return home.
""",
)

chuck_harlan = Character(
    name="Chuck Harlan",
    description="""Tad's older brother. Bigger and stronger than Tad. Chuck works in construction. He's got easygoing mountain charm and is protective of Amy.
""",
)

amy_whitaker = Character(
    name="Amy Whitaker",
    description="""Chuck's girlfriend. Feisty, practical, good with animals and first aid. Country girl who can bait her own hooks and field-dress a deer. She was born and raised on a Kentucky horse farm.
""",
)

sadie_kline = Character(
    name="Sadie Kline",
    description="""Amy's friend. Pretty, kind, and sharp-tongued when upset.
""",
)

jacicus = Character(
    name="Jacicus",
    description="""Jacicus is tall and slender, with onyx-dark skin. His ears are long and sweep back like polished obsidian knives. He possesses striking, crimson-tinted eyes that seem to capture and hold any ambient light.
He dresses in ostentatious, dark gothic finery: a high-collared coat of violet silk trimmed with silver thread, and a breastplate of blackened steel chased with delicate bone filigree.
He moves with theatrical grace, as if always performing for an invisible audience.
Jacicus embodies the classic Druthi duality of dramatic refinement and casual cruelty. He is prone to dramatic sighs, elegant gestures, and flowery speeches.
When Tad kills two of his Ozkur crew members, Jacicus treats it as a tragic but beautifully violent "performance," mourning the loss of his "rebellious but costly" crew while simultaneously appreciating Tad's physical potential. 
He views his slaving operation as a refined curation of exotic talent. He is polite, even charming, to his captives—right up until they resist, at which point his demeanor shifts instantly to sadism.
His mental magic allows him to touch a captive's mind, quickly absorbing their language. This is how he is able to speak to Tad and his group. The knowledge of the language fades over time, and he must reacquire it occasionally.
Jacicus can also craft suppression runes and forge "thrall collars." These collars suppress the magical and mental essences of his captives, making them docile and easy to manage. He also has a combat variant which uses punishment rather than docility.
Jacicus serves as the introduction to the wider, harsher multiverse. He represents the refined, dangerous civilizations of the planes. By treating the Kentucky kids as "wares" rather than people, he immediately establishes the stakes of the setting.
""",
)

clothis = Character(
    name="Clothis",
    description="""This bone-pale Druthi woman is the helmswoman of the *Maw*. She is responsible for navigating the void, tearing open "slips" between worlds, and keeping the crew alive during transit.
Clothis is incredibly thin, almost skeletal. Her hair is shaved close to her scalp, revealing tattooed containment runes etched directly onto her skull. She wears tight-fitting robes designed for utility rather than fashion.
Because of the immense strain of interfacing with the anima core, her eyes have become milk-white and clouded, though she "sees" the flow of magic and the void far better than anyone else.
Clothis is quiet, detached, and neurotic. Spending countless hours plugged into the *Maw*'s anima core has left her disconnected from ordinary mortal concerns. She speaks in disconnected sentences and rarely engages with others.
She is not actively cruel like Jacicus; rather, she is utterly indifferent to the suffering of the cargo, viewing them as nothing more than ballast.
""",
)


_characters: list[Character] = [
    tad_harlan,
    chuck_harlan,
    amy_whitaker,
    sadie_kline,
    jacicus,
    clothis,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
