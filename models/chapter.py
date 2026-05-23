import sys
sys.dont_write_bytecode = True
from typing import Optional

import re


class Chapter:
    def __init__(self, content: str, title: Optional[str] = None):
        self.title = title
        self.content = content

    def prompt_entry(self) -> str:
        return f"{self.title + str("\n") if self.title else str()}{self.content}"
    
    def get_word_count(self) -> int:
        """Get accurate word count for this chapter."""
        # Remove extra whitespace and count words
        clean_content = re.sub(r'\s+', ' ', self.content.strip())
        return len(clean_content.split(' '))
