import sys
sys.dont_write_bytecode = True
from models.outline import Outline


act_one = Outline(
    title="Act One",
    content="""


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
    act_one,
    act_two,
    act_three,
]


def get_outline() -> list[Outline]:
    global _outline
    return _outline
