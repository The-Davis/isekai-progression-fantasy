from models.codex import CodexEntry


druthi = CodexEntry(
    title="Druthi",
    content="""The Druthi are a race of humanoids with elvish features. They are known for their love of the dramatic, their emotional outbursts, and their reliably unreliable codes of personal honor.
""",
)

ozkur = CodexEntry(
    title="Ozkur",
    content="""The Ozkur are a race of gray-skinned humanoids with some vaguely elvish and orcish features. They are known for their odd birth rates (70% female), their culinary kleptomania, and their rambunctious nature.
    Ozkuro (males) tend to keep herds of Ozkura (females), who themselves flit in and out of a male's care as they please. Most Ozkura settle down with their male after their first child is born, but some never do.
""",
)


races_entries: list[CodexEntry] = [
    druthi,
    ozkur,
]
