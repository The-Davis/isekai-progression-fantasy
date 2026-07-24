import sys
sys.dont_write_bytecode = True
from chapters import get_all_chapters

if get_all_chapters():
    for chapter in get_all_chapters():
        print(f"  {chapter.title}: {chapter.get_word_count()} words")
    print(f"Word count is {sum([chapter.get_word_count() for chapter in get_all_chapters()])}")
