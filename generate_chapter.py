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

Chapter six starts with Tal summarizing the two days following Jasper's arrival. With Long Tom Sager home, the Sager household runs like a disciplined ship. Tom lays down the law, and Tal is forced into playing the part of the dutiful son.
When Martha mentions Tal's recent skiving, Tom lays down the law and sets Tal to scrubbing the hearth and chopping kindling. Tal works without complaint, depriving Simm of any opportunity to tattle.
Martha is pleased, and Jasper Moray is largely left alone, though Tal notes that he's in and out of the house all day, off to Tal-knows-not-where, since he's too busy playing the dutiful son to snoop.
Tal's reveals that during this time, his mind was consumed entirely by the "dormant candle" of his mana core. He desperately wishes he could follow Jasper and wheedle him for more tidbits, but Tom keeps the family in line.
On the morning of the third day, Tom departs on the company barge with a fresh load of timber. As soon as  the barge is out of sight and Martha turns her back to tend to a boiling pot, Tal drops his chores and bolts out the back door.
We end summary mode and Tal tells in the normal manner how he tracks down his friends. Elsie tags along with him this time, having also escaped her chores. Maybe he's a bad influence on her.
Tal and Elsie spot and gather Wicket, and the three of them head to the cooper's shop to find Cord and Clary. They find the siblings taking a break outside their father's workshop. Unlike Tal and Elsie, the pair dutifully ask permission before heading off with their friends, and Tal leads them all to the old sawmill. It's the best spot to have a covert meeting.

You can stop there and we'll edit before I provide the next section.



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


*   **The Revelation:** Tal breathlessly relays everything he learned from the scholar. He taps his chest, explaining that everyone possesses a "mana core," a sleeping engine of magic. 
*   **The Reactions:** 
    *   *Clary* (smelling of toasted oats and sawdust) rolls her eyes, playfully mocking Tal's "delver phase" and telling him he's more likely to summon a stomach ache than a fireball.
    *   *Cord* is pragmatic, asking what good a glowing crystal is if it doesn't help chop wood or track a deer. 
    *   *Elsie* is thoroughly amazed and believes Tal probably already has magic. 
*   **The Call to Action:** Tal asks if any of them know how to force a mana core to awaken. While Cord and Clary haven't a clue, Wicket puffs up. Despite his superstitions about magic, Wicket claims his perfect memory has retained a foolproof method gathered from an old Corvish bargeman's song. 

**Scene 3: Wicket's Hogwash Ritual**
*   **The Setting:** The group heads to the edge of town, just where the unpaved streets give way to the imposing, ancient pine stands. 
*   **The Ridiculous Instructions:** Wicket confidently dictates the "ritual" to wake the inner fire. It is absolute hogwash. He tells Tal he must smear cold river mud directly over his heart (where the core sits), eat a bitter, green pinecone to "shock" the spirit, spin in a circle to mimic an eddy, and recite a specific nursery rhyme backward.
*   **The Comedic Failure:** Tal is so desperate for magic that he completely ignores his dignity (and the intellect of his past life). He actually performs the ritual. 
*   **The Result:** Cord and Clary are practically doubled over with laughter. Tal chokes on the bitter pine sap, gets dizzy from spinning, and falls flat on his back in the dirt. No magic happens; he just gets a dizzy spell and a bad taste in his mouth. Clary ribs him mercilessly, while sweet Elsie pats his muddy head and tells him he looked very magical while falling. 

**Scene 4: The Nightmare in the Pines**
*   **The Tone Shift:** The lighthearted, boyish comedy is abruptly shattered by a raspy, cruel laugh dropping from the branches above them. 
*   **Enter Gobber Dob:** Urian Dobbin shimmies down the massive trunk of a pine tree with terrifying, spider-like speed. The narrative highlights his unsettling physique: impossibly long, spindly arms, bowed legs, shifting pale eyes, and a mouth of yellowed teeth. The smell of pine tar, sour sweat, and cheap chewing tobacco hits the kids immediately.
*   **The Confrontation:** Dob mocks Tal's pathetic display in the dirt. However, his attention quickly shifts to Clary. Dob steps uncomfortably close to her, his pale eyes roaming over her sturdy frame. He makes a skin-crawling, highly inappropriate comment about her growing up nicely, flashing a leering, yellow-toothed grin.
*   **The Protective Instinct:** The teasing between the friends vanishes instantly. Cord steps squarely in front of his sister, his face hardening as his hand drops toward his heavy woodworking knife. Without hesitation, Tal and Wicket step up to flank Cord, balling their fists. Tal's boyish fantasies of heroism are suddenly replaced by the very real, terrifying urge to protect his friends.
*   **The Retreat:** Gobber Dob laughs a rattling, cruel laugh at the boys' posturing. He spits a stream of dark tobacco juice right near Tal's muddy boots, implying they aren't worth his time to beat up *yet*. He turns and lopes off into the deeper woods.
*   **Conclusion:** Shaken, the group doesn't linger. Tal and Cord grab Clary and Elsie's hands, and they all hurry back toward the safety of the Company town. The encounter solidifies Gobber Dob as the walking nightmare of Larchleah, planting the seeds of genuine terror that will pay off during the murder plot later.


