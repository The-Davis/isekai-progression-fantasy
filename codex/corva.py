from models.codex import CodexEntry

corvish_isles = CodexEntry(
    title="Corvish Isles",
    content="""The Corvish Isles are this world's version of the British Isles. Corva is the name of the largest island, though it is also called "Corvland"
    Corvland is the industrial and cultural heart of the Corvish Empire and home to the Corvish ethnolinguistic group, which is by far the largest population in the isles. It is a land of rolling green hills, dense oak forests, and sprawling cities.
    The capital city of Dornon sits in the northern-central region along the wide, mud-brown River Varn.
    Corvland is historically the seat of royal power, and its MPs dominate the House of Commons. The northern part of Corvland is the Bannoch, home to the Bannish ethnolinguistic group.
    The Bannish Lowlands are industrious, boasting colossal factories and textile mills that rival Dornon's output. Its Highlands are a wild, romantic expanse of sweeping glens, deep, freezing lochs, and jagged, snow-capped mountains. Bannish Highlanders are fearsome, fiercely loyal infantry regiments who march to war to the drone of Bannish bagpipes.
    The mountainous western expanse of Corvland is Rhondda Taf, home to the Rhondish ethnolinguistic group. It is a land of deep, rain-swept valleys, jagged peaks, and ancient stone. Rhondda Taf is the heavy-mining capital of Corva; its mountains are dotted with colossal headframes where generations of Rhondish men have dug out iron, slate, and coal reserves. The Rhondish people are fiercely proud, culturally distinct, and highly musical.
    The island of Galidon is often called "The Emerald Isle" for its staggering, vibrant greenery. It is the most fertile of the Corvish Isles. Galidon is predominantly agricultural, dotted with ancient, ruined pre-Collapse monasteries and sprawling Canthican cathedrals. It produces the famous "Galish Wool" and provides much of the Empire's basic foodstuffs. Historically, Galidor had a fraught, rebellious relationship with the Crown, having endured several brutal pacifications in centuries past. Today, it is firmly under Crown rule, though resentments still simmer in its poorer, western counties, making it a volatile voting bloc in the House of Commons.
The Corvish Isles are almost exclusively human. Non-humans are seldom welcome, but they can be found in ports. Inland, they're hunted as vagabonds.
"""
)

dornon = CodexEntry(
    title="Dornon",
    content="""The capital city of Corva is Dornon, originally "Dorn-on-Varn", but shortened over the centuries to Dornon. It is situated in the northern hemisphere of Corva, on the banks of the Varn river.
    It is the largest city on the banks of the Varn river. It is essentially like London at the height of the British Empire, scaled up to fit the world of Corva and the starfaring Corvish Empire.
    Its districts have names like Graymarket, the Clinks, Hearthgate, Thorncross, and Ashmoor. Whenever writing about Dornon, consider using these district names, but do not limit yourself to them.
    Most of these are ancient names that have been passed down for centuries, and the original meaning of the names has been lost to time.
    Many are run down and dangerous, but their denizens take fierce pride in their neighborhoods and are loyal to their own.
    Streets should have charming and interesting names as well, like Binders' Walk and the Red Row.
    The city is a bustling metropolis, with a population of over 8 million people. It is a center of commerce, culture, and politics, and is home to the Corvish royal family.
"""
)

corva_entries: list[CodexEntry] = [
    corvish_isles,
    dornon,
]
