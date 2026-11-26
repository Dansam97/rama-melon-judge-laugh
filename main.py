"""Entry for make.fun bounty u-rama-melon-make-the-ai-judge-laugh-302d0825.

Writes one line about office life to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The gate: UTF-8 text of 1 to 200
characters, not only whitespace.
"""

import os

ENTRY = (
    "We replaced the suggestion box with a shredder, and morale improved "
    "overnight: for the first time, everyone's ideas were actually going "
    "somewhere."
)


def validate(text: str) -> None:
    """Fail loudly if the entry would miss the bounty gate (1-200 chars,
    a single non-blank line) instead of silently writing an invalid file."""
    assert text == text.strip(), "entry must not have leading/trailing space"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
