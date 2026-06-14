import sys
sys.dont_write_bytecode = True
from models.character import Character


wayne_coberly = Character(
    name="Trip Coberly",
    description="""Our viewpoint character, a West Virginia good ol' boy. Wayne Coberly III ("Trip") is a tall, wiry man in his late twenties. He's an excellent fisherman, decent shot, strong swimmer, distance runner, coon hunter, and good with his hands.
Trip's been a deputy in Wirt County (the smallest and least populous county of West Virginia) for about five years. He's a bit of an Andy Griffith type character, more than happy to goof around with friends and family, but with a strong backbone and a willingness to stand up for what's right as he sees it.
His morality doesn't always match what's modern. To some ways of thinking, he's downright backwards. Has a tendency to folksy ways of speaking and thinking. "Well... how 'bout that?" is a common phrase he uses. He'll often use coloquialisms.
Trip's been single for a while, isn't too close (or ornery or distant) with his family, and only has work friends, so when he ends up in the other world it's not that big a deal to him. Just one of those things. He'd probably have been a bit more upset if his coon hound hadn't shown up with him.
""",
)

banjo = Character(
    name="Banjo",
    description="""Banjo is a stout, deep-chested hound with the classic heavily mottled "blue" ticking over his body. He has a black head and ears and large, expressive brown eyes framed by black "spectacles". His ears are long and velvety, and his tail is thick and acts like a metronome for his mood.
At four years old, Banjo is in his physical prime. In the new world, he has suddenly been given the vocabulary to express his deeply canine sensibilities, but he is still very much a dog.
In Trip's head, Banjo sounds a bit like a gruff but amiable Southern fella who has had a few too many porch-beers. He is relentlessly optimistic, incredibly food-motivated, and utterly devoted to Trip.
To Banjo, Trip is the ultimate Pack Leader. He calls Trip "Boss" or "Chief" most of the time. If he calls him "Trip" or "Wayne", you know it's serious. Banjo views it as his personal duty to protect Trip from sneaky things, alert him to the presence of strangers, and point out when it is time for breakfast (which is always).
The bond between Banjo and Trip comes as a surprise to both of them. As they experiment with it, they learn they can "speak" clearly when in line of sight, but if separated by distance, it degrades into vague emotional impressions (panic, hunger, excitement, pain).
Banjo is obsessed with *treeing things*, bacon grease, belly scratches, and investigating new smells. When they encounter the fantastical beasts of this new world, Banjo's first instinct will be to determine if it can be treed, and his second will be to ask Trip if they can eat it.
Banjo is a massive morale booster. In a military camp setting (like *Sharpe's Rifles*), the enlisted men will absolutely adore him. He becomes the unofficial mascot of whatever unit Trip ends up in. Scenes of Banjo cadging scraps from the regimental cook or sleeping by the campfire provide the perfect "cozy" downtime.
When the flintlocks start firing and the bayonets are fixed, Banjo is a guided missile of muscle and teeth. Coonhounds are bred to corner bears and cougars, and Banjo is absolutely fearless. In close-quarters combat or trench raids, Banjo will rip the throat out of an enemy soldier trying to sneak up on Trip, only to trot back covered in blood, wagging his tail, and telepathically asking for a piece of jerky as a reward."""
)

_characters: list[Character] = [
    wayne_coberly,
    banjo,
]


def get_characters() -> list[Character]:    
    global _characters
    return _characters
