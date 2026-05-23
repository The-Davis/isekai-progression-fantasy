import sys
sys.dont_write_bytecode = True
from models.character import Character


toby_henderson = Character(
    name="Toby Henderson",
    description="""A 28-year-old logistics manager for a shipping company in Cleveland, Ohio. Toby seems like the sort of person determined to do his 9-to-5, pay off his Honda Civic, occasionally date someone, and eventually die in a predictable manner.
    He dreams of adventure, but he's too practical (and risk averse) to actually go looking for it. If life's a journey, he's just along for the ride. Or he was. When the crew of the *Sunk Cost Fallacy* drag him along on their planar voyage, he's suddenly very interested in the idea of real aventure.
    Toby is entirely out of his depth in the planes but possesses a highly practical mind for organization and problem-solving.
""",
)

vex = Character(
    name="Vex",
    description="""A cynical, chain-smoking Ozkura who makes a meager living writing a frequently-incorrect and often-exaggerated travel log on behalf of the Neophyte's Guide to the Planes.
    After spending a year on Earth, Vex is eager to return to the planes.
""",
)

jacicus = Character(
    name="Jacicus",
    description="""The dashing, outrageously dramatic captain of the *Sunk Cost Fallacy*.
""",
)

yorrick = Character(
    name="Yorrick",
    description="""The ship's spell-mechanic is a floating, glowing skull containing the soul of a deeply anxious, hyper-caffeinated dead wizard.
""",
)


_characters: list[Character] = [
    toby_henderson,
    vex,
    jacicus,
    yorrick,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
