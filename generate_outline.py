import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter seven. This is the aftermath of the church defense, recovery, and planning next steps.
I think this should cover it, but see if it needs anything more, please:
As the altar shatters and the first gnoll hauls itself up from the crypt, Father Sydney rushes the children back into the vestry. He calls to Trip to help him barricade the door. Trip, who still has the shot and powder but no loaded musket, quickly follows, hollering for Banjo to come with him.
When he dashes into the vestry, the priest tosses him a loaded pistol. Trip doesn't hesitate. He whirls and shoves it right in the face of a pursuing gnoll and blasts it, but two more immediately scramble up from below.
Dougal and Maisie shove the cot into the doorway, then start knocking over cabinets. Sydney moves them to the more useful task of reloading pistols and muskets. The children of the Bannish highlands are no slouches when it comes to defending their homes. They all recognize Trip as the superior fighter, and keep him stocked with a fresh weapon. Trip uses the vestry's narrow doorway as a "fatal funnel." Only one or two gnolls can get at them at a time, and Trip's marksmanship ensures they don't survive the attempt. For a few minutes, it's a nightmare of roaring gunfire, powder smoke, and ringing ears.
The gnolls are piling up, but there are too many. Trip yells to Sydney (over the ringing in his ears), asking how much black powder the militia keeps. Sydney points out two small kegs in the corner. Trip instructs the priest to rig one with a fuse. Sydney isn't familiar with this technique, but gives him an altar taper. It'll have to do.
Trip hefts a keg and asks Banjo to clear some room. The hound leaps out, snapping at gnolls, then the pair charge for the altar. Trip hurls the keg straight down into the gaping hole of the crypt and throws the lit taper after it. Banjo pokes his head in the hole and asks if he should fetch. Trip grabs the hound and dives with him behind one of the heavy pews.
The explosion rocks the church, shattering the remaining stained glass windows and completely collapsing the tunnel, crushing the gnolls inside and sealing the breach. Trip and Banjo check the wounded gnolls still in the sanctuary and put them down. Victory.


"""

"""
The rest of the story is going to be episodic, "cozy violence" that mixes "A Soldier's Life" with "Sharpe's Rifles": no-system, stats-lite LitRPG with a loop of action, power ups, loot, socializing, and slice of life set in a Napoleonic/Georgian era of tech and conflict.
Trip and Banjo need to wind up as scouts (well, one scout who has a dog) in the Corvish military, but that hasn't been introduced, so we need to get them to the military.
I plan to have them help secure the church (a desperate defense barricading in the vestry and fighting off a choke point then pushing the gnolls back into the crypt and out, then using the militia gunpowder stocks to blow the escape tunnel) and then head to the nearest military post for help.
After reaching the military post, Trip will return with an army detachment to rescue the village and then they join up to do some good.

I figure we have three to four chapters of material:
1. Defend the church and seal the tunnel.
2. Plan to go for help, restock (and finally get pants), break out the front door, lead the gnolls away from the church, then break contact and head across country
3. Another fight, reach the military (or be rescued by them), and convince them to come help. Ride back with the cavalry to crush the gnoll warband.

I think working in an undead leader of the gnolls as a hook for future adventures and the reason the military actually comes instead of leaving the militia to fend for itself would be good.





With the immediate threat neutralized, the adrenaline wears off. Trip is shivering and bleeding again. Father Sydney accesses a locked militia chest in the vestry.
Praise God, there are finally clothes. Trip is outfitted in a spare Bannish militia uniform: sturdy wool trousers (breeches), a thick green-and-brown flannel shirt, and a pair of heavy leather boots. He marvels at the quality of the "loot." Banjo sniffs the boots, noting they smell like sheep, but admits Trip looks less like a plucked chicken now. Trip also restocks his powder horn, shot, and grabs a bayonet.
*   **The Plan:** The church is safe, but it’s a tomb if they stay. Trip volunteers to go for the army. Father Sydney gives him directions to *Fortress Varn*, a Corvish military outpost on the Bannoch border, about ten miles across the moors.
*   **The Breakout:** Trip and Banjo need to draw the horde away so the church can remain unbothered. They unbar the front door. Trip unleashes a devastating volley into the mob, screams a wild Appalachian rebel yell, and Banjo bays like a demon. They sprint into the night.
*   **The Chase:** The gnolls take the bait. What follows is a tense, tactical cross-country chase. Trip uses his woodsman tracking skills and Banjo’s incredible nose to break line of sight, kite the gnolls through the freezing lochs and glens, and finally lose them in the heather. 

