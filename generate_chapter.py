import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Banjo takes offense at the idea of little singing men who dig for a living. This puzzles Trip, and Banjo can't really explain it. He finally settles with "it's a hound thing. Deal with it."
Turning his attention back to the priest, Trip asks how a regular guy gets his numbers up, assuming it's just hard work, aging, and training. Sydney confirms this is the honorable way, but solemnly mentions rumors that the elven nobility possess magical means of artificially enhancing their attributes to maintain their supremacy over humanity. Sydney admits he doesn't know the details, but views it as an abomination.
The conversation lulls as they trek up a steep rise. Banjo suddenly freezes, cutting off a thought about whether giant coons have their own special "Thieving" stats. He alerts Trip to a scent on the wind: horses, sweat, and black powder.
A pair of horsemen crest the ridge ahead, effectively cutting off their path. They are rough-looking men wearing Corvish military uniforms (tailcoats, sturdy riding boots) and armed with cavalry sabers and short, nasty-looking carbines. Trip unshoulders his musket and holds it at the ready.
Father Sydney is initially relieved. He recognizes them as Corvish Dragoons, likely part of Laird MacTavish's company from Glenrowan. He calls out a greeting, but the dragoons don't recognize the priest, as he is just a country vicar from a backwater parish.
The lead dragoon's eyes lock onto Trip. To the soldier, Trip is a heavily-armed, imposing stranger who speaks in an odd manner, traveling with a large dog. Suspicious, the dragoon demands that Trip hand over his musket and submit to having his hands bound for the ride back to the Laird.
Trip, who just spent the night bleeding for the Bannish people and is exhausted from saving a village, has no intention of being tied up like a criminal. Showing some stubborn independence, Trip firmly but politely declines the order. I reckon my hands'll stay right where they are, friend.
The dragoons don't take kindly to defiance. Both men draw their carbines, the flintlocks clicking ominously as they level the barrels at Trip's chest.
Banjo immediately steps in front of Trip, his hackles raised and a vicious, rattling growl building deep in his chest. In Trip's mind, Banjo declares he's ready to pull these riders right off their saddles.
Trip stares down the barrels of the Corvish carbines, his thumb hovering over the hammer of his own musket, leaving the reader on a tense standoff.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.






























### **Chapter Ten: The Laird of Glenrowan**
**Core Focus:** De-escalating the standoff, escort to the manor, and the social challenge of gaining MacTavish's aid.

*   **Scene 1: Appalachian Diplomacy (Fenshire Style).**
    *   Picks up right at the standoff. Father Sydney tries to invoke Church authority, but Trip steps in with some disarming, folksy charm. He leans hard into his "Fenshire" persona, acting like handing over a gun to a stranger is just a bizarre breach of manners where he comes from. 
    *   Trip offers a compromise: he unprimes his pans and empties his powder horn into Sydney's satchel. A gun without powder is just a club. The Sergeant begrudgingly accepts this display of good faith. 
    *   They are escorted the rest of the way to Glenrowan. Banjo trots alongside the cavalry horses, telepathically critiquing the dragoons' riding posture to Trip.
*   **Scene 2: Glenrowan Manor.**
    *   They arrive at a fortified stone keep surrounded by a bustling military camp. It's an immersive slice-of-life scene: soldiers cleaning muskets, campfires, the drone of distant bagpipes, and the overwhelming smell of roasting meats. Banjo nearly loses his mind at the scent of the mess tents.
*   **Scene 3: Holding Court.**
    *   They are brought before Laird Lachlan MacTavish. The Laird is exactly as described: barrel-chested, mutton-chopped, eating a hearty stew, and blending aristocratic authority with rustic Bannish charm.
    *   *The Social Challenge:* MacTavish is sympathetic to the village's plight, but deploying his dragoons is a massive risk. He interrogates Trip, testing the man's mettle. He tries to browbeat Trip, but Trip's lack of modern deference—meeting the Laird eye-to-eye and speaking plainly—wins MacTavish's respect. 
    *   The turning point: Trip describes the necromancy. MacTavish stops eating. Sydney confirms the use of violet moon magic. 
    *   MacTavish heavily invokes Saint Michael, realizing this isn't a mere raid but an Everdark incursion. He orders the dragoons to saddle up.
    *   *The Clincher:* MacTavish tosses a thick venison sausage to Banjo, praising the dog's build. Banjo instantly declares MacTavish the greatest human alive (next to Trip), cementing a humorous bond between the dog and the Laird.

    


### **Chapter Eleven: The Violet Twilight**
**Core Focus:** The return ride, the Napoleonic military action, and the sniper-shot resolution setting up the future.

*   **Scene 1: The Ride Back.**
    *   The dragoons move out with disciplined speed. Trip is given a sturdy Highland pony (which he rides adequately enough for a country boy, though Banjo mocks him for looking like a sack of potatoes).
    *   Tension mounts as the sun begins to set. The yellow moon and the bruised-plum (violet) moon begin to rise. The air grows cold and heavy with magic. 
*   **Scene 2: The Village Besieged.**
    *   They arrive at the rim of the valley just in time. The twilight has fallen, and the resurrected gnolls are already swarming the village barricades. Hamish, Bider John, and the local militia are fighting desperately, but they are buckling under the weight of monsters that won't stay dead.
*   **Scene 3: Volleys and Bayonets.**
    *   *Sharpe's Rifles action:* The dragoons dismount and form a firing line. MacTavish bellows orders. The rolling crash of disciplined volley fire tears into the gnoll flank. 
    *   Trip joins the line. Amidst the chaos, he falls into the rhythm of a soldier. Banjo acts as a skirmisher, darting in to cripple the undead so the dragoons can crush them.
