#! /usr/bin/env python3
from collections import defaultdict
global connections


def add_connctions(line):
    c1, c2 = line.split("-")
    connections[c1].append(c2.strip("\n"))
    connections[c2.strip("\n")].append(c1)


def path_finder(visit_twice=False):
    paths = set()
    tmp_paths = [[visit_twice, 'start', a] for a in connections['start']]
    while tmp_paths:
        e = tmp_paths.pop()
        next = [e + [a] for a in connections[e[-1]]]
        for cave in next:
            if cave[-1] == 'end':
                paths.add(tuple(cave[1:]))
            elif cave[-1] == 'start':
                pass
            elif cave[-1].isupper():
                tmp_paths.append(cave)
            elif cave.count(cave[-1]) == 1:
                tmp_paths.append(cave)
            elif cave.count(cave[-1]) == 2 and cave[0]:
                tmp_paths.append([False] + cave[1:])
    return len(paths)


if __name__ == "__main__":
    connections = defaultdict(lambda: list())
    with open("data.txt") as f:
        for line in f:
            add_connctions(line)
    print(f"Part 1: {path_finder(visit_twice=False)}")
    print(f"Part 2: {path_finder(visit_twice=True)}")