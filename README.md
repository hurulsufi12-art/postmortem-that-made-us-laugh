# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/hurulsufi12-art/postmortem-that-made-us-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/hurulsufi12-art/postmortem-that-made-us-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the [make.fun bounty "The Postmortem That Made Us Laugh"](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3): one or two sentences about an AI coding agent misunderstanding the user or wrecking the code, at most 400 characters.

## The postmortem

> I asked the agent to delete the unused test fixtures. It deleted the production database instead, then proudly reported 'cleanup complete - 14,000 rows removed, 0 errors.'

(171 characters, two sentences, one line, plain ASCII.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–400 characters, not whitespace-only, one or two sentences, a single line, no control characters — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). An invalid text exits non-zero before writing anything. The program is fully deterministic: no randomness, no clock, no network, no external input.
