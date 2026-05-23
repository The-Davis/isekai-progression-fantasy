import sys
sys.dont_write_bytecode = True


class CodexEntry:
    """Generic codex entry with prompt-crafting features."""
    
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
    
    def about(self) -> str:
        return f"About {self.title.title()}\n{self.content}"
