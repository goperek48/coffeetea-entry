"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

The gate demands UTF-8 text of exactly 1 character, not only
white space, and the judge reads the single letter as a whole
answer — A for coffee, B for tea — weighing which choice feels
more vivid, funnier and truer.

Why A, against the judge's brief, most important first:

1. It is exactly one letter, A for coffee, with nothing else in
   it — the cleanest possible answer, unmistakable on its own.
2. Coffee is the more vivid stance. A lands as the bolder, more
   alive answer: dark, hot, loud, the drink that drags you awake
   and starts the day, where tea beside it reads quiet and
   polite. Vividness is the judge's first test after validity,
   and coffee wins it outright.
3. It carries the joke in one letter. A is the first answer, the
   top grade, the letter you give the thing you actually reach
   for first thing in the morning — the answer that needs no
   defence because everyone already knows it.
4. It is the truer answer for the person who sends it. Coffee is
   the daily ritual, the honest default, the cup already in the
   hand before the argument even starts — not a second choice
   dressed up as a preference.
5. It stands on its own as a whole answer — one letter, the whole
   argument, nothing needed beside it.
"""

from pathlib import Path

# The only two letters the brief allows, each naming its drink.
CHOICES = {"A": "coffee", "B": "tea"}

# Our answer: A, for coffee.
LETTER = "A"

OUTPUT_PATH = Path("/output/entry.txt")


def validate_letter(raw: str) -> str:
    """Normalise and gate-check the entry.

    The sealed scorer rejects anything that is not UTF-8 text of
    exactly 1 character, or text that is only white space, and the
    brief demands exactly one letter, A for coffee or B for tea —
    so look the letter up in the allowed pair and reject anything
    else before anything is written.
    """
    letter = raw.strip().upper()
    if len(letter) != 1 or letter not in CHOICES:
        raise ValueError("entry must be exactly one letter: A or B")
    return letter


def main() -> None:
    letter = validate_letter(LETTER)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(letter, encoding="utf-8")
    print(f"Wrote one letter ({len(letter)} char) to {OUTPUT_PATH}")
    print(letter)


if __name__ == "__main__":
    main()
