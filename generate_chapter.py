import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """Trip drops the spent musket and snatches the second, then fires just as a gnoll lunges for Banjo, who stubbornly ignores Trip's orders to retreat. The shot takes the beast in the neck, sending it spinning into the dirt.
Though he has powder and shot, Trip is not trained to load while snarling gnolls charge at him with spears. Banjo barks and snarls at the creatures as they draw near, and Trip tries to reload. He remembers how they took off running last time, but they seem to have their courage this time.
He soon sees why: more are running up, drawn by the church bell. It may be meant to rouse the village to arms, but it seems to be drawing a whole mess of bad critters. Trip and Banjo briefly argue: Banjo wants to stay and fight more, Trip wants to get back inside and bar the door.
Trip finally just grabs the big coon hound by the scruff and drags him inside. He hauls the door shut just as the gnolls charge the steps. The vicar abandons the bell rope just long enough to help Trip lift the iron-reinforced wooden bar and drop it into the brackets across the doors.
The gnolls slam into the wood outside, howling and scratching furiously, but the masonry and oak hold firm.
Trip slides down the door, totally exhausted, chest heaving. Banjo nudges Trip's bloody chin with a wet nose, and tells Trip he thinks he deserves a treat. Trip says he has no treats. Banjo says this is a church. Don't they have bread and wine? It's not sausages, but it'll do.
Trip laughs. They're safe, for the moment.
We'll end the chapter on that note.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.



Work in somewhere, maybe in chapter 5, that Glenrowan's church is a "chapel of ease" since they're so far from the parish church.
Bider John, who isn't present, is the porter for the chapel.



"""
