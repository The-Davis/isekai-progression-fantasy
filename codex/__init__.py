from models.codex import CodexEntry
from codex.corva import corva_entries
from codex.religion import religion_entries

litrpg_elements = CodexEntry(
      title="LitRPG Elements of This Story",
      content="""While we have RPG-style stats in this story, there is no "system", no quests, no achievements, or any other gamelike elements. Stats are more of a "natural philosophy" attempt to measure a person's abilities.
There is magic, but not too many people can use it. Those who can are often able to objectively measure stats. The major attributes are physical, mental, and magical. Each attribute has five stats measuring the power, control, speed, capacity, and recovery of that attribute.
The physical attributes are Might (Power), Finesse (Control), Agility (Speed), Endurance (Capacity), and Vigor (Recovery).
The mental attributes are Intellect (Power), Focus (Control), Wit (Speed), Memory (Capacity), and Lucidity (Recovery).
The magical attributes are Essence (Power), Dominion (Control), Alacrity (Speed), Vessel (Capacity), and Resonance (Recovery).
"""
)

fantasy_elements = CodexEntry(
      title="Fantasy Elements of This Story",
      content="""This world is geographically similar to ours, but is populated by many fantasy races. The elves are dominant in the "Europe" and "Asia" equivalent areas. Orcs dominate Ifria, the "Africa" equivalent areas. Goblins, gnomes, halflings, dwarves, and most other vanilla fantasy creatures can be found.
Rarer are other more fantastic monsters you'd find in the D&D SRD. The really "out there" types, like Tieflings and Genasi, do not exist. Stick with stuff that'd be at home in 80s D&D or Tolkien.
"""
)

_entries: list[CodexEntry] = [
    litrpg_elements,
] + corva_entries + religion_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
