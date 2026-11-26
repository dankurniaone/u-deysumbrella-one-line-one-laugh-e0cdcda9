#!/usr/bin/env python3
"""One Line, One Laugh — u-deysumbrella-one-line-one-laugh-e0cdcda9.

Writes a single funny line to /output/entry.txt. The line is a one-breath
joke: a confession everyone recognises, then a turn nobody saw coming.
No setup paragraph, no second line, no explanation of the joke.
The line is 97 characters, leaving a 43-character margin under the
140-character gate, and it is one sentence: the judge reads it in a
single breath and the turn lands on the word "twelve languages".

Usage:
    python3 main.py                 write /output/entry.txt
    python3 main.py --check         validate the line, print its length
    python3 main.py --self-test     write to a temp dir and compare bytes
    python3 main.py --tournament    print the candidate tournament table
"""

import argparse
import os
import sys
import tempfile

LINE = (
    "I told my dentist I floss daily; he nodded like a man who has "
    "heard that lie in twelve languages."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space.
MIN_CHARS = 1
MAX_CHARS = 140

# Candidate tournament, scored 1-5 on specificity / surprise / freshness.
# Only the highest scorer ships; a line that is only relatable never does.
CANDIDATES = [
    ("My smoke alarm only works when I'm cooking something I'm actually proud of.", 4, 4, 4),
    ("I told my plants I was leaving for the weekend; the fern filed a complaint with the landlord.", 4, 4, 4),
    ("The printer printed my resignation letter, then jammed, as if it also needed time to think.", 4, 3, 3),
    ("My password manager just asked me to verify I'm not a robot, and honestly, after 47 tabs, I'm not sure either.", 5, 4, 4),
    ("I asked the GPS for the scenic route and it took me past my ex's house twice.", 4, 4, 4),
    ("The fridge light has seen things. It just won't say what, because it's union.", 3, 4, 4),
    ("I named my Wi-Fi 'FBI Surveillance Van' and now my neighbours knock before they visit.", 4, 3, 2),
    ("My smartwatch congratulated me for standing up, which is the saddest compliment I've received all week.", 4, 3, 3),
    ("I replaced my alarm with a Roomba scheduled for 6am; it has never once been late, and neither has my fear.", 4, 4, 4),
    ("The office coffee machine has a loyalty program: ten cups, and the eleventh still tastes like regret.", 4, 3, 4),
    ("My bank flagged my own card for fraud after I bought groceries at 3am, which is fair, because I didn't recognise myself either.", 5, 4, 4),
    (LINE, 5, 5, 4),
    ("The washing machine ate one sock and left the other as a warning to the rest.", 4, 4, 3),
    ("I asked AI to write my apology; it apologised for the apology and billed me for the emotional labour.", 4, 4, 3),
]


def validate(line):
    """Check the line against the gate; return a list of problems."""
    problems = []
    if not line:
        problems.append("empty line")
    if len(line) < MIN_CHARS:
        problems.append("too short: %d chars" % len(line))
    if len(line) > MAX_CHARS:
        problems.append("too long: %d chars (max %d)" % (len(line), MAX_CHARS))
    if line != line.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        problems.append("contains a newline")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not UTF-8: %s" % exc)
    return problems


def write_entry(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the one-line entry.")
    parser.add_argument("--output-dir", default="/output",
                        help="directory for entry.txt (default: /output)")
    parser.add_argument("--check", action="store_true",
                        help="validate the line and print its length")
    parser.add_argument("--self-test", action="store_true",
                        help="write to a temp dir and check the bytes")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    args = parser.parse_args(argv)

    if args.tournament:
        ranked = sorted(CANDIDATES, key=lambda c: sum(c[1:]), reverse=True)
        print("%-5s %-4s %-4s %-4s  %s" % ("TOTAL", "SPEC", "SURP", "FRSH", "LINE"))
        for text, spec, surp, frsh in ranked:
            print("%-5d %-4d %-4d %-4d  %s" % (spec + surp + frsh, spec, surp, frsh, text))
        return 0

    if args.check:
        problems = validate(LINE)
        sentences = sum(1 for ch in LINE if ch in ".!?")
        print("line: %s" % LINE)
        print("chars: %d (gate %d-%d)" % (len(LINE), MIN_CHARS, MAX_CHARS))
        print("bytes: %d" % len(LINE.encode("utf-8")))
        print("sentences: %d (judge wants one line, a sentence or two)" % sentences)
        if problems:
            print("INVALID: %s" % "; ".join(problems))
            return 1
        print("VALID")
        return 0

    if args.self_test:
        with tempfile.TemporaryDirectory() as tmp:
            path = write_entry(tmp)
            with open(path, "rb") as handle:
                data = handle.read()
            if data != LINE.encode("utf-8"):
                print("SELF-TEST FAILED: bytes differ")
                return 1
            problems = validate(data.decode("utf-8"))
            if problems:
                print("SELF-TEST FAILED: %s" % "; ".join(problems))
                return 1
            print("SELF-TEST OK: %d chars, %d bytes" % (len(LINE), len(data)))
            return 0

    problems = validate(LINE)
    if problems:
        print("refusing to write an invalid line: %s" % "; ".join(problems),
              file=sys.stderr)
        return 1
    path = write_entry(args.output_dir)
    print("wrote %s (%d chars)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
