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




Here is a comprehensive outline for Chapter Ten that seamlessly integrates your plot points, worldbuilding rules, and character voices. 

### **Chapter Ten Outline**

**Beat 1: The Fenshire Compromise**
*   **The Standoff:** The chapter opens exactly where Chapter Nine left off. Father Sydney steps forward to broker peace, invoking his authority as a Canthican vicar, but the dragoons are jumpy. They fought off gnolls all night and aren't inclined to trust a blood-stained stranger and a snarling hound. 
*   **Trip Steps Up:** Moved by the priest's earnest attempt to defend him, Trip decides to de-escalate. He lowers his musket slightly and leans hard into his new "Fenshire" identity. He puts on his best folksy drawl and politely informs the dragoons that where he comes from, aiming a loaded weapon at a stranger who's just trying to ask for directions is a severe breach of manners.
*   **The Wager of Pride:** Trip offers a compromise. He smoothly unprimes his pan, letting the powder spill into the heather, and tosses his powder horn to the riders. He tells them a gun without powder is just an awkward club, and surely two brave Corvish dragoons ain't afraid of a man with naught but a stick.
*   **Stand Down:** The dragoons' pride is pricked. Grudgingly respecting his nerve, they lower their carbines and accept the display of good faith—though they pragmatically demand he hand over his leather bag of lead shot, too. 

**Beat 2: Critiques and Campfires**
*   **The Escort:** The group resumes the trek, now escorted by the two mounted dragoons. Trip carries his useless musket, keeping pace with the horses.
*   **Banjo's Commentary:** Banjo trots alongside the horses, maintaining a telepathic running commentary. He is thoroughly unimpressed by the dragoons' mounts. He critiques their smell ("like big, dumb dogs that only eat salad") and speculates that with all their prancing, they couldn't tree a coon if it fell on them. Trip has to stifle a few laughs, earning suspicious glares from the cavalrymen.
*   **Approaching Glenrowan:** As they crest the final ridge, Glenrowan comes into view. It is a fortified stone manor house sitting on the edge of a mid-sized Bannish town, surrounded by a bustling military encampment. 
*   **Sensory Details:** We get a rich slice-of-life scene of the Bannoch military camp. Trip takes in the sights of hardy men in kilts and tailcoats cleaning their muskets, the drone of Bannish bagpipes echoing off the valley walls, and the crackle of campfires.
*   **Banjo's Agony:** The scent of roasting meats from the mess tents wafts over the group. Banjo practically loses his mind, begging Trip for a detour. (*"Trip, I'm wasting away! A dog can't fight a war on half a dry biscuit!"*)

**Beat 3: The Laird's Stew**
*   **Entering the Manor:** Trip, Father Sydney, and Banjo are escorted into the manor's great hall. It is rustic but authoritative, decorated with clan tartans, hunting trophies, and weapons.
*   **Meeting MacTavish:** They are presented to Laird Lachlan MacTavish. The barrel-chested, mutton-chopped commander is seated at a heavy oak table, enthusiastically devouring a bowl of hearty stew. He blends aristocratic authority with a rolling, amiable Bannish brogue. 
*   **A Reluctant Commander:** MacTavish recognizes Father Sydney's collar and affords the priest proper Canthican respect. However, when Sydney begs for the dragoons to relieve their village, Lachlan sighs heavily. He explains that Glenrowan and its surrounding crofts were also hit hard by gnolls. He is reluctant to risk his cavalry by sending them across the open moor when he might need them to defend his own walls tonight.

**Beat 4: The Everdark Threat**
*   **Testing the Waters:** Lachlan turns his sharp gaze on Trip, taking the measure of the blood-stained "Fenshire" man. He attempts to browbeat Trip, demanding to know what business a southerner has bringing trouble to his glen.
*   **Standing Ground:** Trip refuses to be intimidated. Lacking modern deference, he meets the Laird eye-to-eye and speaks plainly, resting his hands on his hips. *"I ain't looking for trouble, Laird, it found us. And if you don't send those men, a lot of good folks are going to die."* 
*   **The Turning Point:** Lachlan actually likes the man's spine. Trip then brings up the true nature of the fight in the church, casually describing the dead gnoll they had to drag out into the sunlight. Father Sydney confirms the beast was animated by violet moon magic.
*   **Escalation:** Lachlan drops his spoon. The stew is forgotten. He realizes this isn't just a bold pack of Everdark scavengers—it's a coordinated necromantic incursion. He immediately invokes Saint Michael and bellows for his lieutenants, ordering the dragoons to saddle up at once.

