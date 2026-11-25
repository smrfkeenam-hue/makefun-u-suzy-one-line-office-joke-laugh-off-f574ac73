import os

# One original one-line office joke: the printer jams on the resignation letter.
ENTRY = "The office printer finally jammed on something important: my resignation letter."

# Write exactly the entry, with no trailing newline, so the gate sees 80 chars.
with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
