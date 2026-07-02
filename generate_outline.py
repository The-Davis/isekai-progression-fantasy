import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter twelve. This will deal with Trip and Banjo in the aftermath of the battle, helping the people of the chapel glen rebuild their lives, among other things.
I think this should cover it, but see if it needs anything more, please:
Late in the morning after the battle, nearing noon, Trip finally wakes up stiff and sore. Banjo is still snoozing, but wakes up when Trip stirs. There should be a brief but comical interaction between the two, leading into comical food demands from Banjo when Maisie comes in to check on them.
Some social interactions that continue to show Trip as a kind and compassionate man towards children should occur. Eventually, he joins Hamish, John, and Sydney in the village. Lachlan left with his dragoons while Trip was still sleeping, but will reportedly return later with aid.
There should be some discussion and debate about what to deal with first. Will the gnolls return tonight? Everyone decides they are confident they will not, but someone had best hunt down the hole to the Everdark they crawled out of.
"""

"""Let's work out the outline for the second act:
The rest of the story is going to be episodic, "cozy violence" that mixes "A Soldier's Life" with "Sharpe's Rifles": no-system, stats-lite LitRPG with a loop of action, power ups, loot, socializing, and slice of life set in a Napoleonic/Georgian era of tech and conflict.
Our first act introduced a narrow picture of the "no-system, stats-light litrpg", magic, and the very basics of politics and life in the world of Rhule.
The second act will expand on those themes while routing Trip towards his personal role in the world.
Trip and Banjo need to wind up as scouts (well, one scout who has a dog) in the Corvish military in order to tell the tales I want to tell, but I think there's potential for an act (about ten to twelve chapters of material) steering him in that direction.
I think we can show a lot of interesting things while organically building the world and characters:
1. Trip can help repair the church while learning about the world from Father Sydney and Bider John. More about stats, magic, etc. Both can steer him towards Lachlan as a good source on politics and how a man might make his living. This can be where we establish firmly that they know of no way back to the Outworld.
2. Lachlan can get his promised hunt with Banjo and Trip, during which they can find the Everdark exit that the gnolls ventured out of and bomb it with gunpowder to collapse it. Once secured, the dragoons will return to Glenrowan.
3. Introduce the fact that the army requires baseline stats for its soldiers.
4. Get Trip tested, perhaps with a trip to the parish church and a monster encounter along the way.
5. Establish that magic is not *common* or rare. There are two very weak practitioners in Glenrowan, though none in the nameless chapel glen.
6. Have one of the dragoons train Trip in basic drill and get him comfortable reloading under stress (Trip should recognize this as a weakness)

Those elements should be in no particular order other than "rebuilding the chapel glen" would be first, since we'd pick up right where we left off. I imagine finding and sealing the Everdark entrance the gnolls used would be early on too.
There should be other elements of story and character growth to logically bring Trip from "I don't know what to do next" to "I should do basic training with the Corvish Army so I can become a paid scout".

"""




write_file(generate_outline_prompt(next_section=next_section))



"""
*   **The Action:** Trip's general contractor instincts kick in. He organizes the militia boys to clear rubble, sister the splintered joists, and cap the hole using salvaged timbers.
*   **Worldbuilding:** Over a hard-earned lunch, Father Sydney and Bider John bring Trip the bad news: Outworlders arriving on Rhule are the result of random, one-way cosmic accidents. There is no known magic or portal to send him back. Trip takes the news with stoic, folksy pragmatism—there's no use crying over spilled milk, and at least he has his dog. He officially accepts that Rhule is his new home. 

**Chapter 13: Magic and Mortar**
*   **The Setup:** As work continues on the chapel, Trip gets to know Bider John, whose dour exterior thaws when he sees Trip isn’t afraid of manual labor. 
*   **Worldbuilding:** Bider John and Father Sydney explain the baseline realities of magic. It is neither a myth nor an everyday commodity. True mages are rare, mostly hoarded by the Elves and elf-friends. The Chapel Glen has none, relying purely on faith and sweat. 
*   **Character:** Banjo acts as the "foreman," mostly sniffing out dropped food and complaining about the noise of the hammers. Trip realizes he needs a permanent way to earn his keep in this world. Farming is out, and contracting seems difficult without tools or capital. 

Trip joins Hamish, Bider John, and the locals in clearing rubble and assessing the church.
*   **Lore/Plot:** As Trip uses his general contractor skills to brace the sagging floor and sister the ruined joists, he talks quietly with Father Sydney. Trip finally asks the big question: *How does a man get back to the Outworld?* Father Sydney gently delivers the hard truth—in two thousand years, no one ever has. It is a one-way trip. 
*   **Character:** Trip takes a private moment to grieve his old life, his property, and his grandmother's grave. Banjo senses his melancholy and offers a remarkably grounded, canine perspective: *Earth didn’t have double-moons or giant coons, but the dirt here smells fine, the folks are decent, and we’re still a pack.* Trip accepts his new reality. He needs to earn a living in Rhule.

