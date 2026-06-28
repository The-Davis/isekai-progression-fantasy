import sys
sys.dont_write_bytecode = True
from prompts.outline import generate_outline_prompt
from util.files import write_file


next_section = """Let's work out the outline for chapter seven. This is the aftermath of the church defense, recovery, and planning next steps.
I think this should cover it, but see if it needs anything more, please:
With the immediate threat neutralized, the adrenaline wears off. Trip is shivering and bleeding again, but the salve won't help his poor ears. This time, Father Sydney spares a dose of a potion for everyone (even Banjo) and Trip gets a miracle healing. For the shivering, the priest accesses a locked militia chest in the vestry.
Praise God, there are finally clothes. Trip is outfitted in spare clothing stocked for the militia: sturdy wool trousers (breeches), a thick green-and-brown flannel shirt, and a pair of heavy leather boots. The children snicker that he looks like a mincing Corvishman without a proper kilt. Dougal is of the mind that a proper man lets himself air out. Banjo approves of the new garments, noting that Trip looks less like a plucked chicken now.
Dawn starts to peek in through the frames of the shattered stained-glass windows, and there's some halloo-ing from outside. A few villagers have arrived. The priest (who Trip realizes isn't a local, given his accent is so different) opens the front doors and greets a few armed men. With the sun rising, the gnolls are nowhere to be seen. They are very much nocturnal raiders, it seems.
One of these is introduced as Bider John, the porter and only other church official at this chapel of ease. Trip gets a short lesson in church details, learning that the actual parish church is in the closest town, and this church services parishioners who can't make the trek for Mass. This is why Father Sydney holds the rank of vicar rather than a higher rank.
Bider John is rather distressed by the state of the building, and he goes to and fro, inspecting the damage. Trip, Sydney, and one of the village militia men (make up a name) discuss plans to bring aid the outlying farmsteads. This conversation is interrupted by Bider John, who urges them to come see something.
The bider has found that one of the gnoll corpses has glowing violet eyes, and it's starting to twitch despite its head being caved in by a rock (it's the one Trip killed at the end of the last chapter). Maisie's warning about the "violet moon" comes into play. Father Sydney is horrified, identifying it as the work of a necromancer. They quickly drag the body out into the sunlight, but it starts to snap and snarl and it takes five of them to hold it down. Father Sydney shoves a communion wafer into its mouth (Banjo asks for one). It crumbles into dust (Banjo withdraws his request).
Father Sydney concludes that the gnolls must have been gathered and driven into the village by some foul villain from the Everdark. The militia man dourly assesses that they won't be able handle this, not if they pop up from fatal injuries. Their only saving grace is that the gnolls and their unseen master fear the sun, but the violet moon will rise again tonight.
The priest announces that he will travel to the manor of Lachlan MacTavish, the local clan laird. He knows a small company of dragoons are attached to his lands. Surely, trained and armed cavalry will be able to scatter the gnolls, or at least send to Wodenburgh for a larger army company. Trip and Banjo volunteer to escort the priest, who gratefully accepts.
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

"""

write_file(generate_outline_prompt(next_section=next_section))
