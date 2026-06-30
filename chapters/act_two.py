import sys
sys.dont_write_bytecode = True
from models.chapter import Chapter

chapter_twelve = Chapter(
    title="Chapter Twelve",
    content="""
""",
)
    
act_two_chapters: list[Chapter] = [
    chapter_twelve,
]
