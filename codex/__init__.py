from models.codex import CodexEntry
from codex.races import races_entries

_entries: list[CodexEntry] = [
] + races_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
