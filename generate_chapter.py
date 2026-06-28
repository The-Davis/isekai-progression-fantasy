import sys
sys.dont_write_bytecode = True
from prompts.chapter import generate_chapter_prompt
from util.files import write_file
from style import main_style  

chapter_outline = """The conversation shifts to the Church. Trip is amazed the Christian faith exists here. Sydney explains the Church has survived on Rhule for nearly two thousand years. The elves outlawed it and violently persecuted Christians, claiming Earth and Christ were myths. The Church survived in secret, keeping oral traditions (the Canthica) alive. When Corvland won its independence, its first kings legalized the faith. Now, a secret mandate of the Church is to protect Outworlders from the elves.
Trip says whether Father Sydney's helping him out of duty to the faith or kindness, he's much obliged. He asks if the father would be willing to tell him about these attributes and numbers he and the kids kept talking about.
Father Sydney's eyes light up. Now that is an interesting question.
We'll end the chapter with that to hook the next one.
"""

write_file(generate_chapter_prompt(chapter_outline=chapter_outline, style=main_style))

"""
You can stop there and we'll edit before I provide the next section.


We'll end the chapter on that note.

Trip learns a bit more about the Canthican structure here: Father Sydney is only a Vicar, not the parish priest. Because the population is so spread out, this church serves as a "chapel of ease" for locals who can't hike to the main parish building miles away, where the parish priest holds Mass.






*   **Explaining Attributes:** Trip brings up the numbers Maisie and Sydney mentioned earlier (Might, Endurance, etc.). He asks if people here can just "see" a person's stats like in a video game (though he'd frame it as "like a baseball player's stat card").
*   **The Mechanics of Stats:** Sydney clarifies that there is no magical floating text. Attributes are a formalized "natural philosophy"—a science of measuring human capability. 
    *   There are Physical, Mental, and Magical categories. 
    *   Each has five measurements: Power, Control, Speed, Capacity, and Recovery. (For example, Physical covers Might, Finesse, Agility, Endurance, and Vigor).
    *   The Church and the elves have specialized rituals to accurately measure these attributes.
    *   Sydney explains that the only way to increase these attributes is through rigorous hard work, aging, and training. While rumors say the elves have dark, magical means of artificially enhancing attributes, Sydney has never witnessed it. 

**Scene 5: The Ambush (The Climax/Cliffhanger)**
*   **A Crash Course in Corvish:** To pass the time and solidify the cover story, they do a montage of Sydney teaching Trip basic Corvish customs, slang, and etiquette so he can pass as a Fenshire man when they meet Laird MacTavish.
*   **The Atmosphere Shifts:** It approaches noon. The sun should be burning off the morning dew, but instead, a thick, unnatural fog begins to roll rapidly down the jagged peaks and fill the glen. The temperature drops sharply, turning their breath to white plumes.
*   **The Warning:** Banjo’s playful demeanor instantly vanishes. His hackles rise, and he drops into a low, predatory stalk. He telepathically warns Trip: *“Boss. Trouble. Smells like wet fur and bad meat. Worse than the coons. They're circling us.”*
*   **The Reveal:** Trip raises his musket, and Father Sydney draws his pistol, his face pale. Out of the swirling, freezing mist step three massive shapes. 
*   **The Cu-Sith:** Father Sydney breathlessly identifies them: *Cu-Sith*, the Black Dogs of the moor. They are magically warped hounds the size of young calves, with shaggy, matted fur and glowing, hateful red eyes. 
*   **The Cliffhanger:** The demonic beasts bare fangs the size of railroad spikes and let out a guttural, terrifying snarl that shakes the ground. Unintimidated, Banjo steps directly in front of Trip, squares his sturdy blue-tick chest, and unleashes a deafening, ringing bay of challenge right back at them. The massive beasts lunge through the mist just as the chapter ends. 



"""




