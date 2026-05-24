import sys
sys.dont_write_bytecode = True
from chapters import get_all_chapters
from util.files import write_file

output = """
I am working on a Space Opera/Fantasy pseudo-19th-century colonialist military adventure story story with no working title. Have a read:
"""

for chapter in get_all_chapters():
    output += chapter.prompt_entry() + "\n"

output += """From this, I'd like you to pick a scene that appeals to you and prepare an AI image prompt describing it. Please be sure to include style guidelines that would result in a Bruce Timm style of cartoon art, i.e.  a distinctive, highly stylized 2D animation aesthetic that blends classic American comic books, 1940s–1950s cartoon elegance, and Art Deco influences into a sleek, modern heroic look.
Line work: Bold, confident black ink outlines with varying thickness (thicker on outer contours, thinner on interior details). Clean, graphic, and economical — no sketchy or painterly lines.
Shapes and proportions: Highly exaggerated, idealized anatomy. Males have massive shoulders, narrow waists, long limbs, and square jaws. Females feature extreme hourglass figures (very small waists, broad hips, long legs) with elegant, stylized faces. Heads are relatively small compared to bodies.
Color and shading: Flat, vibrant, limited color palettes with strong saturation. Minimal cell shading or simple gradients. Heavy use of solid blocks of color and high contrast. Dramatic, noir-influenced lighting with deep shadows and strong rim lighting.
Facial features: Large, expressive eyes (often almond-shaped or angular), minimal nose detail (often just a simple L-shape or shadow), strong eyebrows, and stylized mouths. Faces feel both heroic and slightly retro.
Overall aesthetic: Streamlined, graphic, and iconic. Think "comic book come to life" with a 1990s-early 2000s animation sensibility — elegant yet powerful, sexy without being crude, and always prioritizing strong silhouettes and readability.
Texture and finish: Smooth, cel-shaded surfaces with almost no texture or painterly brushwork. Everything feels crisp and illustrative.

Thank you!"""
write_file(output)
