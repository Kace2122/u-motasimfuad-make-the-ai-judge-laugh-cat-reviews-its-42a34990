#!/usr/bin/env python3
"""Cat Reviews Its Human entry: writes one deadpan one-star review to /output/entry.txt."""

import os

REVIEW = "One star. The human moved my favourite sunbeam, served dinner three minutes late, and then expected purring. I knocked a glass off the table in protest."

# Self-check: the entry must stay one line of at most 200 characters, with no
# leading or trailing whitespace padding the review.
assert "\n" not in REVIEW and 1 <= len(REVIEW) < 200
assert REVIEW == REVIEW.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == REVIEW

if __name__ == "__main__":
    main()
