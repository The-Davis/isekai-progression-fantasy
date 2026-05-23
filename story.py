from datetime import datetime
from models.story import Story


current_story = Story(
    title="A Neophyte's Guide to the Planes",
    genre="Absurdist planar fantasy adventure story",
    setting_notes="""The planes are real. Magic is real. The vastness of the cosmos is overwhelming. Humanity isn't invited, but they sure do make good passengers.
    Our main viewpoint character finds himself carried off on adventure, a la Arthur Dent (minus the exploding Earth. Earth's fine. Also, he's American, not British).
    Travelling on some sort of Spelljammer-like planar vessel between worlds, our hero has odd adventures. It is an action-oriented story, but with some absurdity akin to that of Douglas Adams.
""",
    start_date=datetime(year=2026, month=5, day=23, hour=16, minute=55)
)
