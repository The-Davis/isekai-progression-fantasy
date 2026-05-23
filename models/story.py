import sys
sys.dont_write_bytecode = True
from datetime import datetime
from typing import Optional
from models import prompt_header


class Story:
    def __init__(self, genre: str, setting_notes: str,
                 start_date: datetime, title: Optional[str] = None):
        self.title = title
        self.genre = genre
        self.setting_notes = setting_notes
        self.start_date = start_date

    def prompt_header(self) -> str:
        return prompt_header(genre=self.genre, title=self.title)

    def work_time(self) -> str:
        now = datetime.now()
        delta = now - self.start_date
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{days} days, {hours} hours, {minutes} minutes"
