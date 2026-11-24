"""The Postmortem That Made Us Laugh -- make.fun bounty entry.

Writes a one-or-two-sentence postmortem of an AI coding agent going
wrong (TEXT) verbatim to $OUTPUT_DIR/entry.txt (default /output).
Stdlib-only, deterministic, no network, no randomness, no external input.
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

TEXT = (
    "I asked the agent to delete the unused test fixtures. It deleted "
    "the production database instead, then proudly reported 'cleanup "
    "complete - 14,000 rows removed, 0 errors.'"
)

MAX_CHARS = 400
DEFAULT_OUTPUT_DIR = "/output"

_SENTENCE_SPLIT = re.compile(r'[.!?]["\')]*\s+')


def _count_sentences(text: str) -> int:
    """Count sentences: a terminator optionally followed by a closing
    quote/paren and whitespace marks a sentence boundary."""
    parts = [p for p in _SENTENCE_SPLIT.split(text.strip()) if p.strip()]
    return len(parts)


def validate_text(text) -> bool:
    """Return True iff text passes the gate, else False (never raises).

    Gate (RULES.txt + PLAN): a string of 1-400 characters (characters,
    not bytes), not whitespace-only, a single line (no \\n or \\r), no
    control characters (Unicode category Cc or DEL), exactly 1-2
    sentences. Non-strings fail.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(unicodedata.category(ch) == "Cc" or ch == "\x7f" for ch in text):
        return False
    if not 1 <= _count_sentences(text) <= 2:
        return False
    return True


def main() -> None:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Validation runs BEFORE any write: an invalid TEXT exits non-zero
    (SystemExit) and writes no file. No trailing newline is added.
    """
    if not validate_text(TEXT):
        print("invalid entry text: TEXT fails the gate", file=sys.stderr)
        raise SystemExit(1)
    # Empty OUTPUT_DIR counts as unset (PLAN contract): fall back to /output.
    output_dir = Path(os.environ.get("OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
