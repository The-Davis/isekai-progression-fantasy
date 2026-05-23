import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

style_to_use = main_style + """
The viewpoint character for this chapter is Amabel Clavering.
"""

chapter_outline = """
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=style_to_use))

"""
You can stop there and we'll edit before I provide the next section.

We'll end the chapter on that note.

"""