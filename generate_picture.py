import sys
sys.dont_write_bytecode = True
from chapters import get_all_chapters
from util.files import write_file
from constants import STORY_DESCRIPTION

output = f"""You are a worldbuilding and storytelling assistant helping me, an author, develop my fictional world and story.
{STORY_DESCRIPTION}
"""

for chapter in get_all_chapters():
    output += chapter.prompt_entry() + "\n"

output += """Your task is to create an image prompt for a scene from a chapter in the story.

Your output should read like so:

"Please create an image of a highly detailed fantasy scene.
DESCRIPTION: [describe the specific moment in your words, including character poses, expressions, outfits, expression, accessories, and general appearance].
SETTING: [This is at your discretion.]
LIGHTING: [This is at your discretion.]
ART STYLE: Bruce Timm style, 1990s classic American 2D animation. Bold, confident black ink outlines with varying thickness. Clean, graphic, and economical linework with no sketchy or painterly lines. Minimal nose detail with a simple L-shaped shadow, strong eyebrows, stylized mouth. Flat, vibrant, limited color palette with strong saturation. Heavy use of solid blocks of color and high contrast. Dramatic lighting. Smooth, cel-shaded surfaces with crisp, illustrative finish. Sleek, modern look."

Fill out the character DESCRIPTION, SETTING, and LIGHTING based on your read of the chapter and scene I provided.

The picture for this should chapter two, where the viewpoint character, Tal, fights with Wicket.

Thank you!"""

write_file(output)
