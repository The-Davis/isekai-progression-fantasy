import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Trip reaches the hole leading down to the crypt. He gets a glimpse of a ladder and the remains of a trap door: this was clearly meant for ease-of-access at one point, but all that's doing is helping the gnolls still down below ascend. The crypt is packed with the snarling menaces. Trip heaves the open keg down the shaft. As it tumbles, a thick trail of loose black powder cascades through the air.
Trip immediately pitches the burning taper right into the falling cloud of black powder.
Banjo, having hamstrung or otherwise savaged the last standing gnolls up here, trots up to the edge of the hole right next to Trip. He looks down at the tumbling keg, then looks up at Trip. *Hey Chief, you want me to fetch that?*
Trip's eyes go wide. "NO!" He grabs Banjo by the scruff, heaves the heavy dog backward, and dives behind the thickest pew he can find.
A heartbeat of silence is followed by a cataclysmic *BOOM*. The blast rocks the very foundations of the church. A shockwave of heat and dust rolls over the pews. The handful of stained glass windows (high above, too high for the gnolls to climb from outside) blow outward into the night in a shower of colorful shards.
The weakened stone floor around the altar completely gives way, dropping tons of masonry down into the crypt and permanently sealing the tunnel with a crunching collapse. The church walls stand firm, but Trip reflects how he could just as easily have buried them all inside. He is no explosives expert.
The dust settles, leaving a ringing silence. Trip stands up, coughing, his ears bleeding slightly. Banjo shakes a thick layer of dust off his coat, sneezing violently and commenting humorously on how it ain't the fourth of July, let's not do that again till then.
Only two or three gnolls remain in the sanctuary, deafened, dazed, and already savaged by Banjo. Trip picks up a fist-sized chunk of stone debris and clubs one over the head until it goes still, while Banjo happily finishes off another, and they continue this until none of the monsters remain alive.
Trip leans heavily against the pew, totally spent, as Father Sydney and the children slowly peek out of the vestry. The breach is sealed. They held the line.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.

Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.






"""
