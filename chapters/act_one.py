import sys
sys.dont_write_bytecode = True
from models.chapter import Chapter

chapter_one = Chapter(
    title="Chapter One",
    content="""If a man claims to know exactly how he managed to step straight out of the dark hollers of the Appalachian Mountains and into a world completely unacquainted with the great state of West Virginia, you can safely write him off as a liar. It happened to me, but I certainly couldn't tell you how. 
One minute I was busting through a tangle of rhododendron in the dead of night, following the sweet, ringing music of my coonhound on a fresh trail, and the next, I was flat on my back in a field of purple heather under a sky boasting two moons.
Right before everything changed, I'd got a feeling, a mighty peculiar one. It was this sudden, deep-bone tingle, kinda like the prickle that dances across your skin when a bolt of lightning strikes too close to the front porch. Only, this hum settled right into my marrow and stayed there, buzzing like a nest of angry hornets beneath my skin. I didn't understand it in the slightest. By and by, the shivering stopped, I opened my eyes, and that's when I realized I was flat on my back.
I lay there a spell, trying to blink the double moons out of my vision, thinking I must've hit my head on a low-hanging branch, but the moons failed to come back together no matter how much I blinked. One was a pale, dusty yellow, not too far off from the one I'd known all my life, but the other glowed a sullen shade of bruised plum. It dawned on me right about then that the night air was uncommonly brisk against my skin. All of my skin.
I sat up, took a quick inventory, and found myself entirely in the altogether. I was bereft of my boots, my denim trousers, my flannel shirt, and, most grievously, my hunting rifle. That last one was a bitter pill to swallow. It was my grandfather's Winchester, as fine a lever-action as a man could ever hope to carry into the woods. Losing your pants in the middle of the night is an embarrassment, but losing a piece of family history is a downright tragedy.
"Well... how 'bout that?" I murmured to the empty air, rubbing my bare arms against the chill of the night.
*It ain't right, Boss. That's how 'bout it.*
I jumped like a spooked bullfrog and near pulled a muscle trying to cover my particulars. The voice was deep, gruff, and amiable, sounding a lot like an older fella who'd just popped the tab on the third beer of the afternoon. Except it hadn't *sounded* like anything at all, it'd just popped right into my head without bothering so much as a 'by your leave' to my ears. I looked around for the source of the voice (for want of a better word), but all I saw was Banjo.
He was standing about ten paces off, illuminated by that bruised-plum moonlight. There was no mistaking him for some other hound. Banjo's handsome head has distinct dark spectacle marks framing his eyes. He stared at me, cocked his head, and the voice echoed in my skull once more.
*Chief, I'm gonna need some answers.* Banjo let out a low whine even as his words rattled inside my head. *Where's the tree? More importantly, where's the coon that was in the tree? I had him, Boss. Had him dead to rights.*
I pressed the heels of my hands against my eyes. "I really did hit my head. Must be. I tripped over a root, hit my head, and now I'm dreaming."
Banjo trotted over and bumped his cold nose inquisitively against my bare knee. I flinched.
*Boss, I don't know how to tell you this, but your pants have flown the coop.* He sat back on his haunches and lifted a paw to scratch at his bare neck. *What the Sam Hill?* He stopped and turned in a circle, trying to get a look at himself. *Aw, nuts. My collar's gone. I liked that collar. It jingled. Where's all our stuff, Boss? Did that thieving coon nab our stuff?*
I looked at his neck. Sure enough, his faded orange nylon collar with the brass nameplate was gone, vanished just like my boots and my grandpa's Winchester.
""",
)


act_one_chapters: list[Chapter] = [
    chapter_one,
]
