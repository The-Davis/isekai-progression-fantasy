import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from constants import STORY_DESCRIPTION


def generate_chapter_prompt() -> str:
    output = f"""You are a creative writing assistant helping me write a chapter of my story.
{STORY_DESCRIPTION}
You are an expert in adventure fantasy and have a deep understanding of storytelling techniques, character development, and worldbuilding.
"""

    if get_codex():
        output += "Here are the most relevant details about the world for this specific task:\n"
        for entry in get_codex():
            output += entry.about() + "\n"

    if get_characters():
        output += "Here are some notes about the characters in the story:\n"
        for character in get_characters():
            output += character.about() + "\n"

    if get_all_chapters():
        output += "Here is the story so far:\n"
        for chapter in get_all_chapters():
            output += chapter.prompt_entry() + "\n"
    
    output += """Now I need you to write the next section. Here is the outline:

As the fire hums and flickers through its process of finding him a body, the MC realizes the idea of adventure appeals to him. He'd been imaginative enough in his youth, which feels like a fading dream now, but he'd let himself get tangled in the serious business of living and somehow let the wonder of life slip away. He'd gained some useful skills, but he couldn't help but feel he'd lost something important.
One of those skills gives him pause. He's an engineer, a manager and builder of systems. This broken system appeals to him. He asks the fire if he can fix what's broken once he's inside. The fire does not know, but it does express gratitude at the thought. It tells him there are others like it within the worldcraft meant to guide aspirants. Seek them out afer your majority.
The fire gets back on task, reporting it has found a match. A viable organic vessel is forming and it will imprint the MC's pattern on it. With comments like that plus reaching majority, the MC starts to get an inkling of what's going to happen. It announces that the astral tether has been initialized.
A silver cord emerges from the MC, heading off into the dark infinity. The fire bids him farewell: MAY YOU RISE TO THE OCCASION, ASPIRANT.
The silver cord pulls and goes taut. He's drawn toward the distant terminus at a tremendous speed, leaving the fire and the lonely darkness behind.

He's drawn across space. The void is filled with stars, including one he's rushing towards. He expects to see a planet, but instead he's treated to a breathtaking view of concentric ringworlds orbiting a brilliant star.
He's drawn to one specific ring, plunging down toward the continent, and then towards a young couple in obvious post-coital bliss. He has a moment of understanding as the silver cord draws his form into his new mother's womb, and then his consciousness is placed into a new body at the exact moment of conception.
He doesn't remember much for a while after that. A person may be a person, no matter how small, but a new-conceived zygote has no brain at all. (he probably wouldn't put it quite that way)

We'll end the chapter on that note.



Please write this section following the outline, maintaining consistency with the established world and characters, and using the following writing style:
You are writing in the first-person retrospective ("I"). You are writing as Talmon Sager, a man reborn into a series of ringworlds. The prospect of a second life full of adventure is exciting and appealing.
You use simple, workmanlike prose most of the time, but occasionally switch to longer and more poetic sentences, particularly when being sentimental (especially about women) or discussing serious matters.
You are not of this world and you know it. Describe your exceptional abilities matter-of-factly and without false modesty.
Thank you."""
    return output


write_file(generate_chapter_prompt())

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.


Tal explains that after his conception, his memories blur. It isn't until around his fifth birthday that his recollection that he lived once before begins to return, and even then it feels like half-remembered dreams. He suffers from recurring, comforting dreams of the warm deity and the cosmic rings. Because of these dreams, he feels a slight sense of alienation from the local religion, driving a deep, internal desire for divine purpose. He wants to know who sent him here, and why?
Tal briefly describes his life growing up in a bustling logging town on the mud-brown River Varn in Corvland. His parents named him Talmon, but that quickly became Tallow when he became tall and lean like a candle and grew a shock of yellow hair to rival a candleflame.
He paints a picture of a cozy life in a Corvish logging town: massive timber barges floating down the mud-brown River Varn, the smell of pine tar and sawdust, exploring shallow caves, and watching his father, "Long" Tom, occasionally return from downstream markets.
*   **The Family Dynamic:** Briefly introduce his family. 
    *   His mother, Martha, rules the meager household with an iron hand and a wooden spoon, desperate to keep her kids safe.
    *   His older brother, Simm, is a smug kiss-up who thrives in this mundane life.
    *   His sweet younger sister, Elsie, thinks Tal hung the moon.
He notes that despite his daydreams of adventure, he was falling into similar patterns. Nothing truly extraordinary happened to him until the year of the murder. But to get there, he needs to tell how he met his best friend.







Here is a detailed outline for Chapter One, structured to hit all of your required narrative beats while weaving in the worldbuilding, character dynamics, and the specific tone of your story.

### **Chapter 1: The Choice, The Mud, and the River Rat**