"""

### **Chapter Nine: The Dragoons and the Laird**
*   **The Skirmish:** The Black Dogs are terrifyingly fast (high Agility and Finesse). Trip attempts to fire, but his musket flashes in the pan due to the damp. He's forced to use the musket as a club, utilizing his high Might to hold a beast at bay. Banjo tackles another, furious that these "ugly shadow-dogs" are ruining his walk, but even he is struggling against their unnatural strength. 
*   **The Rescue:** A sudden volley of precise carbine fire rips through the fog. Several men on horseback charge into the fray. They wear green-and-brown tartans, wield sabers, and ride sturdy Bannish moor-ponies. The dragoons make quick work of the remaining beasts. 
*   **Introductions:** The dragoon sergeant recognizes Father Sydney. Sydney introduces Trip as a southern volunteer with a knack for marksmanship. Banjo stares at the horses in awe, telepathically marveling at the "giant dogs" the soldiers get to ride. 
*   **Arrival at Glenrowan:** The dragoons escort the trio the rest of the way. Glenrowan is a bustling, industrious Highland keep nestled in a sweeping glen, ringed by heavy stone walls. It feels like a proper military staging ground, full of marching infantry and the drone of bagpipes. 
*   **Meeting the Laird:** They are brought before Laird Lachlan MacTavish. Lachlan is precisely as described: barrel-chested, mutton-chopped, eating a bowl of hearty venison stew (which drives Banjo telepathically insane with hunger), and rolling his r's amiably. 
*   **Earning Trust:** Sydney explains the necromancer threat, but Lachlan is hesitant to commit his dragoons without firm proof of an organized horde, as he has his own lands to defend. Trip steps up. Speaking contractor-to-laird, and showing the pragmatic, level-headed nature of a seasoned woodsman, he explains the tactical situation, the layout of the gnolls, and how they blew the crypt. Lachlan respects Trip's scarred hands, lack of panic, and physical bearing. Invoking Saint Michael, Lachlan declares Trip a "proper fighting man" and orders the dragoons to saddle up. 

### **Chapter Ten: The Battle of the Glen**
*   **Gearing Up:** A brief slice-of-life moment of military preparation. Trip is given a proper meal (Banjo finally gets his sausages), a spare horse to ride, and a rifled cavalry carbine. Trip feels right at home with the new weapon. 
*   **The Twilight Return:** The dragoon detachment, led by Lachlan and guided by Trip, rides hard back to the village. They crest the valley ridge just as the sun dips below the horizon and the violet moon rises. Down below, the gnoll horde is massing against the village barricades. At the rear of the horde is a figure in tattered robes wielding a jagged staff—the Necromancer. 
*   **The Charge:** Lachlan draws his saber and orders the charge. This is pure Napoleonic-era cavalry action. The dragoons sweep down the hill. Trip rides with them, firing his carbine from the saddle with deadly accuracy. Banjo bounds alongside them, hitting the gnoll flank like a furry cannonball, utterly fearless and ripping through the undead ranks. 
*   **The Climax:** The cavalry shatters the gnoll lines, relieving Hamish and Bider John at the barricades. Trip and Lachlan push deep into the enemy ranks toward the Necromancer. The dark mage unleashes a pulse of Everdark magic that spooks the horses, dismounting Trip. Using his high Agility and Vigor, Trip rolls, comes up to one knee, and takes a breath. Ignoring the chaos, he takes a crack shot that shatters the Necromancer’s staff. 
*   **The Retreat:** His focus destroyed and his horde crumbling under the dragoons' sabers, the Necromancer shrieks and flees into the deep shadows of the Everdark, surviving to be a recurring villain. The remaining gnolls are swiftly routed and put down. 
*   **Resolution and Enlistment:** The village is saved. As the men clean their weapons and tend to the wounded, Lachlan claps Trip on the shoulder. Impressed by his marksmanship, his poise under fire, and his vicious hound, the Laird formally offers Trip a place as a scout in his regiment. Trip realizes that if he's stuck in this world, military life offers steady pay, a roof, a way to learn about the world, and most importantly, three square meals a day for Banjo. He accepts. The chapter ends on a cozy, victorious note as the village and the soldiers share a celebratory round of ale by the fire.







### **Chapter 9: The Dragoons and the Laird**
*   **The Rescue:** Just as the beast is about to take Trip's head off, a thunderous volley of musket fire tears through the defile, shattering the Black Dogs' shadowy forms. Enter a patrol of the **Bannish Dragoons**—heavy cavalrymen wearing dark green tailcoats and Bannish tartan over their shoulders.
*   **Military Camaraderie:** The Dragoon Sergeant (a gruff veteran with a scarred face) rides down, impressed that a civilian and his hound held their ground against Everdark hounds. Banjo proudly struts around the massive cavalry horses, telepathically critiquing their lack of tracking skills while trying to sniff their saddlebags for rations.
*   **Arrival at Glenrowan:** The dragoons escort the trio the rest of the way to Glenrowan. It is a sprawling, industrious military encampment surrounding a stout stone keep. Trip gets his first taste of "A Soldier's Life"—campfires, the smell of hearty stews boiling (which drives Banjo insane with hunger), and men diligently cleaning weapons. 
*   **Meeting the Laird:** They are brought before Laird Lachlan MacTavish. Lachlan is exactly as described: eating a bowl of thick stew, clasping his stomach, and swearing by Saint Sebastian about the lack of good salt. Sydney introduces Trip as a hero from the south.
*   **Gaining Trust & Loot:** Lachlan is skeptical of this wiry "southerner." He tests Trip by tossing him a rusted musket and demanding he strip it. Trip’s practiced, contractor-calloused hands strip the lock and barrel in record time. Impressed by Trip's Finesse and Agility attributes, and noting Banjo's fierce discipline, Lachlan welcomes him. 
*   **Mobilization:** Sydney delivers the news of the gnoll necromancer. Lachlan's jovial demeanor instantly drops. He invokes Saint Michael and orders his company to mount up. Realizing Trip left his Winchester back on Earth and only has a standard musket, Lachlan gifts him a **Bannish Rifled-Musket** (this world's equivalent of a Baker Rifle). Trip feels the balance and immediately falls in love; it’s a sniper’s weapon, perfect for a West Virginia hunter.

### **Chapter 10: Twilight Charge**
*   **The Ride Back:** The dragoon company rides hard across the moor to beat the sunset. Trip rides double with a cavalryman while Banjo runs effortlessly alongside the horses, proving his incredible Vigor stat. Banjo chatters happily about how he feels like a cavalry dog in one of his old western TV shows.
*   **The Battlefield:** They arrive at the ridge above the village just as the violet moon rises. Down in the basin, the surviving villagers are holding out at the barricaded church, but a massive warband of gnolls is swarming the perimeter. At the rear of the horde stands the **Necromancer**—a towering, twisted gnoll shaman clutching a staff of bone, chanting to raise the dead from the previous night's skirmish.
*   **Sharpe's Rifles Action:** Lachlan orders the dragoons to form up. He looks to Trip and gives him a simple order: *Break the shaman's concentration.* Trip dismounts, finds a rocky vantage point, and sights down his new rifle. He takes a breath, calculates the wind, and fires. The shot is perfect, striking the shaman in the shoulder and breaking the necromantic spell just as the dead begin to twitch.
*   **The Cavalry Charge:** With the spell broken, Lachlan draws his heavy broadsword. To the terrifying drone of Bannish bagpipes, the dragoons charge down the slope. It is a brutal, glorious clash of sabers and hooves. Banjo darts into the fray, hamstringing gnolls and protecting the fallen dragoons, reveling in the chaos.
*   **The Retreat:** The shaman, wounded and realizing his horde is being slaughtered by the dragoons, uses a flash of violet magic to blind his pursuers and flees into the Everdark. He escapes, establishing himself as a recurring threat for the future.
*   **Aftermath and Slice of Life:** The village is saved. Hamish and Bider John reunite with Father Sydney. The dragoons set up camp in the village square. Lachlan claps Trip on the shoulder, noting that a man who can shoot like that and survive the Everdark belongs in the King's service. He offers Trip a place as a civilian scout attached to his dragoons. 
*   **Wrap-up:** Trip accepts, seeing it as the best way to earn a living, find answers, and keep his Outworlder secret safe among men who value actions over origins. The act ends with a cozy scene by the campfire: Trip cleaning his new rifle, while Banjo finally gets the massive bowl of Bannish stew he was promised, telepathically declaring this new planet "the greatest place in the whole universe."

"""