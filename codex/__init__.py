from models.codex import CodexEntry

litrpg_elements = CodexEntry(
      title="LitRPG Elements of This Story",
      content="""While we have RPG-style stats in this story, there is no "system", no quests, no achievements, or any other gamelike elements. Stats are more of a "natural philosophy" attempt to measure a person's abilities.
There is magic, but not too many people can use it. Those who can are often able to objectively measure stats. The major attributes are physical, mental, and magical. Each attribute has five stats measuring the power, control, speed, capacity, and recovery of that attribute.
The physical attributes are Might (Power), Finesse (Control), Agility (Speed), Endurance (Capacity), and Vigor (Recovery).
The mental attributes are Intellect (Power), Focus (Control), Wit (Speed), Memory (Capacity), and Lucidity (Recovery).
The magical attributes are Essence (Power), Dominion (Control), Alacrity (Speed), Vessel (Capacity), and Resonance (Recovery).
"""
)

_entries: list[CodexEntry] = [
    litrpg_elements,
]


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