*   **Scene 4: The Outworlder Sniper.**
    *   Through the gunsmoke, Trip spots the source of the trouble: a hunched, cloaked Everdark Shaman (the necromancer) standing on a distant ridge, wielding a staff glowing with violet light. 
    *   The distance is extreme for a smoothbore musket, but Trip's naturally immense Finesse, Agility, and Might come into play. He steadies his stolen musket, accounts for the wind, and takes the impossible shot.
    *   The heavy lead ball shatters the necromancer's staff and clips the shaman. The violet magic breaks, and the undead gnolls collapse into lifeless ash and bone. The wounded necromancer shrieks and flees into the Everdark shadows—a lingering threat for a future story.
*   **Scene 5: A Soldier's Life (Resolution).**
    *   The village is saved. Cheers go up from the militia.
    *   MacTavish claps Trip on the back, astonished by the marksmanship. He offers Trip a permanent, paid position as a scout in his Dragoon company, noting that a Fenshire man with a dog like Banjo is exactly what his border patrols need.
    *   Trip accepts. The act ends on a cozy, triumphant note around a roaring campfire in the village center. Trip cleans his musket, Father Sydney says a prayer of thanks, and Banjo finally gets his long-awaited feast of scraps.



### **Chapter Ten: The Laird, the Loot, and the Sausages**
**Theme:** Socializing, slice-of-life logistics, gear upgrades, and the "Fenshire" ruse.
*   **Meeting the Laird:** Trip, Sydney, and Banjo are ushered into the bustling courtyard of Glenrowan. They meet Lachlan MacTavish, who is currently drilling his dragoons. Lachlan is hearty, booming, and clasping his stomach as described. Sydney quickly briefs him on the gnoll horde and the necromancer. 
*   **The Fenshire Ruse Tested:** Lachlan is suspicious of Trip's odd accent and colloquialisms ("Well... how 'bout that?"). Sydney smoothly introduces him as a volunteer from the deep bogs of Fenshire. Lachlan buys it, laughing heartily at the "backward swamp-dweller," and is deeply impressed when Sydney recounts Trip's kill count.
*   **Cozy Logistics & Loot:** While Lachlan orders the dragoons to saddle up, we get a great slice-of-life military prep scene. 
    *   *Trip's Gear:* The local quartermaster issues Trip a proper military rifle (a Corvish equivalent to the Baker rifle—rifled barrel, highly accurate, slower to load but perfect for a skirmisher) and a powder horn of high-grade military powder. 
    *   *Banjo's Feast:* Banjo finally gets his due. Trip sneaks him over to the keep's kitchens, where a terrified but generous cook throws the "hero hound" a string of plump sausages. Banjo is in absolute heaven, telepathically critiquing the seasoning like a culinary expert.
*   **Mounting Up:** Lachlan offers Trip a horse. Trip admits he's no cavalryman but can run all day (high Endurance). Lachlan assigns Trip to move out with his forward scouts. As the violet moon rises, the dragoons ride out to save the glen, with Banjo and Trip leading the way.

### **Chapter Eleven: The Battle of the Glen (Act 1 Capstone)**
**Theme:** Large-scale action, tactical skirmishing, and a job offer.
*   **The Siege at Dusk:** The dragoons arrive at the ridge overlooking the village. The barricades Hamish and Bider John built are under heavy assault by a massive horde of gnolls and a terrifying vanguard of undead beasties glowing with violet magic. In the backline stands the necromancer (could be a corrupted human elf-friend, a goblinoid, or a dark magic adept).
*   **Skirmisher Tactics:** Lachlan prepares for a heavy cavalry charge down the basin, but notes that the necromancer is using magic to spook the horses. Trip volunteers to take out the magic-user. 
*   **The Assassination:** Trip and Banjo slip through the dark, bypassing the main horde. We see the synergy of Earth-hunting tactics applied to fantasy warfare. Banjo causes a massive, targeted distraction—tearing through the necromancer's bodyguard—while Trip sets up a sniper position on a rocky outcropping. He uses his new rifled musket, takes a breath, and puts a lead ball cleanly through the necromancer's chest.
*   **The Charge:** With the necromancer dead, the undead crumble to ash and the regular gnolls panic. Lachlan and the dragoons thunder down the hill to the drone of Bannish bagpipes, breaking the horde in a glorious, decisive clash of cozy military violence. 
*   **The Capstone / The Offer:** The aftermath is full of camaraderie, smoking powder, and back-slapping. Hamish and the village are saved. Lachlan MacTavish shares a flask of good scotch with Trip. Recognizing that Trip's stats, tracking skills, and aim are a profound asset, Lachlan offers him a permanent commission as a Chief Scout for the Bannish military forces. The pay is good, the cause is just, and Banjo telepathically points out that army camps have *mess tents*. Trip looks at the stars, accepts the offer, and officially begins his new life in Corva. 

***

**Why this works for your goals:**
*   **Worldbuilding:** It naturally grounds the "stats" as an in-world science rather than a magical UI, fitting your "natural philosophy" concept. 
*   **Vibe:** It seamlessly shifts the story from "survival horror" to the desired "Sharpe's Rifles" military/scouting loop. You get the smell of black powder, the joy of acquiring new gear (loot), and the camaraderie of the military camp.
*   **Character Arcs:** Banjo gets a comedic payoff (the sausages), Father Sydney gets to prove his loyalty, and Trip finds a pragmatic, down-to-earth reason to stay and fight in this crazy new world: honest work with good people.

"""