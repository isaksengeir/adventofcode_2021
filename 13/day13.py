#! /usr/bin/env python3
import numpy as np
from collections import defaultdict


def fold_along(axis, paper):
    transpose = False
    paper = paper
    ind = int(axis.split("=")[-1])
    if "x" in axis:
        transpose = True
        paper = np.transpose(paper)

    paper2 = fold_y(ind, paper)

    if transpose:
        paper2 = np.transpose(paper2)
    return paper2


def fold_y(ind, paper):
    new_y = ind
    if (len(paper) - ind) > ind:
        new_y = len(paper) - ind - 1
    new_paper = np.zeros((new_y, len(paper[0])), dtype=int)

    up = ind + 1
    down = ind - 1
    new = -1
    while down >= 0 or up <= len(paper):
        if down >= 0:
            new_paper[new] += paper[down]
        if up < len(paper):
            new_paper[new] += paper[up]
        else:
            break
        new -= 1
        down -= 1
        up += 1

    return new_paper


def make_array(coordinates, x, y):
    dots = np.zeros((y+1, x+1), dtype=int)
    for y in coordinates.keys():
        for x in coordinates[y]:
            dots[y][x] = 1
    return dots


if __name__ == "__main__":
    no_zeros = set()
    coordinates = defaultdict(lambda: set())
    fold = list()
    x_max = 0
    y_max = 0
    with open("data.txt", "r") as f:
        for line in f:
            if len(line.split(",")) == 2:
                x, y = map(int, line.split(",")[0:2])
                if x > x_max:
                    x_max = x
                if y > y_max:
                    y_max = y
                coordinates[y].add(x)
            elif "fold" in line:
                fold.append(line.split()[-1].strip("\n"))

    paper = make_array(coordinates, x_max, y_max)

    print(f"PART 1: {np.count_nonzero(fold_along(fold[0], paper))}")
    print("PART 2:")
    for i in fold:
        paper = fold_along(i, paper)

    for y in range(0, len(paper)):
        for x in range(0, len(paper[y])):
            if paper[y][x] != 0:
                print("#", end="")
            else:
                print(".", end="")
        print("")



