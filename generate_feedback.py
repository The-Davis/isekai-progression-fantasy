import sys
sys.dont_write_bytecode = True
from chapters import get_all_chapters
from util.files import write_file

output = """
I am working on a fantasy adventure story with a working title of "The Neophyte's Guide to the Planes". Have a read:
"""

for chapter in get_all_chapters():
    output += chapter.prompt_entry() + "\n"

output += "What do you think?"
write_file(output)
