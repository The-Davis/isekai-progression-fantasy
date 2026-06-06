import sys
sys.dont_write_bytecode = True
from models.character import Character


tad_harlan = Character(
    name="Tad Harlan",
    description="""Our viewpoint character, a West Virginia good ol' boy. Thaddeus is a tall, wiry man in his mid twenties. He's an excellent fisherman, decent shot, strong swimmer, and good with his hands.
Tad is very much a modern Andy Griffith type character, full of heart and moral conviction. He's more than happy to goof around with friends and family, but when push comes to shove, he's got a strong backbone and a willingness to stand up for what's right.
Has a tendency to folksy ways of speaking and thinking. "Well... how 'bout that?" is a common phrase he uses.
At the start of our story, Tad is one of only two deputies for the Harte County Sheriff's Office. Think of him as an Andy Taylor in the making.
""",
)

hank_fiddle = Character(
    name="Hank Fiddle",
    description="""Henry is the only other deputy in Harte County. He's a pint-sized man who struts like a banty rooster in full spring plumage.
He's the proudest, loudest, and most officious lawman in three counties, even though he's mostly issuing warnings for "suspicious loitering" (kids fishing) and chasing off bears from trash cans.
He worships his sheriff with almost religious fervor, constantly citing "what the Sheriff would do" while completely misapplying it. He's more than a little jealous of how quickly Tad has risen in the sheriff's esteem, but he's a good man underneath the bluster and poor impulse control.
Hank has some excellent qualities: he's the first one to organize a search party when someone's lost in the hollers and the last one to leave a porch after delivering bad news.
Hank speaks in a high, reedy mountain twang that cracks when he gets excited. He tends to engage in lots of finger-pointing, hitch-pulling, and sudden dramatic spins. He has a habit of sucking his teeth and saying "Well now..." before every pronouncement.
When he's trying to be intimidating he puffs up, sticks his chest out, and rocks forward on his toes until he looks like he might tip over.
""",
)

_characters: list[Character] = [
    tad_harlan,
    hank_fiddle,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
