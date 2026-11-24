"""One-Liner Laugh Lab — slot 1.

Writes one short funny line (the excuse a robot vacuum gives after
eating a sock) to /output/entry.txt. Deterministic, no network, no I/O
beyond the single output file.
"""

import os

# Angle: deadpan therapy-confession twist. Field scan (588 entries) shows
# the saturated angles are "job description: eat everything on the floor",
# legal defense, "it attacked first", firmware-update excuses and
# "the sock consented". The therapist / swallowed-feelings turn is fresh,
# fits the excuse prompt, and lands in two short beats.
ENTRY = (
    "My therapist says I swallow my feelings. "
    "Your sock was just standing there, being a feeling."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
