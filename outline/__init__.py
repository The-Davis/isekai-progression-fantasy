import sys
sys.dont_write_bytecode = True
from models.outline import Outline


act_one = Outline(
    title="Act One",
    content="""
Our story starts with a description of the boy's life in his riverside town, including his playful tricks and minor punishments, exploration around the sawmill, trips down the river and to the sea, and so on.

**Chapter 7:** The new Company Foreman arrives on a crimson barge with his elfkin daughter, Rosie Winslow, and Tal is instantly smitten by her pristine beauty and fancy pastel dresses, much to the eye-rolling disgust of his longtime friend Clary.
**Chapter 9:** Eager to impress the sheltered but curious Rosie, Tal offers to be her local guide to the shallow ruins on the edge of the Everdark; Clary aggressively tags along out of jealousy, and Cord gets dragged in to keep everyone from breaking their necks.

**Chapter 11:** Tal gets in serious trouble with Martha when Simmon catches him sneaking Rosie some of the family's prized honey-cakes; Tal is confined to the house with extra chores, leaving sweet little Elsie and an exasperated Wicket to act as his messengers to the outside world.

**Chapter 12:** While grounded, Tal spies from his window and notices Jasper sneaking out late at night to meet with the usually drunk Hollis and the terrifying Gobber Dob, sparking his curiosity about what a wealthy wizard, a harmless woodcarver, and a vicious thug could possibly be plotting.

**Chapter 13:** Freed from his grounding, Tal tries to show out for Rosie by walking the precarious barge pylons over the river, but a biting, sarcastic comment from a jealous Clary makes him lose his balance, resulting in a hilarious and embarrassing dunk in the freezing Varn.

**Chapter 14:** Seeking to regain his dignity, Tal uses the mental focus exercises Jasper taught him to perfectly win a town-wide skipping stone contest, earning an admiring gasp from Rosie and making Clary cross her arms in frustrated, unspoken affection.

**Chapter 15:** Tal and Wicket visit the docks to trade for one of Hollis's beautiful wooden dolls for Elsie, and while they are there, they overhear Jasper subtly questioning the blackout-drunk old man about the location of a specific, ancient Corvish gravestone on the hill.

**Chapter 16:** Rosie invites Tal, Wicket, and Clary to the Foreman's manor for tea; the stark contrast in wealth makes Clary intensely uncomfortable, sparking a tense, polite argument between the two girls over the "romance" of river life versus the reality of hard work.

**Chapter 17:** Tal continues to practice Jasper's mental exercises and feels the absolute faintest flicker of willpower in his mind, but his excitement turns to dread when he spots Gobber Dob lurking menacingly around the Sager home, his beady eyes locked on Jasper's window.

**Chapter 18:** Driven by his burgeoning adventurous spirit and a desperate desire to prove he is the brave delver Rosie thinks he is, Tal convinces Wicket and Cord to sneak out at midnight to investigate the overgrown graveyard after he sees Jasper slip away with a lantern and a shovel.

**Chapter 19:** Tal, Cord, and Wicket witness Hollis digging up a grave while Jasper Moray supervises. Hollis and Jasper fight and Hollis is knocked out. Gobber Dob then appears; it becomes clear Gobber and Jasper conspired to cut Hollis out of the deal, but then Gobber murders Jasper in the graveyard with Hollis' knife. The boys flee in terror as Gobber makes off with the artifact Jasper looted from the grave.

**Chapter 20:** The traumatized boys flee the graveyard and take refuge in Tal's hidden spot beneath the docks, where a terrified Wicket frantically recites a dark local omen that convinces them to swear a pact of absolute secrecy, fearing Gobber Dob will hunt them down if they speak a word of what they saw.

"""
)

act_two = Outline(
    title="Act Two",
    content="""
Fleeing town to avoid being called at the trial, he and his friends face serious hardships before finally returning and testifying. The real killer escapes, swearing vengeance.

Chapter 11: INNOCENT MAN's arrest weighs on Tal's conscience.
Chapter 12: Tal tries a "pain-killer" remedy on his mother (who then gives it to the cat). Rosie falls ill.

### Delver Adventure and Return
Chapter 13: Heartbroken, Tal, Wicket, and OTHER_FRIEND run away to Jackson's Island to become delvers.
Chapter 14: They enjoy camp life—fishing, swimming, smoking—while the town mourns them as drowned.
Chapter 15: Tal sneaks home at night to check on his mother and learns of the funeral plans.
Chapter 16: The boys face a storm, homesickness, and OTHER_FRIEND's illness. Tal reveals his secret visit.
Chapter 17: The boys dramatically appear at their own funeral in temple, delighting the town.
Chapter 18: Tal tells his mother a "dream" version of his visit; Rosie still spurns him.

### School, Testimony, and Treasure Hunting
Chapter 19: Tal takes Rosie's punishment for tearing a book.
Chapter 20: More school antics and Tal's jealousy.
Chapter 21: End-of-term examinations and a pompous speech.
Chapter 22: Tal joins a temperance group but struggles; Wicket quotes scripture awkwardly.
Chapter 23: Tal testifies at INNOCENT MAN's trial, saving him but fearing KILLER.
"""
)

act_three = Outline(
    title="Act Three",
    content="""After things return to normal and seem peaceful, KILLER returns. The boy and a friend are pursued into a dungeon by KILLER.

Chapter 24: Tal has nightmares about KILLER.
Chapter 25: Tal and Wicket hunt for buried treasure.
Chapter 26: In a haunted house, they overhear KILLER and a partner find gold and plan to hide it at "Number Two."
    
### Later Adventures: Danger, the Cave, and Resolution
Chapter 27: The boys investigate possible hideouts.
Chapter 28: Wicket watches KILLER's place.
Chapter 29: At a picnic, Tal and Rosie explore (DUNGEON). Wicket saves the Widow Douglas from KILLER.
Chapter 30: Search parties hunt for the lost children; KILLER is still a threat.
Chapter 31: Tal and Rosie get lost deep in DUNGEON, face starvation and terror (spotting KILLER), and eventually find a way out.
Chapter 32: They are rescued to great joy.
Chapter 33: KILLER starves in DUNGEON. Tal and Wicket return to find the treasure.
Chapter 34: The boys reveal the gold (split between them) at the Widow Douglas's gathering.
Chapter 35 (and Conclusion): Tal and Wicket are rich and celebrated. The Widow adopts Wicket to "civilize" him; Tal forms a robber gang that Wicket reluctantly joins.

They manage to use the dungeon to get the killer killed, recover dungeon treasure, and thus earn a coveted spot in the kingdom's training lyceum.
"""
)

_outline: list[Outline] = [
]


def get_outline() -> list[Outline]:
    global _outline
    return _outline
