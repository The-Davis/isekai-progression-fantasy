from models.codex import CodexEntry
from codex.corva import corva_entries
from codex.religion import religion_entries

litrpg_elements = CodexEntry(
      title="LitRPG Elements of This Story",
      content="""While we have RPG-style stats in this story, there is no "system", no quests, no achievements, or any other gamelike elements. Stats are the mortals' attempts to measure a person's abilities.
Stats can be enhanced through the collection and application of mana, which some people are able to channel into the body. Some do so through meditation, while others force it in with mana crystals.
There are six attributes that most philosophies recognize:
Strength is the body's physical power.
Endurance is how long a body can exert itself and go without rest.
Coordination is manual dexterity.
Quickness is raw physical speed and reaction time.
Focus is how well the mind focuses on a thought or a task.
Willpower is a person's mental power, the "push" that forces magical action to take place, and the resistance against mental attack.
"""
)

fantasy_elements = CodexEntry(
      title="Fantasy Elements of This Story",
      content="""The world, Aratta, is geographically similar to ours, but is populated by many fantasy races. The elves are dominant in the "Europe" and "Asia" equivalent areas.
Orcs dominate Ifria, the "Africa" equivalent areas. Goblins, gnomes, halflings, dwarves, and most other vanilla fantasy creatures can be found in their own regions, but they are minor powers at best and not considered dominant.
Humans can be found most everywhere and are dominant nowhere. The only "human" nation is the Corvish Isles, the equivalent to the British Isles, but even then the king is a half-elf.
There is an "endless dark" of caverns that's basically the underdark. The dark shallows mostly conform to the continents, but the dark deeps can go under the oceans, and these can even extend to magma veins.
Rarer are other more fantastic monsters you'd find in the D&D SRD. The really "out there" types, like Tieflings and Genasi, do not exist.
Stick with stuff that'd be at home in 80s D&D or Tolkien rather than in modern "theater kids/sparkle trolls" D&D.
"""
)

_entries: list[CodexEntry] = [
    litrpg_elements,
    fantasy_elements,
] + corva_entries + religion_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
