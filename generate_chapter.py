import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """We open chapter four mid-sprint. Trip is pushing his body to the absolute limit. His bare feet are numb and bleeding from the freezing stones, the rawhide harness is chafing his bloody chest, and Dougal's weight is becoming unbearable. Maisie is running ahead of him, terrified but determined.
The sounds of the pursuing gnolls (yips, snarls, and heavy footfalls) are getting louder. The violet moon casts disorienting shadows, making the run even harder. Trip realizes they aren't going to make it to the church in time.
Banjo realizes it too. He tells Trip Sorry, Boss. Math ain't in our favor. Don't let 'em get the pups.
Banjo skids to a halt, turns around, and unleashes a ferocious, ringing bay, and stands his ground against the horde.
Trip almost stops. He loves that dog more than anything, and leaving him feels like a betrayal. But he looks down at the bleeding human boy in his arms and ahead at the terrified little girl. Trip's code is ironclad: human life comes first. He grits his teeth, ignores the sounds of the brutal dogfight erupting behind him, and sprints toward the church.
Maisie pushes her way through the heavy oak doors of the church. Trip lunges inside with Dougal. He briefly notes that it's nothing like the church he grew up in, but he was raised Baptist. He recalls being inside a Catholic church once for a friend's wedding, and this "Canthican" church is mighty close to that.
He doesn't dwell on that long. He lays Dougal down on a sturdy wooden pew and calls out for help. He wants to get his hands on those muskets so he can go help Banjo. He asks Maisie where this vicar fella is, but she doesn't know. She goes to fuss over Dougal.
Trip spots the Vicar asleep in the front pew. Next to him on the floor is a spilled flask of strong spirits. He completely missed the fires and the screams because he was drinking to ward off the cold and the isolation of his remote parish.
Trip kicks the pew to wake him up. The Vicar startles awake, hungover and confused. Faced with the sight of a tall, barefoot, blood-soaked man wearing gnoll-leather harnesses, he nearly passes out again.
Maisie spots him and greets him by name (Vicar Sydney). She tells him that the gnolls are attacking and her brother's hurt. Vicar Sydney looks past Trip and sees the children. He rushes over to help them, forgetting Trip in his haste, though he nearly falls over as he isn't sobered up.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.



Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.

**Scene 3: Redemption and Black Powder**
*   **Taking Action:** To his credit, Vicar Lachlan doesn't wallow. Driven by intense shame and duty, he springs into action. He rushes to Dougal, pulling a small, corked glass vial from his robes (a low-grade healing potion) and carefully tips it into the boy’s mouth, stabilizing him.
*   **The Armory:** Trip demands to know where the muskets are. Lachlan tosses him a heavy iron ring of keys and points to the reinforced vestry door. "Take what ye need, man! I must rouse the parish!"
*   **The Bell:** While Trip unlocks the vestry, Vicar Lachlan runs to the narthex and grabs the thick hempen rope of the church bell. He begins hauling on it with all his might. The heavy, frantic tolling begins to echo across the valley, waking the villagers.
*   **Lock and Load:** Inside the vestry, Trip finds the local militia's cache. He grabs two heavy flintlock muskets. They are beautifully maintained—something Trip appreciates. He grabs a pre-measured powder horn and shot, quickly checking the frizzens and priming the pans with the practiced ease of a man whose grandfather raised him on black-powder hunting. 

**Scene 4: The Rescue of Banjo**
*   **Stepping Back Outside:** Trip kicks the heavy oak doors open. The scene outside is chaotic. Banjo is backed against the stone steps of the church. The hound is bleeding from a few scrapes and breathing hard, but he is surrounded by three dead or dying gnolls. The rest of the pack (six or seven of them) are circling, preparing to overwhelm him.
*   **Fire and Smoke:** Trip steps onto the porch. *“Get away from my dog!”* he bellows. He levels the first musket and fires. The roar of the black powder is deafening, and a cloud of thick white smoke erupts. A massive gnoll takes the heavy lead ball to the chest and drops instantly. 
*   **The Second Shot:** Trip drops the spent musket, seamlessly raises the second, and fires just as a gnoll lunges for Banjo’s flank. The shot takes the beast in the shoulder/neck, sending it spinning into the dirt. 
*   **Retreat:** The sudden, thunderous noise and the death of two more packmates stagger the gnolls. Trip yells for Banjo. *“Inside! Now!”* 
*   **Securing the Door:** Banjo darts up the steps, limping slightly but his tail still wagging. Trip grabs the hound by the scruff, hauls him over the threshold, and slams the heavy oak doors shut. 
*   **The Bar Drops:** Trip throws the massive iron-bound wooden beam into the brackets across the doors just as the surviving gnolls crash against the outside wood. The doors shudder, but hold. 
*   **Chapter Ending Image:** The church bell is ringing wildly above them. Trip slides down the heavy doors to sit on the stone floor, exhausted, smoking musket at his feet. Banjo sits next to him, panting, and telepathically asks: *“So… you reckon the Vicar’s got any snacks in here?”* 




**Scene 3: Redemption and the Vestry**
*   **Stepping Up:** The Vicar immediately shakes off his stupor, desperate to redeem himself. He takes Dougal from Trip, laying him on a pew. He tells Maisie to fetch a specific poultice/potion from his bag to stabilize the boy's "Vigor."
*   **Arming Trip:** Trip demands the muskets Maisie mentioned. The Vicar points him to the vestry beside the altar, telling him the militia's weapons and powder are kept there. 
*   **Rousing the Village:** The Vicar then runs for the bell tower rope at the back of the church to wake the rest of the village militia. 
*   **The Guns:** Trip kicks open the vestry door. He finds a rack of heavy, smoothbore muskets (similar to Brown Besses). He’s vastly relieved to find they are already loaded and primed. He grabs two, tucks a powder horn and a pouch of lead balls into his makeshift gnoll-belt, and runs back toward the main doors. 

**Scene 4: The Rescue of Banjo**
*   **The Stand:** Trip bursts out onto the church steps. Banjo is fighting like a demon in the dark, dodging spear thrusts and snapping bone, but he is completely surrounded by five or six gnolls and is getting backed up the stairs. He’s bleeding from a shallow spear graze but refuses to give an inch.
    *   *Telepathic line:* *"I got 'em right where I want 'em, Trip! Just tenderizing the meat!"*
*   **Black Powder:** Trip raises the first musket, seats it against his shoulder, and pulls the trigger. The familiar, deafening roar and heavy kick of black powder is a massive comfort. The heavy lead ball blows a gnoll backward down the steps. 
*   **Double Tap:** The gnolls flinch at the thunder. Trip drops the empty musket, instantly raises the second, and fires into the chest of a massive gnoll lunging for Banjo's blind side.
*   **Retreat:** Through the thick cloud of sulfurous white smoke, Trip yells, "Get in here, dog!" Banjo darts up the steps, slipping past the bewildered monsters. 

**Scene 5: Securing the Fortress**
*   **Barring the Door:** Trip grabs the iron ring of the heavy oak door and hauls it shut just as the gnolls charge the steps. 
*   The Vicar abandons the bell rope just long enough to help Trip lift the massive, iron-reinforced wooden bar and drop it into the brackets across the doors.
*   *Thud!* The first gnolls slam into the wood outside, howling and scratching furiously, but the thick Canthican masonry and oak hold firm. 
*   **Ending Beat:** Above them, the heavy bronze church bell begins to toll furiously, ringing out into the night to wake the valley. Trip slides down the door, totally exhausted, chest heaving. Banjo nudges Trip's bloody chin with a wet nose, telepathically asking if Trip happens to have any of those Communion wafers he's smelling. They are safe—for the moment. 


"""
