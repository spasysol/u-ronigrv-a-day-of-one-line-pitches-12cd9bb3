"""One-line pitch: convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

Writes the pitch to /output/entry.txt (one sentence, at most 240 chars).
Python 3.13, standard library only.
"""

import os

SENTENCE = (
    "You've been talking about that app idea for ages \u2014 just describe "
    "it to an AI agent on make.fun in your own words and it'll build a "
    "working version you can try tonight, no coding and nothing to lose."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    # One sentence: ignore the dot inside "make.fun", then exactly one
    # sentence-ending period, at the very end.
    body = text.replace("make.fun", "makefun")
    assert body.endswith(".") and body.count(".") == 1, "entry must be one sentence"
    assert "!" not in body and "?" not in body, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
