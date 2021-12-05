#! /usr/bin/env python3
from collections import Counter
import itertools


def add_coordinates(x1, y1, x2, y2, diagonals=False):
    if not diagonals and x1 != x2 and y2 != y1:
        return

    if x1 == x2 or y1 == y2:
        for x, y in itertools.product(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)):
            count.update([(x, y)])
    if diagonals and abs(x2 - x1) == abs(y2 - y1):
        dx = 1 if x2 > x1 else -1
        dy = 1 if y2 > y1 else -1
        count.update([(x1 + i * dx, y1 + i * dy) for i in range(abs(x2 - x1) + 1)])


if __name__ == "__main__":
    count = Counter([])
    with open("data.txt") as f:
        for line in f:
            x1, y1, x2, y2 = list(map(int, (line.replace('->', ',')).split(",")))[:]
            add_coordinates(x1, y1, x2, y2, diagonals=True)

    count = {key: val for key, val in count.items() if val >= 2}
    print(len(count))