**Chapter 13: Contractor in a Kilt**
*   **Action/Focus:** Slice-of-life/Rebuilding. A montage-like chapter of hard, satisfying physical labor. Trip earns the deep respect of dour Bider John by showing he isn't afraid of a hard day's work. 
*   **Lore/Plot:** While working, Father Sydney watches Trip effortlessly hoist timbers. He explains more about the physical stats (Might, Finesse, Endurance). Sydney points out that Trip’s "Finesse" (control) is likely what makes him such a good contractor, allowing him to apply his Might perfectly without wasting energy. Sydney suggests that if Trip wants to earn a solid living where his Outworlder ignorance won't be questioned, Lachlan MacTavish’s dragoons are the way to go.
*   **Ending:** Laird Lachlan rides into the glen with a patrol to check on the village. Seeing the church stabilized, he reminds Trip of the hunt he promised Banjo.





**Chapter 14: The Promised Hunt**
*   **The Setup:** Laird Lachlan MacTavish’s dragoons have finished sweeping the glen. Before they return to Glenrowan, Lachlan reminds Trip of the promised hunt. He wants to see the blue tick hound in action.
*   **The Action:** Trip, Banjo, and Lachlan head into the highlands. Banjo is in absolute heaven, effortlessly tracking a massive Bannish stag. Lachlan is astounded by Banjo's tracking speed, which he assumes is due to an insanely high "Wit" and "Finesse" attribute for a beast.
*   **The Twist:** Mid-hunt, Banjo catches a scent that ruins his good mood—the dead-possum stink of the Everdark. He abandons the stag and tracks the foul odor to a hidden cave entrance spewing a faint violet mist. 

**Chapter 15: Fire in the Hole**
*   **The Setup:** The cave is the breach the gnoll horde and the necromancer used to invade the glen. A small remnant of gnolls is guarding the entrance. 
*   **The Action:** A brief, intense skirmish. Trip and Lachlan fight side-by-side. Lachlan is a beast with his cavalry saber, and Trip uses his new Strohl-Martin rifle to pick off the guards. 
*   **The Climax:** To ensure the glen’s safety, Trip uses Lachlan’s spare black powder kegs to rig a controlled demolition. He expertly blows the cave’s overhang, sealing the Everdark tunnel under tons of rock. Grateful for his service, Lachlan formally invites Trip to ride back to Glenrowan as his guest. 

**Chapter 16: The Town of Glenrowan**
*   **The Setup:** The dragoons return to their garrison. Trip gets his first look at a proper, bustling Corvish town. It’s a mix of heavy stone industry and rustic highlands. 
*   **Worldbuilding (Magic):** Trip discovers how "working-class magic" operates. Glenrowan has two weak practitioners: a brewer who uses low-level thermal magic to perfectly ferment his ales, and a blacksmith who uses minor telekinesis to fold heavy steel. It’s practical, blue-collar magic.
*   **The Pivot:** Over a pint at the local tavern, Lachlan pitches the military to Trip. The Corvish Army is always looking for men who don't flinch. However, the Army has strict baseline stat requirements. 

**Chapter 17: Sweating the Fundamentals**
*   **The Setup:** Trip considers the army, but Lachlan assigns a veteran Dragoon—the same grumpy corporal who held Trip up on the moor—to assess him.
*   **The Action/Training:** The corporal puts Trip through the ringer. Trip’s aim is phenomenal, but his reload speed under pressure with a muzzleloader is atrocious by military standards. The dragoon breaks him down, teaching him the Corvish infantry drill. 
*   **Character:** A grueling "training montage" chapter. Trip realizes that hunting from a deer stand is not the same as volley fire. He learns to operate the musket/rifle strictly by muscle memory. Banjo offers hilarious, unhelpful commentary from the shade ("*Just bite 'em, Trip, it's a lot faster than stuffing a ball down a pipe*"). Trip finally masters the combat reload.

**Chapter 18: The Army's Ledger**
*   **The Setup:** With Trip’s combat drills up to standard, Lachlan explains the bureaucracy. To join a line regiment, a man needs a physical attribute (like Might or Endurance) of at least 15. To be a Scout or Rifleman—who get better pay, better rations, and more independence—you need high Agility and Finesse.
*   **The Problem:** Because Trip is an Outworlder ("from the Fenshire bogs"), he has no official parish records. They need to travel to a proper diocesan Parish Church in a neighboring town to get his stats formally measured with a Coda Glass. 
*   **The Plan:** Trip, Banjo, Father Sydney (who needs to report the necromancer attack to his superiors), and a small dragoon escort set out for the larger Parish town.