### Chapter Eight: The Violet Moon's Master and the Redcoats
**Focus: Expanding the lore (Everdark), a new threat, and meeting the military.**
*   **The Trek:** A quieter moment of travel. Banjo asks if the military base will have sausages. Trip and Banjo test the limits of their telepathy now that they are moving through thick fog and hills. 
*   **The Encounter:** Approaching the main road, Banjo's hackles rise. He smells "a possum that's been dead a month." In a ruined stone abbey, they stumble upon a gnoll warband holding position. In the center is the reason for the attack: a rotting, undead figure draped in ancient armor, basking in the light of the violet moon. It is an Everdark Wight (or similar local undead), using dark magic to direct the gnolls.
*   **The Ambush:** Trip realizes this is the leader and tries to sneak past, but Banjo’s hatred for "zombie coons" or a snapped twig gives them away. They are cornered. Just as Trip fixes his bayonet for a desperate last stand, disciplined shouting rings out.
*   **The Cavalry Arrives:** A perfectly timed, devastating volley of musket fire tears through the gnolls from the high ground. Enter the Corvish Army—a detachment of Bannish Highlanders (or Corvan line infantry). They march to the drone of bagpipes, fixing bayonets and slaughtering the disorganized gnolls.
*   **Diplomacy:** Trip is brought before the commanding officer (e.g., Captain Sterling). The Captain is highly skeptical of this strange man and his dog, initially dismissing the village attack as a minor raid. But when Trip points out the slain Undead leader—proving the Everdark is mobilizing under the violet moon—the Captain’s demeanor instantly shifts. This isn't a raid; it's an invasion. 

