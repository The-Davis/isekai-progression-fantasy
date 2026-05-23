import sys
sys.dont_write_bytecode = True
from models.chapter import Chapter

chapter_one = Chapter(
    title="Chapter One",
    content="""
""",
)


act_one_chapters: list[Chapter] = [
    chapter_one,
]
