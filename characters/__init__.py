import sys
sys.dont_write_bytecode = True
from models.character import Character


wayne_coberly = Character(
    name="Trip Coberly",
    description="""Our viewpoint character, a West Virginia good ol' boy. Wayne Coberly III ("Trip") is a tall, wiry man in his late twenties.
He's an excellent fisherman, decent shot, strong swimmer, distance runner, hunter, and good with his hands. The latter is how he's made his living, mostly getting by on a piece of land his family's owned since forever and doing contractor work to make ends meet.
Trip's lived in Wirt County (the smallest and least populous county of West Virginia) for all his life.
His morality doesn't always match what's modern. To some ways of thinking, he's downright backwards. Has a tendency to folksy ways of speaking and thinking. He'll often use coloquialisms.
Trip's been single for a while, isn't too close (or ornery or distant) with his family, and only has "buddies" rather than close friends, so when he ended up in the other world it wasn't that big a deal to him. Just one of those things.
He'd might've even enjoyed it if not for the whole indentured servant bit.
""",
)

_characters: list[Character] = [
    wayne_coberly,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
