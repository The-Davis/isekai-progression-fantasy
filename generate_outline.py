import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
from chapters import get_all_chapters
from outline import get_outline
from constants import STORY_DESCRIPTION


def generate_outline_prompt() -> str:
    output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.
{STORY_DESCRIPTION}
"""
    
    if get_codex():
        output += "Here are some details about the world our story is set in:\n"
        for entry in get_codex():
            output += entry.about() + "\n"
    
    if get_characters():
        output += "Here are some notes about the characters in the story:\n"
        for character in get_characters():
            output += character.about() + "\n"
    
    if get_all_chapters():
        output += "Here is the story so far:\n"
        for chapter in get_all_chapters():
            output += chapter.prompt_entry() + "\n"
    
    if get_outline():
        output += "Here is the outline so far:\n"
        for outline in get_outline():
            output += outline.prompt_entry() + "\n"

    output += """Your task is to create a broad outline for an upcoming section of the story. Here is what we have to work out now:

Our story starts with a description of the boy's life in his riverside town, including his playful tricks and minor punishments, exploration, trips down the river and to the sea, and so on, but also introduce magic and the system that runs the Eidolith worldcraft through that process.
Our fifth chapter needs to continue to set that stage. We opened it nicely, putting Talmon and Jasper Moray together. We can use the rest of the chapter as a primer for "what's actually going on" for the reader and for Tal.
As Tal leads Jasper through town and back to his house, he becomes infatuated with magic and manages to coax the wizard into telling him things. We'll need to work out an introduction between the pair, since Jasper knows Talmon's name but Tal doesn't know his.
I'm thinking we can show that Jasper has an artifact that lets him see his own six attributes and his own mana core. When he lets Tal see it, Tal realizes that this is the source of the strange feeling of warmth, not Jasper himself.
The artifact, Tal privately muses, is part of the same system as the "proxy interface" the fire called itself. Tal prods and pries, and Jasper teasingly gives him some information, hinting that mana cores are something people have that can be awakened to give access to magic, but he declines to tel Tal how to do it.
Jasper does reveal that he got the artifact in a dungeon, but that this particular type of artifact isn't particularly rare. If it was, the kingdom would doubtless take it from him. They do that sometimes, and while it rankles Jasper, he has to admit they give a fair price for what they take.
Jasper hints that he's in Larchleah following rumors about a dungeon and an artifact, but he doesn't go into more detail. They arrive at the house and we wrap it up with a summary of the social niceties of getting a boarder settled.
    
Please ensure that the outline fits into the world I've provided, provides the characters with interesting challenges and dynamic scenes, and doesn't contradict anything in the notes or story so far.
Thank you."""
    return output


write_file(generate_outline_prompt())

"""



Here is the story so far:
Act One - Our story starts with a description of the boy's life in his riverside logging town, including his playful tricks and minor punishments, exploration around the sawmill, trips down the river and to the sea, and so on.

My plan is to put together fifteen to twenty chapters of material for the first act. We need one sentence for each. Here is an example of the length. Do not exceed this length for each chapter.

