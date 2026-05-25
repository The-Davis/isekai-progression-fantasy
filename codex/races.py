from models.codex import CodexEntry


druthi = CodexEntry(
    title="Druthi",
    content="""Druthi are a race of tall, lithe humanoids bearing elegant, sharply refined elvish features: high cheekbones, pointed ears that sweep back like obsidian blades, and eyes that gleam like polished gemstones or spilled blood under moonlight.
Their skin tones range from corpse-pale alabaster to deep, bruised violets and charcoals, often accented by intricate, scar-like tattoos or ritual brands that tell tales of ancient betrayals and glorious vendettas.
They favor dark gothic finery: velvets the color of midnight, silks threaded with silver spiderweb patterns, and armor of blackened steel chased with bone and gemstones.
Druthi culture is defined by theatrical grandeur and raw emotional volatility. A simple greeting may swell into a sonnet of flattery or a venomous aria of insult.
Their personal codes of honor are elaborate, passionate, and notoriously flexible.
A Druthi might spare a foe for the poetic satisfaction of a later, more spectacular revenge, only to weep genuine tears of regret when the deed is done. This makes them both compelling allies and treacherous partners in the planes' endless games of power.
Beneath the elegance lies a core of calculated cruelty. Straightforwardly malevolent, Druthi revel in domination, exquisite torments, and the slow unraveling of souls.
Many serve as slavers, soul-binders, or planar corsairs, their innate talents for mental magics making them natural masters of the flesh trade and the shadowed courts of distant planes.
""",
)

ozkur = CodexEntry(
    title="Ozkur",
    content="""Ozkur are rugged, gray-skinned humanoids blending elvish grace with orcish brutality. They stand shorter and stockier than humans on average, with males (Ozkuro) often towering over their female counterparts when fully grown.
Their features include prominent tusks or fangs, expressive pointed ears, and skin tones of slate, ash, and storm-cloud gray, frequently marked by ritual scars, piercings, or war-paint.
Ozkur dress practically yet flamboyantly for raiders: leathers, furs, looted finery, and an abundance of knives, hooks, and cooking implements.
Ozkur society revolves around their unusual demographics—roughly seventy percent female births—and their rambunctious, kleptomaniacal nature, especially when it comes to food.
Culinary theft is a competitive sport and social bonding ritual among them; a well-executed pantry raid earns respect, while a failed one invites playful (or painful) mockery.
They are boisterous, quick to fight, quick to laugh, and possessed of a pack-hunter's cunning that serves them well as pirates and raiders across the planes.
Reproductive and social structures are fluid and herd-based. An Ozkuro typically maintains a "herd" of Ozkura, who come and go as they please—joining for protection, adventure, or the raising of young, then departing when the mood strikes.
Most Ozkura eventually settle with one male after bearing their first child, but a significant number remain free-roaming warriors, traders, or raiders all their lives.
Young are raised communally within the herd, learning survival, larceny, and the joys of a good scrap from an early age. This structure produces highly adaptable crews for plane-sailing vessels, where the Ozkur serve as enthusiastic, if somewhat chaotic, enforcers and boarders.
In the wider multiverse, Druthi and Ozkur often form symbiotic (if tense) partnerships: the Druthi provide the elegant scheming and magical finesse, while the Ozkur deliver raw muscle, numbers, and unpredictable ferocity.
Together they prowl the planes in Spelljammer-style vessels, hunting for valuable "wares" and prime stock for the flesh markets of distant realities.
""",
)


races_entries: list[CodexEntry] = [
    druthi,
    ozkur,
]
