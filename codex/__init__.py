from models.codex import CodexEntry
from codex.corva import corva_entries

litrpg_elements = CodexEntry(
      title="LitRPG Elements of This Story",
      content="""While we have RPG-style stats in this story, there are no quests, no achievements, and very few gamelike elements. There are artifacts which show stats, but these are only measurement of a person's abilities rather than a "scorecard".
Stats can be enhanced through the collection and application of mana, which some people are able to channel into the body. Some do so through meditation, while others force it in with mana crystals.
There are six attributes:
Strength is the body's physical power.
Endurance is how long a body can exert itself and go without rest.
Coordination is manual dexterity.
Quickness is raw physical speed and reaction time.
Focus is how well the mind focuses on a thought or a task.
Willpower is a person's mental power, the "push" that forces magical action to take place, and the resistance against mental attack.
The artifacts to display these stats use the Illusion magic school and are fairly common artifacts from dungeons. Unknown to the mortal denizens of the Rings of Aratta, this is part of the ancient tutorial system that has been defunct for over ten thousand years.
"""
)

fantasy_elements = CodexEntry(
      title="Fantasy Elements of This Story",
      content="""The story takes place on the Rings of Aratta, a series of concentric ringworlds surrounding a star. Our story takes place on a single ring, where many continents populate a ring sea.
Many traditional fantasy races live on this ring. The elves are dominant in the "Europe" and "Asia" equivalent areas (no names yet).
Orcs dominate Ifria, the "Africa" equivalent areas. Goblins, gnomes, halflings, dwarves, and most other vanilla fantasy creatures can be found in their own regions, but they are minor powers at best and not considered dominant.
Humans can be found most everywhere and are dominant nowhere. The only "human" nation is the Corvish Isles, the equivalent to the British Isles.
On the ring where the story takes place, there is an "Everdark", a network of caverns that's basically the underdark, which penetrate to the crust of the ring itself.
The Everdark shallows mostly conform to the continents, but the dark deeps can go under the oceans, and these can even extend to magma and mana veins, which permeate the crust of the ring.
Rarer are other more fantastic monsters you'd find in the D&D SRD. The really "out there" types, like Tieflings and Genasi, do not exist on the ring where this story takes place.
Stick with stuff that'd be at home in 80s D&D or Tolkien rather than in modern "theater kids/sparkle trolls" D&D.
"""
)

"""
Clay, Stone, Lapis, Obsidian, Copper, Electrum, and Orichalcum
"""

_entries: list[CodexEntry] = [
    litrpg_elements,
    fantasy_elements,
] + corva_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
