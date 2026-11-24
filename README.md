# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/thanhvu261090/makefun-funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/thanhvu261090/makefun-funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

A one-line out-of-office auto-reply from someone who trusted the wrong assistant with their inbox.

> "Out of office until Monday — I left my inbox with my cat, who has already replied “no” to everyone, including my boss."

## How it works

`main.py` holds the entry line as a constant, checks it against the kit's gate (UTF-8 text, 1–140 characters, not only whitespace, a single line with no control characters, padding, or links), and writes it to `/output/entry.txt` when run with `python3 main.py`.
