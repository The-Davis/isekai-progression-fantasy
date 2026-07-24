import sys
sys.dont_write_bytecode = True
from util.files import write_file
from codex import get_codex
from characters import get_characters
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

    output += """Your task is to create an image prompt for a character in the story.

Your output should read like so:

"Please create an image of a highly detailed fantasy character portrait.
DESCRIPTION: [describe the character in your words, including outfit, expression, accessories, and general appearance].
POSE: [This is at your discretion.]
SETTING: [This is at your discretion.]
LIGHTING: [This is at your discretion.]
ART STYLE: Bruce Timm style, 1990s classic American 2D animation. Bold, confident black ink outlines with varying thickness. Clean, graphic, and economical linework with no sketchy or painterly lines. Minimal nose detail with a simple L-shaped shadow, strong eyebrows, stylized mouth. Flat, vibrant, limited color palette with strong saturation. Heavy use of solid blocks of color and high contrast. Dramatic lighting. Smooth, cel-shaded surfaces with crisp, illustrative finish. Sleek, modern look."

Fill out the character DESCRIPTION, POSE, SETTING, and LIGHTING based on your read of the world and the character notes I provided.

The picture for this should be of little Elsie Sager. Don't forget to have her yellow hair match her brother Tal's.

Thank you."""
    return output


write_file(generate_outline_prompt())
