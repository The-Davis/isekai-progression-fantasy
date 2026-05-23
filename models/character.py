import sys
sys.dont_write_bytecode = True


class Character:
    """Enhanced Character model with additional prompt-crafting features."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def about(self) -> str:
        return f"About {self.name.title()}: {self.description}"
