from models.codex import CodexEntry
from codex.races import races_entries


sunk_cost_fallacy = CodexEntry(
    title="Sunk Cost Fallacy",
    content="""The *Sunk Cost Fallacy* is a planejammer, a magical ship.

""",
)


_entries: list[CodexEntry] = [
    sunk_cost_fallacy,
] + races_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
