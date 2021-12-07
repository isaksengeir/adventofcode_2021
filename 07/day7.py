#! /usr/bin/env python3
import numpy as np


def part1(crab_pos):
    c = int(np.average(crab_pos) / 2)
    fuel_min = sum([abs(x - c) for x in crab_pos])
    fuel_increased = False
    while not fuel_increased:
        c += 1
        fuel_c = sum([abs(x - c) for x in crab_pos])
        if fuel_c <= fuel_min:
            fuel_min = fuel_c
        else:
            c -= 1
            fuel_increased = True
    return fuel_min


def part2(crab_pos):
    c = int(np.average(crab_pos) / 2)
    fuel_min = sum([(abs(x - c)*(abs(x - c)+1))/2 for x in crab_pos])
    fuel_increased = False
    while not fuel_increased:
        c += 1
        fuel_c = sum([(abs(x - c)*(abs(x - c)+1))/2 for x in crab_pos])
        if fuel_c <= fuel_min:
            fuel_min = fuel_c
        else:
            c -= 1
            fuel_increased = True
    return fuel_min


if __name__ == "__main__":
    crab_pos = np.loadtxt("data.txt", delimiter=",", dtype=int)

    print(part1(crab_pos))
    print(part2(crab_pos))