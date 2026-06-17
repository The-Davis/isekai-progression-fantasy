import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """
Banjo follows Trip's spoken command to "lay down" a little *too* perfectly. Combined with Banjo's unnatural stillness and the intense, almost human glare he's giving the lawmen, the superstitious guards are severely unnerved. 
One of the lawmen (younger, more twitchy) mutters about witches' familiars and "beasts of the adversary." Believing Banjo to be a demon in animal form, he swings his carbine away from Trip and levels it at the dog.
Trip doesn't even think; he lunges naked through the heather and slams into the twitchy lawman. The flintlock discharges with a deafening crack and a plume of white smoke, missing Banjo.
The lead lawman reacts to the assault on his man by firing his own carbine. The heavy lead ball clips Trip through the shoulder/side, knocking him flat.
Through the blinding pain, Trip mentally and verbally screams for Banjo to *RUN!* Banjo hesitates, projecting a white-hot flash of canine fury and a desire to bite, but Trip's mental command is absolute. Banjo flees, over the hills and far away, moving too fast for the lawmen to reload. 

You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.

We'll end the chapter on that note.




**Scene 2: First Taste of Magic**
*   **The Aftermath:** Trip is bleeding badly in the dirt. The lead lawman curses his twitchy subordinate for shooting a "perfectly good vagabond"—foreshadowing that a healthy prisoner has value.
*   **The Potion:** The lead lawman pulls a small, wax-sealed glass vial from his belt. He unceremoniously pours the liquid over Trip's wound. 
*   **Magical Wonder:** Trip experiences magic for the first time. The sensation is wild—it burns like ice water, knitting flesh and muscle back together in seconds and physically pushing the flattened lead ball out of the wound. 
*   **Cultural Difference:** To Trip, this is a mind-bending miracle. To the lawmen, it's just standard—if somewhat expensive—field kit. They offer no grand explanation, just annoyance at having wasted it.
*   **The March:** They toss Trip a rough, incredibly itchy horse blanket to preserve modesty, bind his hands with thick rope, and march him toward the nearby town of Glenrowan.
*   **The Bond limitation:** As they walk, Trip tries to speak to Banjo, but the voice in his head is gone. Instead, he feels a raw, pulsing emotional tether. He senses Banjo's panic fading into stubborn, predatory patience. The dog is unharmed, but distant.

Describe the Bannish settlement—sturdy stone buildings with slate roofs, smoking chimneys, and a gloomy but picturesque highland aesthetic. 
Trip is hauled straight into the local manor/courthouse to face Lachlan MacTavish. Describe Lachlan exactly as noted: barrel-chested, mutton-chops, green tailcoat over a Bannish tartan waistcoat, broken nose. He speaks with an amiable brogue and clasps his hands over his stomach.
The lead lawman formally charges Trip: Vagrancy (wandering naked), Assaulting a Peace Officer, and Trafficking with Devils (the unnatural hound).
Lachlan hears the testimony. Trip, clutching his horse blanket, tries to use his folksy charm and explains he's just a fella from West Virginia who got lost, and his dog is just a dog. 
*   **Lachlan's Verdict:** Lachlan is entirely pragmatic. He finds Trip guilty of Vagrancy and Assault—the facts are undeniable. However, when it comes to Trafficking, he pauses. He invokes Saint Michael, the defeater of demons, and demands proof. Did the dog cast a hex? Did Trip curse the cattle? The lawmen admit they have no proof. Lachlan decides to hold the devilry verdict in abeyance pending an assessment.

**Scene 4: The Relic and the Assessment (Worldbuilding Beat)**
*   **Enter the Vicar:** Lachlan summons the local Vicar of the Sancta Canthica. The Vicar brings an ancient, ornate Church relic used for measuring a person's God-given humors/attributes.
*   **The Test:** Trip is forced to place his hand on the relic. It glows faintly, reacting to his life force. The Vicar reads the results and begins writing them in a ledger.
*   **The Written Language:** Trip catches a glimpse of the ledger. While everyone speaks what sounds to him like slightly old-fashioned English, the writing is an elegant, flowing script without a single Latin letter. It hits Trip hard that he really is on another planet.
*   **Stat Reveal:** The Vicar reads off Trip's stats to Lachlan (on the 0-100 scale, noting both current ranks and potential maximums). 
    *   Trip's magical stats (Essence, Dominion, etc.) are practically non-existent, but more importantly, they are *pure*. The Vicar confirms Trip carries no spiritual taint or corruption. Magic is natural; devilry leaves a stain. Trip is completely innocent of devilry.
    *   Trip's physical stats, however, are highly impressive for a "commoner". His Endurance (Capacity), Finesse (Control), and Agility (Speed) are well above average, forged by years of distance running, coon hunting, and shooting in the dark Appalachian hollers.
Lachlan's eyes light up. The man clasping his belly isn't just a judge; he's a retired Captain looking at prime military stock. 


*   **The Proposition:** Lachlan dismisses the Vicar and the guards, pouring himself a drink. He lays his cards on the table. King Mundifred is gearing up for a brutal war against the mainland elves. Glenrowan owes a levy of men. Lachlan loves his tenants and refuses to send the local farmboys to die in the mud if he can help it. 
*   **The Roles:** Lachlan explains that with Trip's physical stats, he qualifies for elite units. If Trip enlists as an elite, he counts as Glenrowan's *entire* levy for the year. He briefly describes the Line Infantry (meat grinders), Dragoons (cavalry), and Rangers (scouts, marksmen, skirmishers).
*   **Trip's Choice:** Unsurprisingly, the West Virginian hunter favors the Rangers. 
*   **The Carrot and the Stick:** Lachlan offers a bargain: Sign the enlistment papers for the Rangers. His first year's military wages will be garnished to pay his fines for Vagrancy and Assault. The Devilry charge will be permanently dropped.
Trip asks what happens if he refuses. Lachlan drops the amiable laird act. Trafficking with devils is a capital crime. If Trip doesn't join, Lachlan will ship him to the proper magistrate in Wodenburgh. There, Trip will face a trial where the punishment is penal transportation, bodily mutilation, or a short drop from a hangman's noose. 
Realizing he is thoroughly outmaneuvered, Trip sighs and accepts the deal. 

Trip is given a set of rough, ill-fitting civilian clothes (breeches and a linen shirt) and locked in a stone cell for the night before the army recruiters arrive in the morning.
Sitting alone in the dark, Trip focuses his mind, reaching out to his hound. He can't hear Banjo's gruff, TV-Land-loving voice, but the bond is there. 
He feels a distinct, warm tug from the dark hills outside of town. A persistent feeling of *loyalty, hunger, and waiting*. Banjo hasn't abandoned him. Trip makes a silent promise to survive this army, figure out how this crazy world works, and get his dog back.

"""