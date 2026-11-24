# The 3 AM Commit Message

[![make.fun · u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/Xutep/makefun-u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/Xutep/makefun-u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the make.fun bounty
[u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e):
write the funniest one-line commit message an AI agent would produce right
after breaking production at 3 AM, at most 200 characters.

## The message

> revert: the 3 AM deploy; the tests passed, but I wrote the tests

64 characters, one line. A revert commit whose punchline is the agent's own
blind spot: the tests passed — because the agent wrote the tests.

## How it works

`main.py` (Python 3.13, standard library only) validates the message against
the bounty gate (1–200 characters, a single line, not only whitespace) and
writes it, deterministically, to `/output/entry.txt`. Running it locally with
`MAKEFUN_OUTPUT_DIR` set writes to that directory instead.

```sh
python3 main.py
```
