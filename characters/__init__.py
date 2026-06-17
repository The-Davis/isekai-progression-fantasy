import sys
sys.dont_write_bytecode = True
from models.character import Character


wayne_coberly = Character(
    name="Trip Coberly",
    description="""Our viewpoint character, a West Virginia good ol' boy. Wayne Coberly III ("Trip") is a tall, wiry man in his late twenties. He's an excellent fisherman, decent shot, strong swimmer, distance runner, coon hunter, and good with his hands. The latter is how he's made his living, mostly getting by on a piece of land his family's owned since forever and doing contractor work to make ends meet.
Trip's lived in Wirt County (the smallest and least populous county of West Virginia) for all his life. He's a bit of an Andy Griffith type character, more than happy to goof around with friends and family, but with a strong backbone and a willingness to stand up for what's right as he sees it.
His morality doesn't always match what's modern. To some ways of thinking, he's downright backwards. Has a tendency to folksy ways of speaking and thinking. "Well... how 'bout that?" is a common phrase he uses. He'll often use coloquialisms.
Trip's been single for a while, isn't too close (or ornery or distant) with his family, and only has "buddies" rather than close friends, so when he ends up in the other world it's not that big a deal to him. Just one of those things. He'd probably have been a bit more upset if his coon hound hadn't shown up with him.
""",
)

banjo = Character(
    name="Banjo",
    description="""Banjo is a stout, deep-chested hound with the classic heavily mottled "blue" ticking over his body. He has a black head and ears and large, expressive brown eyes framed by black "spectacles". His ears are long and velvety, and his tail is thick and acts like a metronome for his mood.
At four years old, Banjo is in his physical prime. In the new world, he has suddenly been given the vocabulary to express his deeply canine sensibilities, but he is still very much a dog. He is obsessed with coons: tracking them, treeing them, their smells, their thieving ways, everything about them. If something bad happens, a coon is responsible. All his exclamations and expletives are coon/raccoon-centered. Less frequently, bobcats, pumas, bears, and other sorts of animals coon hounds are suited to hunting.
In Trip's head, Banjo sounds a bit like a gruff but amiable Southern fella. He is relentlessly optimistic, incredibly food-motivated, and utterly devoted to Trip. Aside from hunting, which is always his passion, Banjo also has an oddly-thorough knowledge of 50s and 60s westerns, sitcoms, and sci-fi. Trip had a habit of letting "TV Land" keep Banjo company when he was out.
To Banjo, Trip is the ultimate Pack Leader. He calls Trip "Boss" or "Chief" most of the time. If he calls him "Trip" or "Wayne", you know it's serious. Banjo views it as his personal duty to protect Trip from sneaky things, alert him to the presence of strangers, and point out when it is time for breakfast (which is always).
The bond between Banjo and Trip comes as a surprise to both of them. As they experiment with it, they learn they can "speak" clearly when in line of sight, but if separated by distance, it degrades into vague emotional impressions (panic, hunger, excitement, pain).
When the flintlocks start firing and the bayonets are fixed, Banjo is a guided missile of muscle and teeth. Coonhounds are bred to corner bears and cougars, and Banjo is absolutely fearless. In close-quarters combat or trench raids, Banjo will rip the throat out of an enemy soldier trying to sneak up on Trip, only to trot back covered in blood, wagging his tail, and telepathically asking for a treat.
""",
)

lachlan_mactavish = Character(
    name="Lachlan MacTavish",
    description="""Lachlan MacTavish is the clan laird of Glenrowan, a picturesque but poor highland valley in the Bannoch, where he serves as Justice of the Peace. He is also retired Captain of an infantry company who has previously served in Corvland's wars.
Lachlan is a barrel-chested man in his late fifties who looks like he has enjoyed a lifetime of hearty stews and good ale, yet still retains the dense, bullish muscle of a former soldier. He boasts a wild, mutton-chop beard the color of rusted iron and a nose that has clearly been broken at least twice. He dresses in a blend of aristocratic and rustic: a finely tailored, double-breasted woolen tailcoat of forest green worn over a traditional Bannish tartan waistcoat and riding breeches. Lachlan speaks with a rolling, amiable brogue. He has a habit of clasping his hands over his stomach when pleased and frequently invokes Canthican saints to justify his whims.
Lachlan views Trip's arrival in his pasture as God providing him with an expendable body to fulfill his military quota so he doesn't have to send any of his own people to die in the mud. Lachlan is so low in the noble pecking order that he can get away with openly supporting the church.
King Calador is perpetually preparing for the next inevitable, bloody clash with the mainland elves, and the Crown demands levies. Glenrowan's quota is coming due. The elves use devastating magic; the Corvish counter with disciplined volley fire, bayonet charges, and sheer bloody-minded endurance. The casualty rates are horrific. Lachlan loves his tenants. If he can fill his levy quota with robust "vagabonds" like Trip, he will.
"""
)

_characters: list[Character] = [
    wayne_coberly,
    banjo,
    lachlan_mactavish,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