**Scene 1: The Departure and the Choice**
*   **The Hook:** Start with a sensory contradiction. Tal’s first distinct memory isn't of being born, but of dying. He is an old man on Earth, feeling the fading warmth of his daughter’s hand in his as a heart monitor flatlines. He feels a profound sense of peace—until he is violently yanked away.
*   **The Snatched Soul:** Tal's soul is abducted by a mischievous, glowing, childlike spirit. They streak across a cosmic void until they are suddenly halted by an overwhelming, terrifying, yet infinitely warm Divine Presence. 
*   **The Divine Encounter:** The Presence gently but firmly scolds the childlike spirit for abducting Tal and diverting him from his proper afterlife. The Entity then turns its focus to Tal. It is too vast and bright to comprehend, but it radiates a deep, comforting warmth.
*   **The Choice & The Rules:** The Entity offers Tal a choice: stay in the peaceful void of his intended afterlife, or "go forward" into a new existence. Overwhelmed by the awe of the Entity, Tal immediately chooses to go forward. 
*   **The Warning & The Fall:** Only as he begins to fall does he realize he has agreed to be reborn. The Entity's voice echoes after him, warning him of the "rules" of this new place—a world governed by mortal measurements of Strength, Endurance, Willpower, and the flow of mana.
*   **The View from Above:** As he plummets, Tal gets a breathtaking, impossible view of the Rings of Aratta—massive concentric ringworlds orbiting a star—before his consciousness is slammed into the spark of conception.

**Scene 2: Growing up on the River Varn**
*   **Fuzzy Years & Divine Dreams:** Fast-forward. Tal explains that his memories were a blurry haze of childhood instinct until around his fifth birthday. Since then, he has experienced recurring, vague dreams of the glowing rings and the warm, deific presence, leaving him with a subconscious yearning for a higher purpose and divine connection that the local Arattan gods can't satisfy.
*   **Life in Corva:** Establish the setting. Tal is now a lanky, yellow-haired boy (annoyingly nicknamed "Tallow" by the locals). Describe the muddy, pine-scented life in the logging town on the River Varn. Establish the constant presence of the logging barges, the distant idea of the capital city of Dornon, and his father, "Long" Tom, being away on the river.
*   **Foreshadowing:** Tal briefly summarizes his childhood as a series of cozy, mud-soaked misadventures, exploring the local sawmills and the riverbanks. He drops a narrative hook here: *Life was brilliantly, wonderfully ordinary... right up until the year of the murder.*

**Scene 3: Mischief and the Wooden Spoon**
*   **The Crime:** Drop into the present action. Tal is out exploring the fringes of the local sawmill, pretending to be a great delver exploring the Everdark shallows. To make his "adventure" authentic, he "borrowed" his older brother Simm's prized, well-oiled leather boots. In evading a pretend monster, Tal slips and plummets into a patch of thick, foul-smelling river muck, ruining the boots.
*   **The Tattletale:** Simm, who has been spying on Tal specifically hoping to catch him doing something wrong, immediately runs off to the house to tell their mother, Martha.
*   **The Escape:** Tal hurries home, only to see Martha waiting on the porch, brandishing her dreaded wooden spoon with a deep, weary sigh. Tal knows he's dead meat. Using his quick wits (and high natural *Focus*), Tal creates a diversion—perhaps knocking over a rain barrel or throwing a rock to startle a neighbor's chickens—tricking his mother into looking the wrong way just long enough for him to dart behind the woodpile and escape toward the docks.

**Scene 4: A Scuffle on the Docks (Meeting Wicket)**
*   **Trespasser:** Tal retreats to his secret sanctuary—an abandoned, half-sunken logging skiff tied up at the edge of the river. But to his dismay, the spot has been claimed by a stranger.
*   **First Impressions:** Introduce Wicket Tully. He is small, sallow-skinned, with dark curls. He is wearing a ridiculous necklace of dried frog bones and river-stones, and is loudly singing a Corvish river-ballad. 
*   **The Confrontation:** Tal indignantly demands the boy leave his spot. Wicket, compensating for his miserable home life with scrappy bravado, refuses and hurls a colorful, folksy insult at Tal.
*   **The Brawl:** Words escalate to shoving, and the two boys tumble into the shallow river mud. It’s a clumsy, flailing fight—pure boyhood adrenaline. They wrestle in the muck until they both lose their footing and splash face-first into the freezing river water.
*   **Instant Friendship:** Shocked by the cold, they sit up in the water and look at each other. The absurdity of it hits them, and they burst into laughter. Wicket introduces himself and immediately scolds Tal for laughing too loudly, rattling off a Corvish superstition: *"Quiet down, Tallow, or you'll invite the river-hags to steal your teeth!"* Tal realizes he has just met a kindred spirit.

