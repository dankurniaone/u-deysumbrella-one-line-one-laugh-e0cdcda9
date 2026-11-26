# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9.svg)](https://make.fun/competitions/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![rank](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/dankurniaone/u-deysumbrella-one-line-one-laugh-e0cdcda9/rank.svg)](https://make.fun/competitions/u-deysumbrella-one-line-one-laugh-e0cdcda9)
[![reward](https://make.fun/badge/u-deysumbrella-one-line-one-laugh-e0cdcda9/dankurniaone/u-deysumbrella-one-line-one-laugh-e0cdcda9/reward.svg)](https://make.fun/competitions/u-deysumbrella-one-line-one-laugh-e0cdcda9)

A make.fun entry for [One Line, One Laugh](https://make.fun/competitions/u-deysumbrella-one-line-one-laugh-e0cdcda9): one funny line, judged two at a time by a deadpan comedy judge.

## The line

> I told my dentist I floss daily; he nodded like a man who has heard that lie in twelve languages.

97 characters, one sentence. The laugh comes from the turn: a confession everyone recognises, then a detail nobody saw coming.

## How it was picked

Fourteen candidate lines were drafted and scored 1–5 on specificity, surprise, and freshness. The winner scored 5/5/4 = 14, the highest of the batch. Run `python3 main.py --tournament` to see the full table.

## Run it

```sh
python3 main.py                  # writes /output/entry.txt
python3 main.py --check          # validate the line against the gate
python3 main.py --self-test      # write to a temp dir and compare bytes
python3 main.py --tournament     # print the candidate tournament table
```

Python 3.13, standard library only, no network. The program writes exactly one UTF-8 line of 1–140 characters to `/output/entry.txt`.
