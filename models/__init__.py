import sys
sys.dont_write_bytecode = True
from typing import Optional


def prompt_header(genre: str, title: Optional[str] = None) -> str:
    if title is None:
        title = "no working title"
    else:
        title = f"a working title of \"{title}\""
    if genre.lower()[0] in 'aeiou':
        genre = f"an {genre}"
    else:
        genre = f"a {genre}"
    return f"I am working on {genre} story with {title}."
