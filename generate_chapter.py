import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """We open chapter five right where we left off. Father Sydney is incredulous that Trip just risked his life to save a dog. He thought they must have had another companion the way Trip ran out there, but he didn't think he'd risk his life for a mere dog. He also mentions it's a shame Trip didn't bring back both muskets. Trip realizes in his haste, he did leave one behind, but the other is on the ground beside him.
Banjo quips that it's better than a mere cat. He then goes off on a tangent about mere cats and meerkats. He'll pester Trip about the similarity throughout the conversation while Trip tries to ignore him and talk to the priest.
Trip tries to explain how special Banjo is, but with danger firmly barricaded outside, his body is starting to betray him, and he has trouble putting his thoughts in order. He even has an idle, distracted thought of a gnoll trying to use the musket he left behind. Adrenaline dumping is an ornery foe. Fortunately, Maisie and a recovering Dougal have much positive to say about how brave Banjo and Trip were at their farm.
From their tale (which Trip summarizes for the reader, we don't need to revisit it in full, but do note that the children recounted how Trip wasn't wearing a stitch until he took the gnoll's loincloth) Father Sydney soon learns of the deaths of their parents. He says a quick prayer for the dead, and then says he'd best see to the living. Trip is clearly exhausted and hurt, he says. He helps Trip back into the vestry, where he has medical gear. Banjo follows, limping but wagging and still chattering away in Trip's head about meerkats. Trip is thoroughly disoriented by his crash, but he has the presence of mind to ask the priest to help the dog.
Father Sydney, seeing the distress of Dougal and Maisie reliving their parents' death, gives the children bandages and tells them to tend to the hound. When the kids start wrapping Banjo, the dog tells Trip he doesn't want to be trussed up like a turkey (or something similar), but Trip tells him he's the one who says he's better with pups. Deal with it.
Sydney and Trip set up in the vestry, and the priest sees to his wounds. He admits he wanted to have a word with Trip away from the children. He asks Trip directly: did he come from the homeworld?
Trip says as far as he knows, yes, unless that crazy fella on the TV was right and some place other than Earth is where humanity was originally from. Sydney is excited. Has Trip been to the sepulcre? The holy land? Is it true that the Church has spread the gospel to the entire world?
After calming the excited, practically fan-boying priest down, Trip points at his bleeding feet and asks if he could get a drop or two of that healing potion stuff. Father Sydney looks a little embarassed (and possibly still a mite tipsy) and hurriedly rummages through some cabinets in the vestry.
He pulls a jar filled with an amber-colored salve from a cabinet. He explains that healing potions (like the one used on Dougal) are expensive and difficult to make and strictly for life-threatening injuries. Dougal was near death when Trip brought him there. For lacerations like those plaguing Trip's feet, he uses "Saint Raphael's Pitch", a magical, fast-acting medical glue that sears like fire but binds the skin instantly so it can heal naturally underneath. Trip comments that it smells like turpentine, but is pleased to see that it works better than stitches and hurts less.
As Sydney cleans and binds Trip's wounds, they chat. Trip quickly deduces that he isn't the first person to come here. He asks if everyone's from Earth originally. Sydney says many church fathers believe so, but the elves claim otherwise. Sydney himself was born here, as was everyone in his family as far back as he can trace his family tree. His grandmother claims that one of her ancestors was an Outworlder, a man from the "British East India Company" who arrived nearly four hundred years ago. Nearly two hundred people showed up at once in that wave, and such trouble they caused. They're the reason Corva is a kingdom rather than a mere electorate in the Erlenreich, you know.
Trip admits that no, he does not know, but some of that sounds familiar. Did them British fellas teach you all English?
English? Father Sydney doesn't know the word.
The language we're speaking. It's English, unless I hit my head real hard and didn't realize it.
Sydney says it's called Corvish, and it predates the British arrival. Perhaps it arrived even earlier? A fascinating idea. The homeworld is a passion of his, he confesses.
Trip is amused and says he never would have guessed (or "you don't say"). Father Sydney should be very excited when talking about Earth, "geeking out", so to speak.
You can stop there and we'll edit before I provide the next section.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.



Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.




They brought black powder, flintlocks, and ruthless tactics. Their arrival shattered the absolute dominion of the elves, allowed humanity to carve out the Corvish Empire, and changed the balance of the world forever.
*   **The Language and The Curse:** Trip notes that everyone speaks English. Sydney explains that "Corvish" is indeed the tongue of the East India Company, slightly drifted over centuries. Trip spots a book on a desk and notices the letters look like flowing vines, not English. 
    *   Sydney warns him: *Never* try to write in the Latin alphabet. The elves, terrified of Outworlder knowledge spreading, wove a continental curse into the magic of the world. Any paper or parchment inscribed with Latin letters rots to ash in seconds. They are forced to use the elvish script to survive.
*   **The Danger of Discovery:** Sydney gives Trip a grave warning. King Calador Half-Elven, despite ruling a human empire, shares the elvish loathing of Outworlders. Their existence threatens the status quo. If the Crown or the "elf-friend" nobles discover Trip is an Outworlder, he will be imprisoned, dissected by elvish scholars, or executed. Trip must adopt a cover story immediately—perhaps claiming to be an illiterate hermit from the deep Bannish Highlands. 

**Scene 4: The Threat Returns (Cliffhanger)**
*   **Processing:** Trip is overwhelmed. He’s stuck on an alien world, he can't write his own name without destroying paper, the King wants him dead, and he has to fake an identity. Banjo, meanwhile, is sniffing the floorboards, wholly unconcerned with geopolitical elvish drama. (*"Hey Trip, I don't care about no East India whatever, but they didn't happen to bring any canned beans with 'em, did they?"*)
*   **The Shift:** Suddenly, Banjo’s hackles rise. He lets out a low, vibrating growl. The telepathic voice in Trip's head turns dead serious. 
    *   *"Boss. The big coons. They ain't scratching at the front door no more."*
*   **The Realization:** Trip listens. The heavy thudding against the front oak doors has stopped. Instead, he hears a chorus of yips, snarls, and the clicking of claws... coming from *beneath* the floorboards. It’s echoing through the stone of the church.
*   **The Cliffhanger:** Trip looks at Father Sydney. "Reverend... what's underneath this floor?" 
    *   Father Sydney’s face drains of what little color it had left. "The crypts... Merciful Saints, they must have found the old smuggling tunnel." 
    *   A heavy *CRACK* of splintering wood echoes from the sanctuary outside the vestry, followed by the terrified screams of Maisie and Dougal. The gnolls have broken in.


**Scene 2: Vestry Triage & Healing Glue**
*   **Setting the Scene:** In the quiet, lamplit vestry (where Trip grabbed the muskets), Sydney rummages through a medical cabinet. 
*   **Healing Mechanics:** Trip asks for a drop of that miracle potion for his torn-up feet and Banjo's leg. Sydney scoffs, explaining that Alchemical Potions are exorbitant luxuries meant strictly to pull a soul back from the brink of death. 
*   **The Glue:** Instead, Sydney pulls out a pungent, thick salve—a "healing glue." He applies it to Trip's bleeding soles and collarbone, and then to Banjo’s gashes. The glue stings fiercely but binds the torn skin together instantly, speeding up natural recovery. Banjo complains telepathically to Trip that it smells worse than the gnolls, but admits it does the trick. 
*   **Banjo's Treat:** To keep the dog quiet, Sydney actually tosses Banjo a chunk of stale communion bread, cementing the priest as an okay guy in Banjo's book.

**Scene 3: The Infodump (Natural Philosophy & Magic)**
*   **The Stat System:** As he works, Sydney explains what Maisie meant. He explains that Stats are a "natural philosophy" used to measure human limits. He breaks down the 0 to 100 scale, explaining that stats are divided into physical, mental, and magical attributes. Each person has a "current rank" and a "potential maximum" they can train toward. An average farmer might have a Might of 10; fighting a gnoll barehanded implies a Might well over 20 or 30.
*   **The Magic Bond:** Trip asks if telepathy is one of those stats. Sydney looks confused until Trip admits that he and Banjo have been talking in his head. Sydney is stunned. He explains that magic is real, but a rare gift. Trip realizes that whatever brought them to Rhul forged a magical bond between him and his dog, but admits to himself (and Banjo) that he has absolutely zero idea how to control its "capacity" or "power"—right now, it just lets them chat and share emotions.

**Scene 4: The Secret History of Earth and Rhul**
*   **The Confession:** Sydney locks the vestry door and demands to know where Trip is from. Trip admits he's from Wirt County, West Virginia, on a planet called Earth.
*   **The East India Company:** Sydney pales, but isn't entirely shocked. He reveals that the Canthican Church knows of "Outworlders." In fact, centuries ago, a massive group of men claiming to work for something called the "British East India Company" arrived. They brought knowledge of black powder and muskets, totally upsetting the balance of power and saving humanity from total elvish subjugation—thus birthing the Corvish Empire.
*   **The Language Curse:** Trip notes that everyone speaks English (or Corvish), and asks if he can write a note or look at a map. Sydney stops him, pulling out a book to show that everything is written in a flowing, alien script. Sydney explains the Elves, terrified of Earth’s disruptive knowledge, placed a powerful planar curse on the Latin alphabet. If you write with it on this world, the paper will instantly rot and turn to ash. 
*   **The Warning:** Sydney grabs Trip by his bare, glue-covered shoulders. He warns Trip that he must *never* reveal his origins. King Calador Half-Elven, ruling from Dornon, shares the elvish hatred of offworlders. If the Crown or the nobles find an Outworlder, they will dissect him, imprison him, or execute him. Trip realizes with a sinking stomach that his total lack of knowledge about this world isn't just an inconvenience—it's a deadly liability. He will have to craft a watertight cover story.

**Scene 5: The Cliffhanger**
*   **The Interruption:** Just as the weight of Trip's new reality settles in, Banjo stops chewing his stale bread. The hound’s ears prick up, and the fur on his spine bristles.
*   **The Warning:** *Boss,* Banjo says in Trip's mind, his mental voice dropping its usual goofy tone. *The big coons. I smell 'em again. And they ain't outside no more.*
*   **The Breach:** Trip hushes the priest. He strains his ears. The heavy oak doors at the front of the church are silent. But from somewhere *beneath* the floorboards—growing louder by the second—comes the frantic yipping, scratching, and snarling of the gnoll pack.
*   **The Realization:** Sydney’s face drains of all remaining color. "The crypts," he whispers in horror. "Saints preserve us... they found the old smuggling tunnel." 
*   **End Chapter:** Trip grabs a reloaded musket as the sound of splintering wood echoes from the sanctuary where the children are waiting.

"""
