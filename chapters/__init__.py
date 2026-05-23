import sys
sys.dont_write_bytecode = True
from models.chapter import Chapter
from chapters.act_one import act_one_chapters

_chapters: list[Chapter] = act_one_chapters


def get_all_chapters() -> list[Chapter]:
    global _chapters
    return _chapters
