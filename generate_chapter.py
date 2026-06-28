import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Trip takes his position at the gap. Father Sydney grabs a pair of loaded muskets and stands behind Trip, informing him that he'll keep him fresh. He asks the kids if they can reload. Dougal, who surely helped his father hunt or drill with the militia, grabs up the spent pistol and starts to reload it.
Banjo takes up position at Trip's side, grumbling that a hound's teeth are wasted hiding behind a wall. He should be out there. Trip assures him that will happen soon enough.
Gnolls start slamming into the barricade, trying to squeeze through the gap. What follows is chaotic. 
Trip fires a musket through the gap, dropping a gnoll.
He blindly hands the empty weapon backward. A small pair of hands (Maisie's) snatches it, while Sydney shoves a fresh musket into Trip's other hand.
Trip fires again. He only wounds a gnoll and it manages to get through, but Banjo siezes it and savages it.
The vestry quickly fills with blinding, sulfurous white smoke. The noise is deafening in the enclosed space. Trip's ears are ringing, his bare shoulder is bruised from the continuous recoil, and he's sweating profusely in his makeshift leather harness.
Over the ringing in his ears, Trip hears Father Sydney muttering in awe to the children about Trip's incredible *Alacrity* and *Agility*, marveling at how fast the Outworlder acquires targets and cycles weapons.
The barricade groans. The sheer weight of the gnolls pressing against the door is starting to push the heavy cabinet back. Trip realizes the gunline is failing; they are bottlenecked, but the gnolls are endless.
Trip shouts over the din, asking if the militia keeps bulk powder. Sydney points to two small wooden kegs in the corner.
Trip asks for a fuse. Sydney is bewildered by the request, but grabs a thick beeswax altar taper (candle) and hands it over. He has a few matches as well.
Knowing a candle won't blow a sealed keg on its own, Trip uses the heavy rusted cleaver he looted earlier to violently pry the wooden bung out of the keg's top, ensuring the black powder will spill freely.
Trip hefts the heavy keg under one arm and holds the lit taper in his other hand. He looks down at Banjo. *Banjo, I need some elbow room! Clear the gap!*
Banjo lets out a thunderous bay. *Comin' right up, Boss!* The hound squeezes through the barricade gap and explodes into the sanctuary, a blur of muscle and fury. He hits the gnolls clustering the door so hard and fast that he scatters them, buying Trip a precious window.
Trip charges out into the smoke-filled sanctuary, sprinting straight for the ruined altar.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.

Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.

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