**Chapter 19: The Road to the Parish**
*   **The Setup:** A travel chapter that expands the scope of the world. As they march through the Bannoch highlands, Father Sydney and the dragoons share tales of the ongoing border skirmishes and the political friction with the Elves in the south. 
*   **Character:** Trip realizes he likes the camaraderie of the soldiers. He enjoys the banter, the marching, and the clear-cut purpose. It feels right. Banjo is just thrilled to be exploring new territory and begging rations from multiple dragoons.

**Chapter 20: Ambush on the Moor**
*   **The Setup:** The violet moon rises early, and the group is ambushed on the road by a localized Everdark threat—perhaps a pack of *Cu Sith* (fearsome, oversized faerie hounds) or a corrupted troll. 
*   **The Action:** Chaos erupts. The dragoons’ horses panic. This time, Trip doesn't freeze or fumble. His rigorous training pays off. He demonstrates "cozy violence" competence, rapid-firing his rifle, staying cool under pressure, and covering the dragoons while Banjo intercepts the beasts in melee. 
*   **The Result:** Trip earns the absolute respect of the dragoons. He is no longer just a guest; he is one of the boys.

**Chapter 21: The Coda Glass**
*   **The Setup:** The group arrives at the sprawling, pre-Collapse Canthican Cathedral of the Parish town. It’s breathtakingly massive, showing Trip the true scale of the Church.
*   **The Measurement:** Trip meets the local Bishop, who produces the Coda Glass—a beautifully intricate, alchemically treated monocle/lens. The Bishop reads Trip’s stats. 
*   **The Results:** Trip's physicals (Finesse, Endurance, Might) are shocking—comfortably in the low-to-mid 30s, placing him on par with elite veteran rangers. 
*   **The Anomaly:** When checking his Magical/Mental stats, the Bishop is confused by a strange "Resonance" anomaly. Unbeknownst to the Bishop, the Glass is picking up Trip's telepathic bond with Banjo. Father Sydney smoothly covers for Trip, passing it off as a quirk of his "Fenshire" heritage. 

**Chapter 22: Taking the Shilling**
*   **The Setup:** With his stats officially recorded on Canthican parchment, Trip hits the threshold for the elite scouting cadres. 
*   **The Climax:** A local Corvish Army recruiter (or Lachlan, acting as a magistrate) sits down with Trip. He offers him the "King's Shilling." Trip takes it, officially enlisting. 
*   **The Wrap-Up:** Trip is outfitted in a proper, tailored green-and-brown Scout's uniform (much to Banjo's approval, as it smells like wool and not dead gnolls). Banjo is officially recognized as a "working military hound" (which means he gets his own ration stipend). 
*   **Ending Note:** Act II ends with Trip and Banjo looking out over the town, finally grounded. He has a job, a uniform, a rifle, and a place in this vast, magical universe. He's ready for whatever deployment the Corvish Army throws at him.











Here is a proposed chapter-by-chapter outline for the second act of your story. It hits all your requested beats while maintaining the “cozy violence,” "Sharpe's Rifles" camaraderie, and the LitRPG-lite natural philosophy elements. 


**Chapter 14: The Hound and the Highlands**
*   **Action/Focus:** Trip, Banjo, Lachlan, and Captain MacFarlane head up into the craggy Bannish highlands. Banjo is in absolute heaven, narrating the hunt in Trip's head with hilarious, food-motivated commentary.
*   **Lore/Plot:** As they track a massive highland stag, Lachlan and Trip bond over hunting and firearms. Trip gets to show off his marksmanship with the Strohl-Martin rifle, dropping the stag cleanly. 
*   **Twist:** Banjo suddenly loses interest in the stag. His hackles go up. He smells the lingering, rotten-egg stench of the Everdark and the purple magic of the escaped Necromancer. The hunt changes from leisure to a tactical sweep.

**Chapter 15: Sealing the Breach**
*   **Action/Focus:** Banjo leads the hunting party to a jagged fissure hidden in a deep, shadowed ravine—an Everdark tunnel the gnolls used to bypass the glen's natural defenses. 
*   **Conflict:** A small remnant guard of Everdark creatures (perhaps mutated cave-spiders or foul-tempered gnoll stragglers left behind by the fleeing necromancer) attack. It's a short, sharp skirmish. Trip and the dragoons fight shoulder-to-shoulder.
*   **Resolution:** Trip uses his contractor's eye for load-bearing stone to identify the cave's weak points. Using a couple of spare powder kegs from MacFarlane’s saddlebags, Trip orchestrates a controlled demolition, permanently burying the Everdark exit. Lachlan is thoroughly impressed. 

