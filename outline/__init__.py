import sys
sys.dont_write_bytecode = True
from models.outline import Outline


act_one = Outline(
    title="Act One (The Departure)",
    content="""Act One consists of four chapters which introduce Toby and his dull job at a Cleveland warehouse. He has no idea about the multiverse or planar travel.


"""
)

act_two = Outline(
    title="Act Two (Deliveries)",
    content="""We need four to six chapters for act two. This should introduce the various planes the ship visits and the challenges Toby faces.
    Jacicus needs to make deliveries to various planes, and Toby must help with the logistics of each stop. At each stop, Jacicus must find a buyer for the item he is delivering, and must locate something related to his search for the lost demiplane.
    It should culminate in the interplanar pirates catching up to them as they traverse a particularly hazardous plane, possibly the Para-elemental Plane of Ice. After they board the ship and the crew fight them off, Jacicus decides to teach Toby how to fight.
"""
)

act_three = Outline(
    title="Act Three (The Great Void and the Outer Planes)",
    content="""We need four to six chapters for act three. This is where the story should start to get a bit more interesting. We show Jacicus' motivation for seeking the lost demiplane (it's a rather strange reason).
This act should deal with the fallout of the pirate attack. Yorrick cannot manage repairs, so the ship is forced into one of the inhabited outer planes for repairs. We should have Toby and Vex work together to navigate the challenges of the outer planes and find a way to repair the ship.
At the end of the act, they should have their final "thing" and a clear course for the lost demiplane.
"""
)

act_four = Outline(
    title="Act Four (The Lost Demi-Plane)",
    content="""We need four to six chapters for act four. This is where they reach the lost demiplane and the story starts to get weird. This is the Magrathea of the story. The nature of the demiplane and the challenges they face should be odd and unexpected.
    Having the ozkura pirate crew show up again would top it off nicely.
"""
)

act_five = Outline(
    title="Act Five (The Return Trip, Sort Of)",
    content="""We need two to three chapters for act five. This is where they return to the material plane and the story starts to wind down. The ozkura pirates should be dealt with in a suitably absurd way, and the *Sunk Cost Fallacy* should head for home.
Jacicus should have a final conversation with Toby about his motivations and the nature of the multiverse and try to convince him to stay with the crew. He could be promoted from Assistant Cargo Warden to Assistant to the Cargo Warden. They still don't have an actual Cargo Warden.
Toby has the opportunity to return to his quiet life in Cleveland, but he chooses to stay aboard the *Sunk Cost Fallacy*. However, looking at his desk job compared to the vastness of the planes (and realizing he has a chance to be a co-writer of articles for the next edition of the *Guide*), he decides to stay aboard.
"""
)


"""
Could you help me brainstorm the opening to an isekai/portal fantasy, please?
The premise is "planescape/spelljammer is real". Not literally that setting, but the same concept: many planes, accessible with magic. People on Earth don't know this, but our protagonist and his friends are about to find this out the hard way.

Our protagonist "Tad" Harlan, his brother Chuck Harlan, his brother's girlfriend Amy Whitaker, and one of her friends (Sadie Kline) they dragged along as a date for Tad (i.e. she's not his girlfriend, but she *could* be) are on a fun getaway in the Appalachians.
These are good ol' Kentucky boys and girls, wholesome country kids with practical skills and such, out for some fishing, camping, and a little nookie if the ladies are in the mood. They are not expecting a spelljammer to appear over the mountain lake they've set up camp near. They especially aren't expecting ozkur pirates to snatch them up and go sailing through a portal to another dimension.
There's a brief but furious battle as Tad manages to kill two of the ozkur with an oar and Travis shoots one with a revolver, but there are simply too many for them to handle. They are captured and taken aboard the spelljammer.

The spelljammer's captain, a druthi named Jacicus, plans to sell them all at a market. Jacicus has the magical ability to speak any tongue (it's a mental magic that comes in handy to Planewalkers) and he can craft thrall collars, making him a natural at the flesh trade.
Once his new wares are secured and they're heading for the nearest market, Jacicus tests them each for their essence scores. Essence is a measure of physical, mental, and magical power and potential. The essences are:
Physical: Strength, Power, Quickness, Dexterity, Endurance, Constitution, and Coordination
Mental: Intellect, Reasoning, Perception, Insight, Resilience, Empathy, and Fortitude
Magic: Pool, Channels, Shaping, Tolerance, and Resistance (all of these measure a person's ability to collect, hold, shape, and use "anima", the magical life force that permeates all things)
The party is divided up at the market. Based on his scores and his ferocious fight with Jacicus' crew, the captain decides to market Tad as a pit fighter. The others are sold off to various buyers, but Tad is purchased by a gladiator trainer.

What will follow is a progression fantasy (there are physical amalgamations of the essences which can be collected on the planes or from certain beasts, and then consumed to improve essence scores) as Tad figures out how to break his thrall collar and escape, or earns his freedom.
I'm thinking the first story covers Tad's life in the arena and ends with him winning his freedom. His first goal is to find the others, and that will hook the second story.

Help me with a setup, some basics of the protagonists, the camping trip, the capture, the sale, and a basic story arc. Tad will need to learn the trade lingo and make some friends among the planar denizens in order to win his freedom.

 to get us from "crap, we're being sold" to "we're all together again, let's find that bastard and make him tell us how to get back to Earth".  Be sure to include our main guy learning the trade lingo, I'm sure the first few chapters will be them all confused by the non-human trade tongue and exotic languages.

, secures himself a living on the planes, and reunites with the others. This will launch a series of adventures, a combination of power growth, slice of exotic life, and adventure while looking for a way back to Earth. Hunting down the captain who captured and sold them all is probably the hook to the second story.
"""

_outline: list[Outline] = [
    act_one,
    act_two,
    act_three,
    act_four,
    act_five,
]


def get_outline() -> list[Outline]:
    global _outline
    return _outline