### Chapter Nine: The Relief of the Glen
**Focus: Large-scale Georgian combat, wrapping the arc, and setting the new status quo.**
*   **The Ride Back:** The Captain orders a forced march/cavalry ride back to the village. Trip rides alongside them, learning a bit more about how the military measures "stats" (the Captain approvingly notes Trip's "Agility" and "Finesse" in keeping pace).
*   **The Battle:** They arrive at the glen just as the gnolls are trying to burn the church roof. The military deploys in strict, beautiful Napoleonic formations. Volley fire, rolling smoke, and disciplined bayonet charges.
*   **The Scout Role:** Because standard line infantry is rigid, the Captain tasks Trip and Banjo to act as skirmishers/scouts on the flanks. Trip uses his woodsman skills to pick off gnoll chieftains from the rocky high ground, while Banjo acts as a brutal shock-troop in the trenches/ditches, ripping throats and teleporting his gleeful, blood-soaked commentary into Trip's mind.
*   **Resolution:** The horde breaks and scatters. The village is saved. Dougal, Maisie, and Father Sydney emerge to thank them.
*   **The Hook:** Captain Sterling is deeply impressed by Trip's marksmanship, bravery, and physical attributes, noting that his "Finesse" and "Wit" are exactly what the Empire's scouting regiments need. He offers Trip a paying job, food, and board. Banjo hears the word "food" via Trip's mind and demands Trip accept. Trip, realizing he needs to make a living in this crazy new world, agrees.



















Here is a detailed outline for the next four chapters, continuing the story directly from the gnolls breaking through the church floor. It sticks to your "cozy violence" tone, integrates the worldbuilding rules you've established, and sets up Trip and Banjo’s transition into the Corvish military.

### **Chapter Six: The Fatal Funnel**
*   **The Breach:** As the altar shatters, the first gnoll hauls itself up from the crypt. Trip doesn't hesitate. He snaps his musket to his shoulder and blasts the lead creature, but two more immediately scramble over its corpse. 
*   **Tactical Retreat:** Realizing the open sanctuary offers too many angles of attack, Trip yells for Father Sydney to grab the kids and fall back to the vestry. Trip and Banjo fight a fighting retreat down the aisle. Banjo is a terror, dragging gnolls down by their hamstrings to buy Trip time to reload his single musket. 
*   **The Choke Point:** They reach the heavy vestry door. Trip uses the narrow doorway as a "fatal funnel." Only one or two gnolls can get at them at a time. Here, Trip's incredibly high (and currently unmeasured) physical stats—specifically Endurance and Vigor—are on full display. He uses the heavy butt of the empty musket like a club, fighting with raw, rhythmic stamina, while Banjo bites and tears at knee-level. 
*   **The Counter-Measure:** The gnolls are piling up, but there are too many. Trip yells to Sydney, asking how much black powder the militia keeps. Sydney points out two small kegs in the corner. Trip instructs the priest to ready a slow match (or simply pour a thick trail of powder). 
*   **Fire in the Hole:** Trip hefts a keg, kicks the nearest gnoll back to create space, and charges out of the vestry with Banjo covering his flank. He hurls the keg straight down into the gaping hole of the crypt, throws a lit taper (or fires a spark from a flintlock mechanism) after it, and dives behind a heavy stone pew. 
*   **The Boom:** The explosion rocks the church, shattering the remaining stained glass windows and completely collapsing the tunnel, crushing the gnolls inside and sealing the breach. The few surviving gnolls in the sanctuary flee in panic, and Trip and Banjo put them down.

### **Chapter Seven: Pants, Plans, and the Decoy**
*   **Loot and Restock:** The church is quiet, though the horde outside the front doors is still a threat. In the vestry, the adrenaline fades. Trip makes it clear he is not fighting another battle in a dead monster's underwear. Father Sydney rummages through the donation bins and militia spares, finally outfitting Trip in a sturdy pair of Bannish highland wool trousers, a thick shirt, and a pair of militia boots (a bit tight, but they work). Trip also requisitions a bayonet to use as a close-quarters blade, lots of powder, and shot. Banjo demands (and receives) half a loaf of communion bread.
*   **The Hook (The Undead):** While inspecting the dead gnolls by the ruined altar, Trip notices something unnatural. One of the gnolls has glowing violet veins and doesn't bleed properly. Maisie's warning about the "violet moon" comes into play. Father Sydney is horrified, identifying it as the work of an Everdark Necromancer—a "Grave-Walker." This is no longer a mere raid; it's an Everdark incursion. 
*   **The Plan:** Father Sydney reveals that the local militia can't handle this, but there is a Corvish military garrison—a Dragoon outpost—ten miles down the valley. However, someone needs to go get them, and the church is currently surrounded. 
*   **The Breakout:** Trip and Banjo volunteer to be the decoy so the priest and kids can stay safe in the fortified (and now sealed) church. Trip throws open the heavy front doors. He fires a volley into the gnolls, yells a West Virginia rebel yell, and Banjo unleashes a massive, taunting bay. The gnolls take the bait. Trip and Banjo sprint into the dark, leading the horde away from the village and into the treacherous moors.

### **Chapter Eight: Cross-Country Pursuit and the Master**
*   **The Chase:** A thrilling, fast-paced sequence across the heather. Trip uses "Sharpe's Rifles" style hit-and-run tactics—loading on the run, using the terrain to break line of sight, and turning to deliver devastating volleys before running again. Banjo darts in and out of the brush, picking off stragglers. They communicate flawlessly when in sight, operating as a perfect hunter/hound duo.
*   **Cornered by the Master:** Trip and Banjo are pushed toward a rocky gorge, running out of maneuvering room. Here, they finally see the leader. Stepping out of the violet moonlight is an Everdark Necromancer (perhaps a skeletal, corrupted Elf or a long-dead Bannish warlord) wielding foul magic, flanked by heavily mutated, undead gnoll elites. 
*   **The Stand:** The Necromancer attacks. Trip’s mundane black powder weapons are less effective against the magic-shielded undead, but Trip uses his wits—shooting the cliff face to cause a rockslide or using his bayonet in desperate close-quarters defense. Banjo bravely tanks a hit to protect Trip, showing his fierce loyalty. They are on the ropes.
*   **The Cavalry Arrives:** Just as the Necromancer prepares a killing blow, a disciplined, rolling volley of musket fire tears through the dark, shredding the undead gnolls. A detachment of Corvish Dragoons, drawn by the sound of Trip's constant firing and the earlier church explosion, crests the ridge. The Necromancer, realizing the military has arrived, sneers at Trip, drops a cryptic threat (or a physical clue, like an amulet), and escapes into the shadows.

### **Chapter Nine: The Return of the Chief**
*   **First Impressions:** The Dragoon commanding officer (a pragmatic, proper Corvish gentleman with a stiff upper lip) approaches. He initially views Trip as a vagabond, but Trip's demeanor, his tally of dead monsters, and his presentation of the Necromancer's artifact change the officer's tune. When the officer learns a Grave-Walker is leading a warband against a Sancta Canthica church, he immediately orders a counter-attack.
*   **The Ride Back:** Trip is given a horse. Banjo runs alongside, telepathically marveling at the "giant ugly dogs with hooves" and boasting to the cavalry mounts about his kill count. Trip and the officer share a brief cultural exchange—Trip's folksy wisdom clashing delightfully with the officer's rigid Corvish military doctrine.
*   **The Cavalry Charge:** They arrive back at the village just as dawn breaks (the twin moons setting). The remaining gnolls are trying to break into the church again. The military action is a glorious display of Napoleonic warfare: coordinated volley fire, the drawing of cavalry sabers, and the fierce drone of Bannish bagpipes. 
*   **Slice of Life & New Beginnings:** The village is saved. Father Sydney, Maisie, and Dougal emerge safely. The military officer objectively measures Trip's stats, confirming his physical attributes are incredibly high for a commoner. Realizing Trip's potential and his lack of a home, the officer offers him a place as a Scout in the Corvish Army. 
*   **Conclusion:** Trip accepts, figuring a steady paycheck, the chance to hunt Everdark critters, and a clear purpose beat wandering aimlessly. The chapter ends on a cozy note: Banjo is finally rewarded with a massive plate of village sausages, and Trip, wearing real boots and pants, looks out over the alien sunrise, ready for his new life.

### **Why this outline works for your story:**
*   **Sticks to the Mechanics:** Banjo's line-of-sight telepathy will make the nighttime chase sequence intense (if they get separated by brush, they lose communication, relying on instinct until they reunite). 
*   **Establishes the Loop:** Introduces the core gameplay loop of the narrative: survival combat -> tactical use of black powder/terrain -> looting gear (pants/muskets) -> interacting with the broader world (the military/church) -> cozy downtime (sausages).
*   **Integrates Worldbuilding:** Utilizes the tension between the Elves and humans (the Necromancer could be Elvish or using Elvish magic, confirming the prejudice), heavily features the Sancta Canthica, and introduces the Erlenreich/Corvish geopolitical conflict indirectly through the military.







"""

write_file(generate_outline_prompt(next_section=next_section))