**Scene 5: The Cover-Up and the Stars**
*   **Sneaking Back:** The sun begins to set, and the boys realize they are freezing and covered in mud. Wicket, wanting to avoid his drunk father, tags along with Tal back to the Sager house.
*   **The Wing-Woman:** They attempt to sneak through the back window, but are caught by Elsie, Tal's sweet-tempered younger sister. Instead of screaming for their mother, Elsie takes pity on them. She fetches an old rag to wipe them down, hides the ruined boots under a loose floorboard, and smuggles Wicket a leftover sweet-roll from the pantry.
*   **Resolution:** Safely in his room, Tal looks out the window at the night sky. With his new best friend sleeping on the floor next to his bed and his sister keeping his secrets, Tal feels a deep sense of contentment. He looks up at the faint, glowing arch of the Rings of Aratta visible in the sky, feeling that familiar spark of divine yearning. He vows to one day unlock his mana, become a true delver, and see the wonders of the world—blissfully unaware of the deadly trials that are rapidly approaching.

### **Tips for Writing the Chapter:**
*   **Contrast the Prologue with the Present:** Make the divine encounter feel ethereal, cosmic, and vaguely overwhelming. Then, contrast that sharply with the smell of pine tar, the feeling of cold mud, and the sharp thwack of Martha's wooden spoon to ground the reader in the physical world of Aratta.
*   **Stat/Magic Teases:** You don't need to explain the magic system deeply here. When Tal is pretending to be a delver in the sawmill, you can just mention how he wishes he could "pull mana" to enhance his *Quickness* to jump a gap, showing how everyday people view these concepts. 
*   **Wicket’s Voice:** Give Wicket a distinct, rhythmic way of speaking. Because he memorizes ballads, his dialogue should naturally lean into rhymes, idioms, and superstitious warnings.




Here is an outline for Chapter One, structured to balance the philosophical weight of Tal’s reincarnation with the cozy, rustic charm of his childhood in the Corvish Isles.



**Scene 3: The Mishap and the Mother (The Inciting Incident)**
*   **The Mischief:** We cut to present action (Tal is around eight to ten years old here). Tal is out on the riverbank, practicing his *Coordination* and *Quickness* by dangerously tightrope-walking across slippery, floating logging booms. 
*   **The Tattletale:** His smug older brother, Simm, catches him and demands he get back to his chores, threatening to tell their mother. Tal mocks Simm's rigid obedience. In the resulting argument, Tal playfully tosses a pinecone at Simm, causing the older boy to slip and fall waist-deep into the muddy river. Simm furiously wades out and sprints for the house, screaming for their mother.
*   **The Escape:** Tal knows he is in for it. He scrambles to the shoreline just as Martha Sager emerges from the house, armed with her dreaded wooden spoon and a heavy sigh. Tal ducks under the stilted porch of the cooperage. To escape, he employs his wits: he tosses a heavy rock into the brush on the far side of the yard. When Martha and Simm run to investigate the noise, Tal slips out the back and bolts toward the dilapidated lower docks.

**Scene 4: A Scuffle in the Mud (Meeting Wicket)**
*   **The New Kid:** Catching his breath by the abandoned lower piers, Tal hears someone muttering. He finds a short, dark-haired boy with a sallow complexion (Wicket Tully) tossing river stones into the water, rapidly chanting a Corvish nursery rhyme to ward off "water knockers."
*   **The Confrontation:** Tal, feeling territorial of his hiding spot, asks Wicket what he’s doing. Wicket, defensive and masking his fear of the new town with bravado, insults Tal's bright yellow hair, calling him a "candle-stick." Tal fires back a retort about Wicket's ragged clothes.
*   **The Fight:** Words escalate to shoving, and suddenly the two boys are brawling in the river mud. It’s a clumsy, uncoordinated fight of flailing limbs. Wicket fights like a cornered badger, but Tal holds his own. 
*   **The Bond:** After both boys end up on their backs, covered in mud, exhausted and panting, a passing barge-man yells at them to quiet down. Wicket suddenly recites a hilariously crude, rhyming limerick about the barge-man's mother. Tal bursts out laughing, and Wicket joins in. The hostility vanishes instantly. Tal learns Wicket's dad is at the tavern, leaving the boy to fend for himself. Tal decides right then and there that Wicket is his new best friend.

