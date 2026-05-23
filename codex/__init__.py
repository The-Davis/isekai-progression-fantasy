from models.codex import CodexEntry

_entries: list[CodexEntry] = []


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
