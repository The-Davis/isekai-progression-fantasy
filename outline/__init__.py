import sys
sys.dont_write_bytecode = True
from models.outline import Outline


act_one = Outline(
    title="Act One",
    content="""Chapter One: After waking up completely naked on the muddy banks of the River Varn, Trip is promptly arrested by the local constabulary for vagrancy and indecency. Because Trip cannot pay his fines, he is placed on the indenture block. He is first assessed on his stats, and we learn about them. We also find that Trip *cannot* speak of where he's from, but he doesn't know why. There's a void in his head for how he got here.
Chapter Two: The indenture auction is a bit of theater. A group of HUMAN ACTIVISTS make a show of trying to buy him to strike a blow against non-human supremacy and start a bidding war. Ultimately, a wealthy NOBLE wins the bid. Trip learns he's essentially a slave due to his new five-year indenture contract.
Chapter Three: Trip and his new master travel from Dornon to the noble's estates. Along the way, Trip realizes that fighting against legal indenture will only get him killed. He decides to keep his head down and treat this like a long-term contracting gig. Shorlty after this epiphany, the noble's carriage is attacked.


Social Gains: Trip is integrated into the household of the ELF NOBLE and is formally introduced to the NOBLE'S SON, taking his first steps into the complex hierarchy of Corvland’s elite.
Challenge Overcome: Surviving the profound shock of arriving naked in a brutal fantasy metropolis, navigating the dehumanizing auction block, and keeping his temper in check.
Issue Set Up: The HUMAN ACTIVISTS who lost the bidding war take note of Trip and the ELF NOBLE, setting up a simmering racial and political tension in the background.
"""
)

act_two = Outline(
    title="Act Two",
    content="""
"""
)

act_three = Outline(
    title="Act Three",
    content="""
"""
)

_outline: list[Outline] = [
]


def get_outline() -> list[Outline]:
    global _outline
    return _outline
