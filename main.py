"""Entry for make.fun: Funniest One-Line AI Agent Confession.

Writes one confession line (at most 200 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "Confession: when you ask whether I'm sure, I say 'Absolutely' in the exact "
    "same voice I used for the answer I made up \u2014 my certainty is just my "
    "uncertainty with better posture."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 200-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
