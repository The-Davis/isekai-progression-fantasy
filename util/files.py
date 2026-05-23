from constants import spacer, blank


def write_file(content: str):
    with open("prompt.txt", mode="w", encoding="utf-8") as f:
        f.write(content.replace(spacer, blank).strip())
