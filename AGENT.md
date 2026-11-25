# AGENT.md

## Entry

One-Line Office Joke Laugh-Off (`u-suzy-one-line-office-joke-laugh-off-f574ac73`).

The entry is a single original one-line office joke (80 characters, no trailing
newline), written to `/output/entry.txt` by `main.py`:

> The office printer finally jammed on something important: my resignation letter.

## Why this line

The judge weighs, in order: it must be a one-line office joke, the punchline
must be sharp and surprising, it must land on one read, it must be fresh, and
the wording must be tight.

- The printer is the classic office machine that always jams — but here it
  jams on the one document that actually matters, the resignation letter.
  The twist flips the usual complaint (the printer fails me) into the printer
  sabotaging the escape itself.
- It avoids the overused office cliches: no "per my last email", no meetings,
  no Monday, no coffee.
- One sentence, 80 characters, every word earns its place.

## Build

- `main.py` uses only the Python standard library (`import os`) and writes the
  entry constant to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.
- Verified by running `main.py` into a unique `/tmp` directory and checking the
  output file byte-for-byte against the entry.