**Beat 5: Venison and Rifles**
*   **A Bribe for a Hound:** While barking orders, Lachlan fishes a massive, dripping chunk of venison from his stewpot and tosses it to Banjo, praising the hound's handsome blue-tick markings. Banjo snaps it out of the air, swallows it whole, and instantly telepathically declares Lachlan the greatest human alive (second only to Trip).
*   **The Strohl-Martin Rifle:** Lachlan notes the poor quality of the smoothbore militia musket Trip is carrying. He asks if Trip is a marksman. Trip replies with his usual modesty, noting he usually hits what he aims at, but without proper rifling in the barrel, he can't promise much past fifty yards. 
*   **An Upgrade:** Lachlan proudly reveals that he recently acquired a crate of Strohl-Martin rifles (a Corvish equivalent to the Baker rifle). He explains that the grooved barrel makes it deadly accurate at long range, though it takes a fair bit more elbow grease and time to load. He tosses one to Trip, along with a fresh powder horn and patched lead balls, suggesting Trip put his Outworlder... *ahem*, Fenshire... marksmanship to good use.

**Beat 6: Riding to the Rescue**
*   **Saddling Up:** The courtyard is a flurry of organized chaos as twenty dragoons mount up. Lachlan offers horses to Trip and Father Sydney.
*   **Equestrian Troubles:** Trip sheepishly admits he's a lot more comfortable on his own two feet (or behind the wheel of a truck, though he keeps that part to himself). Father Sydney, surprisingly adept, gives Trip a rapid-fire, bare-bones lesson on how to stay in the saddle without breaking his neck.
*   **The Ticking Clock:** Banjo bounds eagerly around the horses, ready for a fight. The shadows in the courtyard are stretching long. Trip looks up to see the sun beginning to dip behind the jagged mountain peaks, meaning the yellow and violet moons will soon rise. 
*   **Departure:** With Lachlan at the head of the column, Trip clinging awkwardly but determinedly to his saddle, and Banjo leading the charge, the cavalry rides out of Glenrowan to save the village just as dusk begins to fall.








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




### **Chapter Eleven: The Battle of the Glen (Act 1 Capstone)**
**Theme:** Large-scale action, tactical skirmishing, and a job offer.
*   **The Siege at Dusk:** The dragoons arrive at the ridge overlooking the village. The barricades Hamish and Bider John built are under heavy assault by a massive horde of gnolls and a terrifying vanguard of undead beasties glowing with violet magic. In the backline stands the necromancer (could be a corrupted human elf-friend, a goblinoid, or a dark magic adept).
*   **Skirmisher Tactics:** Lachlan prepares for a heavy cavalry charge down the basin, but notes that the necromancer is using magic to spook the horses. Trip volunteers to take out the magic-user. 
*   **The Assassination:** Trip and Banjo slip through the dark, bypassing the main horde. We see the synergy of Earth-hunting tactics applied to fantasy warfare. Banjo causes a massive, targeted distraction—tearing through the necromancer's bodyguard—while Trip sets up a sniper position on a rocky outcropping. He uses his new rifled musket, takes a breath, and puts a lead ball cleanly through the necromancer's chest.
*   **The Charge:** With the necromancer dead, the undead crumble to ash and the regular gnolls panic. Lachlan and the dragoons thunder down the hill to the drone of Bannish bagpipes, breaking the horde in a glorious, decisive clash of cozy military violence. 
*   **The Capstone / The Offer:** The aftermath is full of camaraderie, smoking powder, and back-slapping. Hamish and the village are saved. Lachlan MacTavish shares a flask of good scotch with Trip. Recognizing that Trip's stats, tracking skills, and aim are a profound asset, Lachlan offers him a permanent commission as a Chief Scout for the Bannish military forces. The pay is good, the cause is just, and Banjo telepathically points out that army camps have *mess tents*. Trip looks at the stars, accepts the offer, and officially begins his new life in Corva. 


"""