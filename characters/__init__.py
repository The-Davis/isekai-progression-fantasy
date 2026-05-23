import sys
sys.dont_write_bytecode = True
from models.character import Character


toby_henderson = Character(
    name="Toby Henderson",
    description="""A 28-year-old logistics manager for a shipping company in Cleveland, Ohio. Toby seems like the sort of person determined to do his 9-to-5, pay off his Honda Civic, occasionally date someone, and eventually die in a predictable manner.
    He dreams of adventure, but he's too practical (and risk averse) to actually go looking for it. If life's a journey, he's just along for the ride. Or he was. When the crew of the *Sunk Cost Fallacy* drag him along on their planar voyage, he's suddenly very interested in the idea of real aventure.
    Toby is entirely out of his depth in the planes but possesses a highly practical mind for organization and problem-solving. He quickly comes to realize that he's been living his life as an empty shell of a person. He doesn't know what he wants, but he knows it's "not what I had".
    Toby serves as the reader's surrogate, keenly aware that he's ordinary and uninteresting, but eager to be something more than that, even if it's largely vicariously through his new friends.
""",
)

vex = Character(
    name="Vex",
    description="""A cynical, chain-smoking Ozkura who makes a meager living writing a frequently-incorrect and often-exaggerated travel log on behalf of the Neophyte's Guide to the Planes. At the start of the story, Vex has been stranded on Earth for a year. She has developed a habit for cheap, gas-station menthols during this time.
Her wardrobe consists of a mix of planar gear and mundane Earth apparel. Her Cloak of Many Pockets always figures into her outfit, which usually consists of grungy jeans and a faded (stolen) "Cleveland Browns" t-shirt.
The cloak is a magical item that can hold anything that can fit through any of its many pockets. Vex does not feel the weight of the items within, but they clang about. It's a constant source of noise and minor inconvenience. It is impossible to conceal theft with a Cloak of Many Pockets, but that doesn't stop Vex from trying.
During her year on Earth, she developed a deep fascination with diner culture. She has an entire pocket of her coat dedicated to stolen diner syrup dispensers, miniature Tabasco bottles, and a highly prized waffle iron she lifted from a Denny's. She had to disassemble it completely to get it to fit into her cloak's pockets.
Vex writes for *The Neophyte's Guide to the Planes*, but she treats facts as mere suggestions. Travel journalism in the planes is dangerous. Vex doesn't want to risk her life exploring a volcanic demiplane inhabited by fire elementals, so she will sit in a tavern on a perfectly safe plane, buy a drink for someone who claimed to have been there, and embellish their story.
The publishers of the *Guide* pay her very little, which she uses to justify her poor research. If a reader gets lost or eaten because of her directions, she views it as a personal failing on their part for trusting a cheap guidebook.
Vex uses purple prose, heavy sarcasm, and occasional warnings that are entirely made up to spice up the narrative (e.g., claiming a perfectly safe meadow is home to "invisible, flesh-eating sheep").
She is eager to leave Earth. She never meant to be there in the first place, and she found it to be incredibly boring and bogged down by laws that make no sense to an Ozkura. However, she did appreciate the ready availability of cheap coffee and processed sugar, particularly where pancakes and syrup are abundant.
Dynamic With Toby: Toby thrives on order, spreadsheets, and predictable outcomes. Vex doesn't mind if a map is inaccurate as long as it looks nice. She finds Toby's anxiety hilarious but appreciates his organizational skills. Toby, conversely, is horrified by her lack of professional ethics and her habit of stealing silverware.
Dynamic With Jacicus: Jacicus wants everything to be an epic saga. Vex has seen enough "epic sagas" end in cholera or sudden decompression in the Astral Void. She acts as a sarcastic foil to his dramatic monologues, often pointing out the practical or embarrassing flaws in his grand plans.
Dynamic With Yorrick: As a hyper-caffeinated, anxious floating skull, Yorrick is loud and demanding. Vex generally ignores his panic, sometimes using his glowing head as a reading light when she is writing her logs at night. She occasionally threatens to use him as a bowling ball.
Narrative Role: Vex serves as the "unreliable guide" and the voice of pragmatic pessimism. When the crew needs to know how to navigate a dangerous plane, Vex's guidebook entry is the only reference they have—leading to comedic tension when they realize she wrote the entry based on a rumor she heard in a bar.
""",
)

