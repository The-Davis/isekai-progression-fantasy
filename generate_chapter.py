import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Father Sydney remarks that Trip has shown excellent pain tolerance. His Endurance attribute must be high. Perhaps twenty-five?
Trip says he doesn't rightly know what that means. Little miss Maisie mentioned words like that, but to him "endurance" is just a fancy word for not getting tired while working.
Father Sydney should be very excited when talking about "the Outworld", "geeking out", so to speak.
Sydney is surprised by this. He thought the outworld was a place of great learning. Whenever outworlders arrive in numbers, it is highly disruptive and heralds great change. The last time that happened was nearly four hundred years ago, when nearly two hundred people from something called the "British East India Company" showed up all at once. Their knowledge of gunpowder and firearms changed so much. It's why Corva is a kingdom rather than a mere electorate in the Erlenreich, you know.
Trip admits that no, he does not know, but that "East India Company" sounds sort of familiar. Did them British fellas teach you all English?
English? Father Sydney doesn't know the word.
The language we're speaking. It's English, unless I hit my head real hard and didn't realize it. I also heard you say a word or two of Latin, unless I misheard, along with some words I don't rightly know at all.
Sydney says the language they're sharing is called Corvish in this land, and it predates the British arrival. The "church tongue" is spoken only by the clergy, and only high-ranking ones know its history, something he hopes to learn someday. Mankind's arrival on this world is a fascinating subject and a passion of his, he confesses.
Trip is amused and says he never would have guessed (or "you don't say"). He redirects back to the attributes, asking again what they mean. Before Father Sydney can respond, Banjo starts barking.
Trip frowns and calls out to the hound mentally, but he gets no response. He remembers how he didn't hear the dog when Banjo was outside fighting the gnolls and the church door separated them either. Is their new bond limited to line of sight?
Not pondering it further, he leaves the vestry. Immediately he's greeted by the sight of Banjo barking at a dark corner, and his mental voice cries out in warning that them big coons are coming. They ain't scratching at the front door no more and I got to thinkin they must be coming. I was right!
From somewhere beneath the floor, growing louder by the second, comes the frantic yipping, scratching, and snarling of the gnoll pack.
Trip looks at Father Sydney. "Reverend... what's underneath this floor?" 
Father Sydney realizes with horror: The crypts... Merciful Saints, they must have found the old smuggling tunnel. It's so parishioners can escape the elves, but--
A heavy *CRACK* of splintering wood comes from beneath the altar, followed by the terrified screams of Maisie and Dougal. The gnolls have broken in.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.



Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.







**Scene 2: Vestry Triage & Healing Glue**
*   **Setting the Scene:** In the quiet, lamplit vestry (where Trip grabbed the muskets), Sydney rummages through a medical cabinet. 
*   **Healing Mechanics:** Trip asks for a drop of that miracle potion for his torn-up feet and Banjo's leg. Sydney scoffs, explaining that Alchemical Potions are exorbitant luxuries meant strictly to pull a soul back from the brink of death. 
*   **The Glue:** Instead, Sydney pulls out a pungent, thick salve—a "healing glue." He applies it to Trip's bleeding soles and collarbone, and then to Banjo’s gashes. The glue stings fiercely but binds the torn skin together instantly, speeding up natural recovery. Banjo complains telepathically to Trip that it smells worse than the gnolls, but admits it does the trick. 
*   **Banjo's Treat:** To keep the dog quiet, Sydney actually tosses Banjo a chunk of stale communion bread, cementing the priest as an okay guy in Banjo's book.


*   **The Realization:** Sydney’s face drains of all remaining color. "The crypts," he whispers in horror. "Saints preserve us... they found the old smuggling tunnel." 
*   **End Chapter:** Trip grabs a reloaded musket as the sound of splintering wood echoes from the sanctuary where the children are waiting.

"""