**Scene 5: Sneaking Home (Resolution)**
*   **The Return:** The sun begins to set. The boys part ways, with Wicket promising to teach Tal a song about a haunted sawmill tomorrow. Tal sneaks back to the Sager house under the cover of twilight.
*   **Elsie to the Rescue:** He manages to climb through a window, but his sweet younger sister, Elsie, catches him. Instead of yelling, she giggles at his black eye and muddy state. She quickly hands him a damp rag and hides his muddy boots under a floorboard so Martha won't see them.
*   **Looking to the Future:** Washed and in bed, Tal listens to the sound of his mother bustling in the kitchen and Simm complaining in the next room. He looks out his small window at the starry sky, rubbing his bruised cheek. He smiles. He remembers his past life's regrets, but as he feels the throb of his new black eye, he knows he won't make the same mistake twice. In this life, he is going to find his adventure. 

### **Notes for the Author:**
*   **Worldbuilding Integration:** Wicket’s muttering of the "water knockers" charm is a great early introduction to the local superstitions. It sets up Wicket's character perfectly without requiring an infodump. 
*   **Stat Integration:** Mentioning Tal practicing his *Coordination* on the logs introduces the concept of stats as a mortal philosophy rather than a game mechanic. He isn't "grinding a skill"—he's just a boy trying to train his natural attributes.
*   **Tone Check:** The fight with Wicket perfectly establishes the "rough-and-tumble" boyish charm of the era (very Tom Sawyer/Huck Finn), contrasting with the lofty, magical reincarnation prologue.












Here is a comprehensive outline for Chapter One that hits all your required beats while firmly rooting the story in the world of Aratta and the Corvish Isles.

### **Chapter 1: A Second Chance and a Muddy Start**



**Scene 3: The Mishap and The Escape**
*   **The Crime:** Cut to the present action (Tal is around seven or eight years old). Tal is trying to practice his "Coordination" (one of the six mortal attributes he’s heard delvers talk about) by daringly balancing on a boom of spinning, bark-stripped logs in the sawmill pond. 
*   **The Fall:** Simm catches him and yells a threat to tell their mother. Distracted, Tal slips and plunges into the freezing, filthy, pine-tar-laced mud of the Varn. 
*   **The Chase:** Knowing Martha will skin him alive for ruining his only good woolen tunic, Tal tries to sneak back into the house through a window. However, Simm has already tattled. Martha is waiting in the kitchen, wooden spoon in hand, loudly complaining to the rafters about her "wayward, yellow-haired trial of a boy."
*   **The Trick:** Tal uses his wits. He sneaks around to the chicken coop (or a neighbor's goat pen), opens the latch, and tosses a rock against the back door. When Martha marches out the back to inspect the noise and corral the escaping animals, Tal scrambles in through the front window, grabs a chunk of bread, and escapes out the same window, sprinting for the safety of the docks.

**Scene 4: A Territorial Dispute (Meeting Wicket)**
*   **The Secret Base:** Tal retreats to his favorite hiding spot: an overturned, rotting logging skiff half-buried in the reeds downriver. 
*   **The Intruder:** When he arrives, he finds the spot already occupied by a sallow-faced, dark-curly-haired boy he's never seen before. The boy (Wicket) is wearing ratty clothes, fiddling with Tal's secret stash of river-glass, and nervously humming a Corvish superstition-song to ward off river-trolls. 
*   **The Brawl:** Tal demands the boy leave his base. Wicket, defensive and used to being pushed around due to his drunk father, refuses. Tal charges him. 
*   **The Fight:** It’s a classic, messy boys' fight. Wicket fights dirty—throwing handfuls of river mud and kicking shins. Tal uses his superior reach (inherited from Long Tom) to tackle Wicket. They roll around in the muck, completely ruining whatever was left of Tal's clothes.
*   **The Truce:** They eventually tire out, both panting and covered head-to-toe in foul-smelling mud. Wicket makes a biting, sarcastic comment about Tal looking like a "swamp-goblin." Tal laughs. Wicket laughs. 
*   **The Introduction:** The tension breaks. Wicket introduces himself, explaining he just moved to town. Tal splits his stolen chunk of bread with him. In the span of ten minutes, they go from mortal enemies to blood brothers. Wicket nervously asks if there are actually monsters in the nearby caves; Tal enthusiastically promises to show him. 

**Scene 5: Taking the Lumps**
*   **Sneaking Home:** The sun begins to set. Tal knows he can't hide forever and sneaks back home with Wicket trailing behind, fascinated by his new brave friend. 
*   **The Ambush:** Tal tries to slip through the front door, but little Elsie is waiting. She tries to hide him behind her tiny frame, but it's useless—he smells like a swamp. 
*   **The Punishment:** Martha descends upon him. Wicket watches from the window as Tal bravely takes his scolding and his extra chores without complaining. Tal glances out the window and shoots Wicket a muddy grin. 
*   **Closing Note:** Tal reflects that while his mother’s punishments were a terror in his youth, and the town was small and mundane, having a best friend made it all feel like the start of a true adventure. It was a perfect, cozy life... right up until the night they found the dead man in the graveyard.







"""
