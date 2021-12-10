#! /usr/bin/env python3
import numpy as np
global syntax_points
global open_close
global complete_points
global score_incomplete
global score_corrupt


def complete_syntax(openings):
    score = 0
    for i in reversed(openings):
        score *= 5
        score += complete_points[open_close[i]]
    score_incomplete.append(score)


def check_syntax(line):
    openings = list()
    for i in line:
        if i in open_close.keys():
            openings.append(i)
        elif len(openings) > 0 and i == open_close[openings[-1]]:
            del openings[-1]
        else:
            score_corrupt.append(syntax_points[i])
            return
    complete_syntax(openings)


if __name__ == "__main__":
    syntax_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    complete_points = {")": 1, "]": 2, "}": 3, ">": 4}
    open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score_incomplete = list()
    score_corrupt = list()

    with open("data.txt") as f:
        for line in f:
            check_syntax(line.strip("\n"))
    print(f"PART 1: Corrupted syntax points: {sum(score_corrupt)}")
    print(f"PART 2: Incomplete syntax points: {np.median(score_incomplete)}")
