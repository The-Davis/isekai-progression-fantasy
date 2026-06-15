from datetime import datetime
from models.story import Story


current_story = Story(
    title="A Neophyte's Guide to the Planes",
    genre="A planar progression fantasy adventure story",
    setting_notes="""The planes are real. Magic is real. The vastness of the cosmos is overwhelming.
    Our main viewpoint character finds himself abducted and carried off on a Spelljammer-like planar vessel to be sold in a flesh market in a distant plane of existence.
""",
    start_date=datetime(year=2026, month=6, day=13, hour=15, minute=2)
)