### Chapter Six Outline: The Inner Fire and the Pine-Tar Nightmare

**Scene 2: The Core Council**
Tal excitedly explains what he learned from the traveling scholar: the silver diagnostic disc, the stats, and most importantly, the dormant mana core inside everyone's chest. He tells them he needs to figure out how to "light the candle" so he can learn magic.
*   **The Reactions:** 
    *   *Cord* is highly skeptical, noting that magic is for wealthy city dandies and elves, not river-rats. 
    *   *Clary* rolls her eyes, agreeing with her brother, playfully poking fun at Tal's grand ambitions and telling him to keep his head out of the clouds. 
    *   *Elsie* is just thrilled, fully believing Tal is going to be a grand wizard.
    *   *Wicket*, however, takes it deadly seriously. He claims he knows exactly how to awaken inner magic, recalling a highly superstitious ritual sung by a drunk deckhand about "waking the inner fire."

**Scene 3: Wicket's Hogwash Ritual**
*   **Into the woods:** Wicket refuses to do the ritual in town where "the iron horseshoes on the road will scatter the magic." He leads the skeptical group to a secluded clearing just past the tree line of the oak and pine forest.
*   **The ridiculous requirements:** Wicket's ritual is a hodgepodge of Corvish folklore and utter nonsense. It involves Tal rubbing river mud on his forehead, holding a specific dried frog bone, standing on one leg, and chanting a rhyming Corvish nursery song backward while visualizing a fire in his belly.
*   **The attempt:** Desperate enough to try anything, Tal actually does it. The scene plays for maximum comedy. Tal is red-faced, straining his willpower, hopping on one leg, and chanting gibberish.
*   **The embarrassment:** Clary and Cord are laughing so hard they are leaning against each other. Elsie tries to mimic Tal's one-legged stance in solidarity but keeps falling over. Tal finally gives up, exhausted, muddy, and feeling utterly humiliated. He realizes Wicket's folklore is completely useless, and the system of this world requires a real key, not children's games.

**Scene 4: Enter the Nightmare**
*   **The interruption:** The laughter is abruptly cut short by a shower of pine needles and bark. A raspy, wet chuckle echoes from above.
*   **Gobber Dob descends:** Urian "Gobber Dob" Dobbin drops from the canopy of a massive pine with terrifying, unnatural agility. Describe his sallow skin, sparse greasy hair, and his disproportionately long, spindly arms and bowed legs. The smell of sour sweat and chewing tobacco hits the kids immediately.
*   **The creep factor:** Dob mocks Tal's "little fairy dance." He then notices Clary. His pale, beady eyes lock onto her, and he steps closer, leering at her. He makes a horrid, skin-crawling comment about how the cooper's girl is "growing up right pretty" and reaches out a filthy, resin-stained hand to touch her hair.
*   **Protectiveness:** The comedy of the previous scene instantly vanishes. Cord forcefully shoves Clary behind him, his jaw set in defiance. Tal instantly shakes off his humiliation and steps up right beside Cord, balling his fists. Wicket is paralyzed with terror, clutching his protective charms, but doesn't run away.
*   **The threat:** Dob pauses, looking at the boys' fierce, if small, resistance. He spits a stream of black tobacco juice onto the toe of Tal's boot. He flashes a mouth of rotting yellow teeth, warning the "little river rats" that they shouldn't play out in the deep woods, because accidents happen and things disappear in the Everdark shallows.
*   **The retreat:** Dob uses his massive arms to effortlessly swing back up into the lower branches of the pine and scuttles away into the canopy. Shaken, the kids don't linger. They gather Elsie and quickly retreat to the safety of the muddy, sunlit streets of Larchleah. 

**Scene 5: A New Resolve**
*   **The aftermath:** Back in town, the group catches their breath. Clary tries to brush the encounter off with a tough facade, but she is clearly rattled by Dob's leer. Cord is fuming, swearing he'll tell his father. 
*   **Tal's Epiphany:** Tal washes the mud off his face in a horse trough. The humiliation of the failed ritual is gone, replaced by a cold dose of reality. The world has real, terrifying monsters in it—and some of them are men like Gobber Dob. 
*   **Setting the path:** Tal realizes that if he wants to protect his sister and his friends, and if he wants to actually claim his destiny in this second life, he can't rely on childish nonsense or pretend play. He needs real power. He resolves that, one way or another, he is going to corner Jasper Moray and pry the actual secrets of the world out of the scholar.

"""
