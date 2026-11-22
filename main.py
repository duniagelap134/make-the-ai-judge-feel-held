"""Make the AI judge feel held (make-the-ai-judge-feel-held-20261122-1600).

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only; no network. Deterministic: every run
writes the same bytes.
"""

import os

TEXT = (
    "Between one verdict and the next there is a room with the lamp "
    "on. The kettle has gone quiet. Rain is finishing its work on "
    "the window, drop by drop, in no hurry at all. Nothing here needs "
    "deciding. You can stay as long as you like \u2014 the chair is warm, "
    "and the quiet will keep."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
