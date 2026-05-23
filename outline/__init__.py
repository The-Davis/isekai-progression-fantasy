import sys
sys.dont_write_bytecode = True
from models.outline import Outline


act_one = Outline(
    title="Act One (The Departure)",
    content="""We need four to six chapters for act one. This should introduce Toby and his dull job at a Cleveland warehouse. He has no idea about the multiverse or planar travel.
    Enter Vex, a stranded Ozkura who's been on Earth for a few years, writing for the Neophyte's Guide to the Planes. She wants *out* of Earth and back into the planes.
    Captain Jacicus of the *Sunk Cost Fallacy* (a cargo ship) needs a (something) on his quest to find a lost demi-plane. Vex has a lead on it, and she's trading that to Jacicus for passage.
    Toby's company is involved in the shipping of the (something) that Vex is carrying.
    When interplanar pirates attack the *Fallacy* during the transfer, Toby gets swept up in the chaos and ends up on the ship. It departs Earth and heads into the multiverse.
    Vex tries to cheer him up and gives him a copy of *The Neophyte's Guide to the Planes*. Captain Jacicus assigns Toby the role of "Assistant Cargo Warden" to earn his keep. It's an odd role, since there is no Cargo Warden position on the ship.
"""
)

"""
### Act II: The Inner Ring (Fire, Ice, and Bureaucracy)

*   **Chapter 5: The City of Brass (Plane of Fire).** The ship's first stop is the bustling, incredibly hot markets of the City of Brass to deliver a shipment of industrial-grade fire extinguishers (highly prized by safety-conscious efreet). Toby experiences the extreme heat and the local legal system, which is entirely based on contracts written in smoke.
*   **Chapter 6: An Actionable Claim.** Toby uses his logistics background to negotiate their way out of a predatory tariff imposed by a corrupt fire genie. This earns him some respect from Captain Brim, though he almost loses his eyebrows in the process.
*   **Chapter 7: The Frostfell Shortcut.** To evade the githyanki raiders still tracking Vaelen's "conceptual art," the captain takes a shortcut through the Para-elemental Plane of Ice. The ship's sails freeze, and Toby must climb the rigging in a thermal suit designed for warehouse freezers to free the rudder.
*   **Chapter 8: The Boarding Action.** The githyanki raiders catch up. A frantic battle occurs on the deck of the frozen ship. Toby manages to defeat a raider not with magic, but by using a forklift-like loading enchantment in a highly creative, OSHA-violating manner.

### Act III: The Great Void and the Outer Planes

*   **Chapter 9: The Astral Drifters.** The ship enters the Astral Sea, a silver void where thoughts become semi-physical. Here, Vaelen reveals the truth: the "art" they are carrying is actually a stolen beacon that points to a legendary, lost demi-plane created by a forgotten deity.
*   **Chapter 10: Mechanus Customs.** They are pulled over by a patrol of Modrons demanding a safety inspection. The crew must hide Toby (since humans are technically classified as "unregistered invasive fauna" in this sector). Sprocket's caffeinated modifications to the ship's engine nearly cause a diplomatic incident.
*   **Chapter 11: The Pandemonium Layover.** Needing repairs, they dock at an outpost built inside a giant, hollowed-out stone head floating in Pandemonium (the plane of howling winds). The constant noise makes everyone irritable. Toby discovers that his noise-canceling headphones are a priceless artifact in this plane, trading them for a replacement engine part.

### Act IV: The Lost Demi-Plane

*   **Chapter 12: Finding the Pocket.** Following the beacon, the ship navigates a treacherous storm of wild magic to enter the lost demi-plane: "The Archives of the Unimportant." It is a massive, dusty library containing everything ever lost or forgotten in the multiverse.
*   **Chapter 13: The Guardian.** The archive is guarded by a massive, ancient Sphinx who does not ask riddles, but instead demands a complete, categorized inventory of the archive before anyone can leave. The previous visitors have all died of old age trying to solve it.
*   **Chapter 14: The Logistics Solution.** Toby realization: the Sphinx's library is just a poorly organized warehouse. Using basic Dewey Decimal concepts and warehouse inventory methods, Toby reorganizes the entry system in a matter of hours, satisfying the Sphinx's ancient geas.

### Act V: The Return Trip (Sort Of)

*   **Chapter 15: The Escape.** The githyanki leader arrives to claim the archive's power. A final, chaotic battle erupts amidst towering shelves of forgotten history. Toby uses the newly organized catalog system to locate and activate a defensive magical artifact, neutralizing the raiders.
*   **Chapter 16: The New Normal.** With the archive secured, the crew is rewarded with valuable planar maps and treasures. The ship returns to the neutral ports near Earth.
*   **Chapter 17: The Choice.** Toby has the opportunity to return to his quiet life in New Jersey. However, looking at his desk job compared to the vastness of the planes (and realizing he has been offered a promotion to full-time Cargo Warden and co-writer of the next edition of the *Guide*), he decides to stay aboard.

---

## Themes

*   **The Power of Mundane Skills:** 
*   **The Absurdity of the Infinite:** In a multiverse where anything is possible, the most common problems are still bureaucracy, miscommunication, and poor planning.
*   **Home is a Relative Concept:** Toby finds that he feels more at home among an eccentric crew of outsiders than he did in his predictable suburban life.
"""

_outline: list[Outline] = [
    act_one,
]


def get_outline() -> list[Outline]:
    global _outline
    return _outline