jacicus = Character(
    name="Jacicus",
    description="""The dashing, outrageously dramatic Druthi captain of the *Sunk Cost Fallacy*. Jacicus is the self-appointed protagonist of his own grand adventure. He views the multiverse as a stage, and himself as the leading man. As a Druthi, his emotions are always dialed to eleven.
Despite his ridiculous theatrics, Jacicus is genuinely charismatic. He believes in the romance of the voyage, which occasionally inspires his crew to do heroic things despite themselves. However, his decision-making is heavily compromised by his adherence to his dramatic instincts rather than common sense. If a logical plan lacks poetic flair, Jacicus will reject it in favor of a reckless, spectacular alternative.
Jacicus possesses classic Druthi features—sharp, elegant elvish ears, dark skin, and stark white hair styled in an effortlessly windswept look. He wears a high-collared, deep purple captain's coat that has seen better days, adorned with tarnished gold trim.
He wears a silk eyepatch over his left eye. He does not actually need it; he swaps which eye it covers depending on which side of his face has better lighting during a conversation.
As a Druthi, Jacicus lives by a highly specific, constantly shifting code of personal conduct. This code is entirely logical to him, but baffling to everyone else. For example:
He will never strike an unarmed opponent, but he will happily toss an enemy a spoon and declare them "armed and dangerous."
He considers it a matter of supreme honor to always pay his debts, but he defines "payment" broadly, sometimes offering a heartfelt poem or a "debt-acquitting handshake" in lieu of actual currency.
He will never break a promise, but he is a master of finding semantic loopholes in his own vows.
Dynamic With the *Sunk Cost Fallacy*: Jacicus is irrationally loyal to his ship. He purchased the vessel under highly questionable circumstances and has spent far more money repairing it than it is worth. True to the ship's name, he refuses to abandon it, viewing its frequent failures as "opportunities for the crew to show their mettle." He speaks to the ship as if it were a temperamental lover, often apologizing to the hull after rough handling.
Dynamic With Toby: Jacicus views Toby as a tragic man starved of "the poetry of existence." He has taken it upon himself to be Toby's mentor in the arts of adventure, much to Toby's distress.
Dynamic With Vex: Jacicus is constantly trying to get Vex to write about him in *The Neophyte's Guide to the Planes* in a heroic light. He often stages dramatic poses when he thinks she is looking, or dictates grand, fictionalized versions of their daily activities to her.
Dynamic With Yorrick: Their dynamic is one of noisy friction. As the ship's spell-mechanic, Yorrick is the one who actually has to deal with the physical consequences of Jacicus's dramatic maneuvers. Jacicus treats Yorrick like a Shakespearean prop, occasionally holding him aloft to deliver monologues about mortality. Yorrick hates this, usually responding by biting Jacicus's fingers.
Narrative Role: Jacicus serves as the instigator of the plot. His refusal to back down from bad decisions, combined with his dramatic flair, ensures that simple logistical trips frequently escalate into absurd, high-stakes escapades.
""",
)

yorrick = Character(
    name="Yorrick",
    description="""The ship's spell-mechanic is a floating, glowing skull containing the soul of a deeply anxious, hyper-caffeinated dead wizard. While most undead are driven by dark purposes or unfinished business, Yorrick is driven entirely by the need to keep the *Sunk Cost Fallacy* from falling apart. He also, strangely, fears death (or an end to his undeath) in a way that puzzles those who do not understand the planes as deeply as he does.
As a fleshless skull, Yorrick has no digestive tract, nervous system, or bloodstream. Yet somehow, he is hopelessly addicted to Jolt Cola, which he imports from Earth by the crate. When he "drinks" a can, he has one of his assistants pour the soda directly into his mouth. The liquid vaporizes inside his cranial cavity, venting out of his eye sockets and ear canals as a sweet, carbonated, neon-colored steam. He insists that the caffeine stimulates his magical core, though the rest of the crew suspects it is psychosomatic. When deprived of Jolt, his magical glow dims to a sluggish flicker, and he becomes irritable.
To keep the ship running, Yorrick relies on a crew of three animated skeletons who serve as his sub-mechanics (whom he has named Tom, Dick, and Harry). Yorrick is deeply embarrassed by the fact that he is technically a necromancer. In the high-minded wizarding circles he once aspired to, necromancy is considered tacky, unhygienic, and socially ruinous.
Dynamic With Toby: Yorrick and Toby share a mutual appreciation for order, but their anxieties manifest differently. Toby worries about supplies, but Yorrick worries about the planar drive imploding and scattering their atoms across seven different dimensions. Yorrick often vents his frustrations to Toby because Toby is the only crew member who actually listens to his safety warnings.
Dynamic With Vex: Vex occasionally taps on his forehead to see if he's "home" (he always is), and uses his glowing head as a reading light when she's writing her travel logs late at night. He finds the former annoying and the latter oddly endearing. For the most part, the pair have little to say to one another.
Dynamic with Jacicus: Constant friction. Jacicus views the ship's mechanical failures as "poetic challenges," while Yorrick views them as "preventable disasters caused by an idiot captain." Whenever Jacicus demands a reckless maneuver, Yorrick is the one who has to push the engines past their safety limits. He frequently bites Jacicus's fingers when the captain tries to hold him like a skull in a play.
Narrative Role: Yorrick is the practical anchor of the ship's operations. While Jacicus provides the dramatic direction and Vex provides the questionable navigation, Yorrick is the one who actually understands how the multiverse works on a physical and magical level. He serves as a source of exposition for the reader, explaining the dangerous (and often absurd) rules of the planes, usually while screaming in terror as he tries to fix a faulty ward spell.""",
)


_characters: list[Character] = [
    toby_henderson,
    vex,
    jacicus,
    yorrick,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