Chapter 1: After a brief introduction of his memories of reincarnation, Tal tells how he met Wicket. He hides from his mother after he does something bad. He tricks her to escape, meets a new kid in town (Wicket), gets in a fight with him, becomes best friends (because that's what boys do), and sneaks home.


Our first major event involves him and his friends when they witness a murder and swear each other to secrecy out of fear, leading to profound guilt when an innocent man is falsely accused.
Chapter 19: Tal, Cord, and Wicket witness Hollis digging up a grave while Jasper Moray supervises. Hollis and Jasper fight and Hollis is knocked out. Gobber Dob then appears (the boys will notice him lurking around in an earlier chapter). It becomes clear Gobber and Jasper conspired to cut Hollis out of the deal, but then Gobber murders Jasper in the graveyard with Hollis' knife. The boys flee in terror as Gobber makes off with the artifact Jasper looted from the grave.
Chapter 20: The boys swear an oath of secrecy. An omen terrifies them.

Your task is to create twenty chapters of material to fill in the blanks.
We need Tal learning to do things and progressing slowly from comfortable, fun-loving boy to a more serious young man. We need interactions between Tal and Wicket and their family and friends. Lots of fun. The major beats we need to be sure to hit:
Long Tom returning home with Jasper as a passenger and Jasper taking up rooms at the Sager home. Long Tom reports a new foreman is coming to town (foreshadowing Rosie)
Tal learning about magic from Jasper and finding out he needs to awaken his mana core. Jasper won't tell him how, but does teach him a few fundamentals of the mental controls. Tal obsessively collects rumors and childish superstitions on how to do this.
Interactions with Hollis to show he's a friend to the children. Fearful sightings of Gobber Dob. Foreshadowings that he, Jasper, and Hollis are in cahoots over something.
Tal wooing Rosie. Jealousy between Clary and Rosie.
Interactions with Tal, Martha, Simmon, and Elsie. Work them in with the other kids.
Tal getting into trouble.

Please ensure that the outline fits into the world I've provided, provides the characters with interesting scenes, and doesn't contradict anything in the notes or story so far.
Thank you.





A boy seeks adventure but faces trouble from mischief, a witnessed crime, and awakening magic.

Step 2) Take another hour and expand that sentence to a full paragraph describing the story setup, major disasters, and ending of the novel.
This is the analog of the second stage of the snowflake. I like to structure a story as "three disasters plus an ending".
Each of the disasters takes a quarter of the book to develop and the ending takes the final quarter. I don't know if this is the ideal structure, it's just my personal taste.

Our story starts with a description of the boy's life in his riverside town, including his playful tricks and minor punishments, exploration around the sawmill, trips down the river and to the sea, and so on.
Our first major event involves him and his friends when they witness a murder and swear each other to secrecy out of fear, leading to profound guilt when an innocent man is falsely accused.
Fleeing town to avoid being called at the trial, he and his friends face serious hardships before finally returning and testifying. The real killer escapes, swearing vengeance.
After things return to normal and seem peaceful, the killer returns. The boy and a friend are pursued into a dungeon by the killer.
They manage to use the dungeon to get the killer killed, recover dungeon treasure, and thus earn a coveted spot in the kingdom's training lyceum.

This paragraph summarizes the whole story. Your back-cover copy should summarize only about the first quarter of the story.
Step 3) The above gives you a high-level view of your novel. Now you need something similar for the storylines of each of your characters.
Characters are the most important part of any novel, and the time you invest in designing them up front will pay off ten-fold when you start writing.
For each of your major characters, take an hour and write a one-page summary sheet that tells:

The character's name
A one-sentence summary of the character's storyline
The character's motivation (what does he/she want abstractly?)
The character's goal (what does he/she want concretely?)
The character's conflict (what prevents him/her from reaching this goal?)
The character's epiphany (what will he/she learn, how will he/she change?
A one-paragraph summary of the character's storyline
An important point: You may find that you need to go back and revise your one-sentence summary and/or your one-paragraph summary. Go ahead! This is good.
It means your characters are teaching you things about your story. It's always okay at any stage of the design process to go back and revise earlier stages.
In fact, it's not just okay, it's inevitable. And it's good. Any revisions you make now are revisions you won't need to make later on to a clunky 400 page manuscript.

Step 4) By this stage, you should have a good idea of the large-scale structure of your novel, and you have only spent a day or two.
So now just keep growing the story. Take several hours and expand each sentence of your summary paragraph into a full paragraph. All but the last paragraph should end in a disaster. The final paragraph should tell how the book ends.
This is a lot of fun, and at the end of the exercise, you have a pretty decent one-page skeleton of your novel. It's okay if you can't get it all onto one single-spaced page.
What matters is that you are growing the ideas that will go into your story. You are expanding the conflict. You should now have a synopsis suitable for a proposal, although there is a better alternative for proposals.

