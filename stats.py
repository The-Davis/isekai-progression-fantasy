import sys
sys.dont_write_bytecode = True
from story import current_story
from chapters import get_all_chapters

title = f" {current_story.title}" if current_story.title else ""

print(f"Have been writing{title} for {current_story.work_time()}.")
if get_all_chapters():
    for chapter in get_all_chapters():
        print(f"  {chapter.title}: {chapter.get_word_count()} words")
    print(f"Word count is {sum([chapter.get_word_count() for chapter in get_all_chapters()])}")
