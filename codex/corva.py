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

corva_entries: list[CodexEntry] = [
    corvish_isles,
    dornon,
]