**Chapter 16: The King's Shilling**
*   **Action/Focus:** Return to Glenrowan for a venison feast. Trip needs a job, and Lachlan makes his pitch: The Corvish Army needs men who can shoot straight and keep their heads. 
*   **Lore/Plot:** Lachlan breaks down army life. He explains that to join the regular line infantry, a man must pass a physical proving to ensure a baseline *Might* and *Endurance* (usually around 15). But to join the elite specialized companies—like the Rangers, Rifles, or Scouts—a man needs exceptional stats (20+) and a writ from a local parish proving it. 
*   **Magic Setup:** Trip asks if he'll be fighting alongside wizards. Lachlan laughs and points out two locals at the feast—an old woman who uses weak 'Dominion' to brew alchemical hangover cures, and a farrier who uses weak 'Resonance' to mend cracked horseshoes. True battle-mages are exceedingly rare (and mostly elven or elf-blooded nobles). 

**Chapter 17: Bite, Pour, Spit, Tap**
*   **Action/Focus:** Trip realizes that while he's a great shot, he fumbled his reloads terribly under stress during the church fight. He humbly asks Captain MacFarlane to drill him.
*   **Training:** A "Sharpe's Rifles" style training sequence. MacFarlane puts Trip through the grueling manual of arms for reloading under fire. Trip learns to use paper cartridges, drill movements, and how to ignore distractions. Banjo provides comedic relief by trying to "distract" Trip by barking about squirrels and trying to steal Trip's rations while he's loading. Trip masters the muscle memory, increasing his effective 'Agility' with firearms.

**Chapter 18: The Road to the Parish**
*   **Action/Focus:** To get Trip’s stats officially tested for enlistment, Trip, Banjo, and Captain MacFarlane ride out for the larger regional Parish Church, a day's ride away.
*   **Lore/Plot:** On the road, MacFarlane fills Trip in on the geopolitical landscape. We learn more about the northern Bannoch's uneasy relationship with the elven-influenced southern Corvland, and the friction in the capital of Dornon. Trip absorbs this, solidifying his "Fenshire rustic" cover story so he doesn't slip up in the military.

**Chapter 19: The Highland Cu Sith**
*   **Action/Focus:** The Monster Encounter. While crossing a misty stretch of moor, Banjo gives a frantic warning. They are ambushed by a *Cu Sith*—a massive, fae-tainted hound native to the wilds of Rhule (not an Everdark monster, but a natural predator of the magical world).
*   **Combat:** The beast is incredibly fast and shrugs off MacFarlane's carbine shot. Here, Trip’s training pays off. He hits it with his rifle, smoothly and calmly executes his new reload drill under terrifying pressure, and fires a second shot to save MacFarlane. Banjo proves his worth by tangling with the beast just long enough to give Trip the shot, proving they are an elite scout-and-hound team.

**Chapter 20: The Coda Glass**
*   **Action/Focus:** Arrival at the bustling parish town. It's a step up in civilization—cobblestones, merchants, and a grand Canthican church. They meet a Bishop or high-ranking Vicar.
*   **Lore/Plot:** The Testing. The priest uses an alchemically treated *coda glass* to read Trip's attributes. 
    *   *The Reveal:* We get real numbers. Trip's physical stats are highly impressive (Might, Endurance, and Vigor all in the high 20s/low 30s), validating his hard-working Outworlder background. His mental stats are perfectly average. His magical stats are absolute zero. 
*   **Resolution:** The priest issues a sealed writ certifying Trip's stats. He is officially overqualified for the line infantry and perfectly suited for a specialized Scout/Rifleman role. 

**Chapter 21: A Scout's Decision**
*   **Action/Focus:** They return to Glenrowan. Trip sits by the fire with Banjo, looking at the official writ. He has a path forward. 
*   **Resolution of Act 2:** Trip meets with Lachlan and officially decides to enlist. He has no home to go back to, but he has a hound, a rifle, and a kingdom full of ordinary folks who need protection from Everdark monsters and elven tyrants. Lachlan writes him a glowing letter of recommendation for the recruiting depot in Dornon (or the nearest major fort). 
*   **Ending Hook:** Act 2 ends with a slice-of-life farewell. Trip is gifted the Strohl-Martin rifle permanently by Lachlan. With his pack loaded, his writ in his pocket, and Banjo trotting happily at his side (expecting army food to be top-tier), Wayne "Trip" Coberly sets off down the road to officially join the Corvish Empire's military. 

### **Key Progressions in this Act:**
*   **Character:** From lost/reactive survivor to proactive, trained, and certified soldier.
*   **Worldbuilding:** Seamlessly integrates LitRPG stats as a *metric* of physical reality, rather than a magical video game UI. Establishes the limits of human magic and the standard structure of the military.
*   **Plot:** Closes the loop on the immediate gnoll threat (sealing the cave) while leaving the Necromancer at large for future acts. Routes Trip directly into the broader military/political plotline of the Corvish Isles.




"""