Step 5) Take a day or two and write up a one-page description of each major character and a half-page description of the other important characters.
These "character synopses" should tell the story from the point of view of each character.
As always, feel free to cycle back to the earlier steps and make revisions as you learn cool stuff about your characters.
I usually enjoy this step the most and lately, I have been putting the resulting "character synopses" into my proposals instead of a plot-based synopsis. Editors love character synopses, because editors love character-based fiction.

Step 6) By now, you have a solid story and several story-threads, one for each character. Now take a week and expand the one-page plot synopsis of the novel to a four-page synopsis. Basically, you will again be expanding each paragraph from step (4) into a full page. This is a lot of fun, because you are figuring out the high-level logic of the story and making strategic decisions. Here, you will definitely want to cycle back and fix things in the earlier steps as you gain insight into the story and new ideas whack you in the face.

Step 7) Take another week and expand your character descriptions into full-fledged character charts detailing everything there is to know about each character.
The standard stuff such as birthdate, description, history, motivation, goal, etc. Most importantly, how will this character change by the end of the novel?
This is an expansion of your work in step (3), and it will teach you a lot about your characters. You will probably go back and revise steps (1-6) as your characters become "real" to you and begin making petulant demands on the story.
This is good — great fiction is character-driven. Take as much time as you need to do this, because you're just saving time downstream.
When you have finished this process, (and it may take a full month of solid effort to get here), you have most of what you need to write a proposal.

Step 8) You may or may not take a hiatus here, waiting for the book to sell. At some point, you've got to actually write the novel. Before you do that, there are a couple of things you can do to make that traumatic first draft easier.
The first thing to do is to take that four-page synopsis and make a list of all the scenes that you'll need to turn the story into a novel. And the easiest way to make that list is . . . with a spreadsheet.

For some reason, this is scary to a lot of writers. Oh the horror. Deal with it. You learned to use a word-processor. Spreadsheets are easier. You need to make a list of scenes, and spreadsheets were invented for making lists.
If you need some tutoring, buy a book. There are a thousand out there, and one of them will work for you. It should take you less than a day to learn the itty bit you need. It'll be the most valuable day you ever spent. Do it.

Make a spreadsheet detailing the scenes that emerge from your four-page plot outline. Make just one line for each scene. In one column, list the POV character. In another (wide) column, tell what happens.
If you want to get fancy, add more columns that tell you how many pages you expect to write for the scene.
A spreadsheet is ideal, because you can see the whole storyline at a glance, and it's easy to move scenes around to reorder things.

My spreadsheets usually wind up being over 100 lines long, one line for each scene of the novel. As I develop the story, I make new versions of my story spreadsheet.
This is incredibly valuable for analyzing a story.
It can take a week to make a good spreadsheet. When you are done, you can add a new column for chapter numbers and assign a chapter to each scene.

Step 9) (Optional. I don't do this step anymore.) Switch back to your word processor and begin writing a narrative description of the story. Take each line of the spreadsheet and expand it to a multi-paragraph description of the scene.
Put in any cool lines of dialogue you think of, and sketch out the essential conflict of that scene. If there's no conflict, you'll know it here and you should either add conflict or scrub the scene.

I used to write either one or two pages per chapter, and I started each chapter on a new page.
Then I just printed it all out and put it in a loose-leaf notebook, so I could easily swap chapters around later or revise chapters without messing up the others.
This process usually took me a week and the end result was a massive 50-page printed document that I would revise in red ink as I wrote the first draft.
All my good ideas when I woke up in the morning got hand-written in the margins of this document. This, by the way, is a rather painless way of writing that dreaded detailed synopsis that all writers seem to hate.
But it's actually fun to develop, if you have done steps (1) through (8) first. When I did this step, I never showed this synopsis to anyone, least of all to an editor — it was for me alone.
I liked to think of it as the prototype first draft. Imagine writing a first draft in a week! Yes, you can do it and it's well worth the time. But I'll be honest, I don't feel like I need this step anymore, so I don't do it now.

"""