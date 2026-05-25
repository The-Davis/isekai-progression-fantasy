from models.codex import CodexEntry
from codex.races import races_entries


void_keels = CodexEntry(
    title="Void Keels",
    content="""Across the infinite expanse of the planes, travel between realities is rarely a matter of simple portals on solid ground. For those who trade, raid, or explore on a grand scale, the preferred method of transit is the **Void Keel**.
These are specially constructed vessels capable of sailing the chaotic, non-physical currents of the aetherial void that separates the planes.
Because ordinary wood and iron disintegrate under the intense spatial shearing forces of planar transitions, Void Keels are constructed from highly resilient, magically conductive materials. Common hulls are fashioned from the fossilized bones of astral leviathans, dense star-wood harvested from planar borders, or the discarded carapaces of massive deep-void creatures.
The heart of every Void Keel is its anima core, a housing matrix of refined crystal and enchanted alloy. The core acts as a reservoir and converter for anima, the magical life force that permeates the cosmos. Without a functioning core, a vessel is merely a drifting hulk.
Operating a Void Keel requires a highly specialized magic-user, often referred to as a helmsman. This individual must possess exceptionally high scores in magical and mental essences. By interfacing with the core, the helmsman directs the vessel's movement, shapes the ship's defensive wardings, and manifests the wards.
The core continuously projects a protective warding spells which cling to the hull, trapping a pocket of breathable air and generating a subjective down-force (gravity) for the crew. If the wards are breached or the core fails while in the void, the atmosphere quickly dissipates, and the crew is exposed to the suffocating, freezing vacuum of the inter-planar medium.
To move between planes, the helmsman must use the ship's core to tear open "slips", temporary rifts in the fabric of reality. This requires precise calculation and a deep understanding of planar resonance. A failed jump can strand a vessel in the dark spaces between worlds, or worse, tear the ship apart.
""",
)

the_maw = CodexEntry(
    title="The Maw",
    content="""A medium void keel owned and commanded by the Druthi captain, Jacicus. Serving as both a raiding vessel and a secure transport for his living cargo, it is a predatory ship designed for stealth, swift boarding actions, and the long-term containment of his "wares."
The ship is built from the hollowed-out shell of a Gorgon-Nautiloid, a gargantuan, predatory mollusk native to the deep silt-currents of the outer planes. The spiral shell provides natural, segmented compartmentalization, which Jacicus has retrofitted to suit his business. The exterior of the shell is reinforced with plates of blackened steel, and the spiral ridge is lined with defensive iron spikes.
True to Druthi sensibilities, the vessel features dark, elegant trim, polished obsidian railings, and sails made of deep violet silk that absorb the ambient light of the void. To the casual observer, it looks like a sleek, skeletal crescent gliding through the darkness.
The deepest, most curved chambers of the shell serve as the slave pens. Damp, cramped, and heavily warded with suppression runes, these cells are designed to depress the essences of captives, preventing escape attempts.
The mid-deck section contains the crew quarters, dominated by the messy, chaotic communal spaces of the Ozkur raiders. It is cluttered with looted finery, racks of weapons, and drying meat.
The Quarterdeck and Pilot House are situated at the crest of the shell. This elegant pavilion is where Jacicus commands. It is decorated with fine carpets, silver-chased furniture, and trophies from his various acquisitions.
""",
)


_entries: list[CodexEntry] = [
    void_keels,
    the_maw,
] + races_entries


def get_codex() -> list[CodexEntry]:
    global _entries
    return _entries
