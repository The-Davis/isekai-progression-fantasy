import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """We open chapter six right where we left off: 
The first gnoll, a massive brute covered in crypt dust, drags itself out of the gaping hole where the altar used to be. Behind it, Trip can hear more of the beasts yelping and scratching to join in.
Father Sydney, thinking quickly, grabs the kids by their shoulders and shoves them toward the open vestry door. He calls to Trip to follow, saying they can barricade the door and use the militia weapons.
Trip yells for Banjo to fall back. Banjo is deeply offended by the idea of retreating from a fight he was just getting ready for, but he backs toward the vestry, snapping at the air to keep the gnoll at bay.
As Trip nears the vestry, a second gnoll scrambles up from the hole and lunges past Banjo and the first gnoll. From the vestry doorway, Father Sydney tosses a heavy flintlock pistol to Trip.
Trip catches the pistol smoothly, steps inside the beast's reach, shoves the barrel right into its face, and pulls the trigger. The blast blows the gnoll's head apart.
Trip ducks into the vestry and trades his empty pistol for a fresh musket. To his pleasant surprise, the kids and the priest are already shoving furniture in front of the doorway, creating a barricade he can shoot past. It will take the weight and effort of many gnolls to get past.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.



Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.





**Scene 3: The Bannish Reloading Line**
*   **Assembly Line:** Trip takes his position at the gap. Father Sydney, recognizing Trip’s skill, organizes the children. He grabs the loaded muskets and pistols from the racks. Dougal and Maisie—who have likely helped their father hunt or drill with the militia—take charge of the powder horns, shot pouches, and ramrods. 
*   **The Defense:** Gnolls start slamming into the door, trying to squeeze through the gap. What follows is a brutal, chaotic sequence. 
    *   Trip fires a musket through the gap, dropping a gnoll.
    *   He blindly hands the empty weapon backward. A small pair of hands (Maisie's) snatches it, while Dougal shoves a freshly loaded pistol into Trip's other hand.
    *   Trip fires again. Banjo is at Trip's knees, a whirling dervish of teeth, ripping into any gnoll snout or paw that dares poke through the smoke-filled gap.
*   **Sensory Details:** The vestry quickly fills with blinding, sulfurous white smoke. The noise is deafening in the enclosed space. Trip's ears are ringing, his bare shoulder is bruised from the continuous recoil, and he's sweating profusely in his makeshift leather harness.
*   **LitRPG Flavor:** Over the ringing in his ears, Trip hears Father Sydney muttering in awe to the children about Trip's incredible *Alacrity* and *Agility*, marveling at how fast the Outworlder acquires targets and cycles weapons.

**Scene 4: The Keg and the Taper**
*   **The Escalation:** The barricade groans. The sheer weight of the gnolls pressing against the door is starting to push the heavy cabinet back. Trip realizes the gunline is failing; they are bottlenecked, but the gnolls are endless.
*   **The Idea:** Trip shouts over the din, asking if the militia keeps bulk powder. Sydney points to two small wooden kegs in the corner. 
*   **Improvisation:** Trip asks for a fuse. Sydney is bewildered by the request, but grabs a thick beeswax altar taper (candle) that had been burning on a small shrine in the room and hands it over. 
*   **The Prep:** Knowing a candle won't blow a sealed keg on its own, Trip uses the heavy rusted cleaver he looted earlier to violently pry the wooden bung out of the keg's top, ensuring the black powder will spill freely. 

**Scene 5: Clearing the Way**
*   **The Order:** Trip hefts the heavy keg under one arm and holds the lit taper in his other hand. He looks down at Banjo. *Banjo, I need some elbow room! Clear the gap!*
*   **The Charge:** Banjo lets out a thunderous bay. *Comin' right up, Boss!* The hound squeezes through the barricade gap and explodes into the sanctuary, a blur of muscle and fury. He hits the gnolls clustering the door so hard and fast that he scatters them, buying Trip a precious window.
*   **The Sprint:** Trip kicks the cot aside, yanks the door open, and charges out into the smoke-filled sanctuary, sprinting straight for the ruined altar.

**Scene 6: Fire in the Hole**
*   **The Throw:** Trip reaches the lip of the crypt. The stairs below are packed shoulder-to-shoulder with roaring, climbing gnolls. He heaves the open keg straight down the stairs. As it tumbles, a thick trail of loose black powder cascades through the air. 
*   **The Spark:** Trip immediately pitches the burning taper right into the falling cloud of black powder.
*   **The Fetch:** Banjo, having bitten his way clear of the door, trots up to the edge of the hole right next to Trip. He looks down at the tumbling keg, then looks up at Trip. *Hey Chief, you want me to fetch that?*
*   **The Dive:** Trip's eyes go wide. "NO!" He grabs Banjo by the scruff, heaves the heavy dog backward, and dives behind the thickest, most solid oak pew he can find just as the spark catches.

**Scene 7: The Aftermath**
*   **The Explosion:** A heartbeat of silence is followed by a cataclysmic *BOOM*. The blast rocks the very foundations of the church. A shockwave of heat and dust rolls over the pews. The remaining stained-glass windows blow outward into the night in a shower of colorful shards. 
*   **The Collapse:** The weakened stone floor around the altar completely gives way, dropping tons of masonry down into the crypt and permanently sealing the tunnel with a crunching collapse.
*   **Cleanup:** The dust settles, leaving a ringing silence. Trip stands up, coughing, his ears bleeding slightly. Banjo shakes a thick layer of dust off his coat, sneezing violently. *Phew! That was a spicy meatball!* 
*   **Victory:** Only two or three gnolls remain in the sanctuary, deafened, dazed, and half-crushed by debris. Trip casually picks up a dropped musket, clubs one over the head with the heavy wooden stock, while Banjo happily pounces on the other, finishing it off.
*   **Resolution:** Trip leans heavily against the pew, totally spent, as Father Sydney and the children slowly peek out of the vestry. The breach is sealed. They survived the night.

"""
