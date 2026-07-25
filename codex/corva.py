from models.codex import CodexEntry

corvish_isles = CodexEntry(
    title="Corvish Isles",
    content="""The Corvish Isles are the ringworld's version of the British Isles. Corva is the largest of these islands, and it is also called "Corvland".
Corvland is the heart of the Corvish Kingdom and home to the Corvish ethnolinguistic group, which is by far the largest population in the isles. It is a land of rolling green hills, dense oak forests, and sprawling cities.
The capital city of Dornon sits in the northern-central region along the wide, mud-brown River Varn. Corvland is historically the seat of royal power.
The northern part of Corvland is the Bannoch, home to the Bannish ethnolinguistic group. The Bannish Lowlands are industrious, boasting textile mills that rival Dornon's output. Its Highlands are a wild, romantic expanse of sweeping glens, deep, freezing lochs, and jagged, snow-capped mountains.
The mountainous western expanse of Corva is Rhondda Taf, home to the Rhondish ethnolinguistic group. It is a land of deep, rain-swept valleys, jagged peaks, and ancient stone. Rhondda Taf is the mining capital of Corva, and generations of Rhondish men have dug out iron, slate, and coal reserves.
The island of Galidon is often called "The Emerald Isle" for its vibrant greenery. It is the most fertile of the Corvish Isles. Galidon is predominantly agricultural. It produces wool and much of the Kingdom's basic foodstuffs.
"""
)

dornon = CodexEntry(
    title="Dornon",
    content="""The capital city of Corva is Dornon, originally "Dorn-on-Varn", but shortened over the centuries to Dornon. It is situated on the banks of the Varn river.
    It is the largest city on the banks of the Varn river. It is essentially like London at the height of Georgian England.
    Its districts have names like Graymarket, the Clinks, Hearthgate, Thorncross, and Ashmoor. Whenever writing about Dornon, consider using these district names, but do not limit yourself to them.
    Most of these are ancient names that have been passed down for centuries, and the original meaning of the names has been lost to time.
    Many are run down and dangerous, but their denizens take fierce pride in their neighborhoods and are loyal to their own.
    Streets should have charming and interesting names as well, like Binders' Walk and the Red Row.
    The city is a bustling metropolis, with the largest population in the kingdom. It is a center of commerce, culture, and politics, and is home to the Corvish royal family.
"""
)

larchleah_town = CodexEntry(
    title="The Town of Larchleah",
    content="""Larchleah is a rustic logging settlement nestled on a wide curve of the mud-brown River Varn, many miles upriver from Dornon. It is encircled by ancient oak forests and towering pine stands interspersed with larches and firs.
From the kingdom's perspective, the town exists to feed the insatiable industrial and naval needs for timber. The town is the first major staging point for wood being harvested from the wilder reaches of Corvland.
While it lacks the refinement of Dornon, it possesses the tightly-knit charm of its hard-working populace.
**The August Chartist Company (Economy & Governance)**
Larchleah is a "company town," governed by a chartered monopoly known as **The August and Honourable Company of Larchwood**. Their sprawling timber barges are painted in striking crimson and gold, and their appointed foremen wear tailored wool coats with brass buttons stamped with the Company crest (a golden axe).
Wages for the laborers are paid mostly in Company scrip, which can only be redeemed at the Company Store for staples like flour, wool, and oil. Because scrip is useless elsewhere in Corvland, the locals rely on a barter economy to fill the gaps. Real coin is rare, usually only acquired through side-hustles—such as Martha Sager renting her spare room to traveling delvers or bargemen acting as unofficial merchants to sell local crafts (like Old Man Hollis's carvings) in the downstream markets.
**Social Hierarchy**
The social ladder is defined by one's relationship to the Company:
*   **The Foreman:** Sitting at the absolute top is the Company Foreman (currently Rosie's father), an educated outsider appointed by the Dornon executives. They live in the largest house on the hill, manage the ledgers, and represent upper-class authority.
*   **The Bargemen:** Below the Foreman are the bargemen (like "Long" Tom Sager). Because they pilot the Company's barges and bring back goods and coin from the outside world, they are highly respected and earn the best living among the working class.
*   **The Tradesmen:** Coopers, blacksmiths, and carpenters who maintain the town's infrastructure enjoy a comfortable, stable middle-ground.
*   **The Fellers:** At the bottom are the lumberjacks and tree-toppers (like Wicket's father and Gobber Dob). They do the most grueling work out in the woods for the lowest pay, often drinking away what little they earn at the local tavern.
**Town Layout and Key Landmarks**
The town is a collection of timber-framed, thatch-or-slate-roofed homes built along unpaved streets that turn into soup during the rainy seasons.
*   **The Barge Docks:** The heart of the town, jutting out into the deep, fast-moving channel of the Varn. It is a place of constant activity, shouting foremen, and the scent of pine tar and river-reeds. The lower pylons form secluded, shaded hollows where local children often claim "secret spots."
*   **The Graveyard:** An overgrown plot of ancient stones on a hill overlooking the town. It holds generations of loggers, but also hides older, forgotten secrets.
*   **The Foreman's Manor:** The only truly fine house in town, sitting on a high hill safely away from the muddy riverbank. It boasts glass windows, a proper hearth, and imported furniture.
While the town itself is a pocket of mundane industry overseen by wealthy city aristocrats, it sits on the edge of Corvland's magical wilderness. The surrounding forests are dotted with ancient ruins, overgrown graveyards, and stony cave mouths. These caves often connect to the magically active Everdark shallows. Sensible folk stay out of the woods and stick to the safety of the Company's logging camps, but for imaginative boys like Tal, the dark tree line represents a tantalizing promise of adventure, magic, and escape from drudgery.
"""
)


corva_entries: list[CodexEntry] = [
    corvish_isles,
    dornon,
    larchleah_town,
]
