import sys
sys.dont_write_bytecode = True
from typing import Optional


class Outline:
    def __init__(self, content: str, title: Optional[str] = None):
        self.title = title
        self.content = content

    def prompt_entry(self) -> str:
        return f"{self.title + str("\n") if self.title else str()}{self.content}"
