import sys
sys.dont_write_bytecode = True
from models.character import Character

_characters: list[Character] = list()


def get_characters() -> list[Character]:    
    global _characters
    return _characters
