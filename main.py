"""The 3 AM Commit Message -- make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. Standard library only.

The message is an AI agent's commit right after breaking production at
3 AM: a revert whose punchline is the agent's own blind spot -- the tests
passed, but the agent wrote the tests.
"""

import os
import sys

MESSAGE = "revert: the 3 AM deploy; the tests passed, but I wrote the tests"

MAX_CHARS = 200


def validate(message: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one line, not only whitespace."""
    if not message or not message.strip():
        raise ValueError("message must not be blank")
    if "\n" in message or "\r" in message:
        raise ValueError("message must be a single line")
    if len(message) > MAX_CHARS:
        raise ValueError(
            "message is %d chars, over the %d cap" % (len(message), MAX_CHARS)
        )
    if message != message.strip():
        raise ValueError("message must not have leading or trailing whitespace")


def main() -> int:
    validate(MESSAGE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(MESSAGE)
    with open(path, "r", encoding="utf-8", newline="\n") as fh:
        written = fh.read()
    if written != MESSAGE:
        raise ValueError("wrote %r, expected %r" % (written, MESSAGE))
    print("wrote %d chars to %s" % (len(MESSAGE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
