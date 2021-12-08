#! /usr/bin/env python3
import numpy as np


def part1_fuel(c, pos):
    return sum([abs(x - c) for x in pos])


def part2_fuel(c, pos):
    return sum([(abs(x - c) * (abs(x - c) + 1)) / 2 for x in pos])


def calc_fuel(part1=True):
    c = int(np.average(crab_pos) / 2)
    print(np.median(crab_pos))
    print(c)
    if part1:
        fuel_min = part1_fuel(c, crab_pos)
    else:
        fuel_min = part2_fuel(c, crab_pos)
    fuel_increased = False
    while not fuel_increased:
        c += 1
        if part1:
            fuel_c = part1_fuel(c, crab_pos)
        else:
            fuel_c = part2_fuel(c, crab_pos)
        if fuel_c <= fuel_min:
            fuel_min = fuel_c
        else:
            c -= 1
            fuel_increased = True
    print(c)
    return fuel_min


if __name__ == "__main__":
    crab_pos = np.loadtxt("data.txt", delimiter=",", dtype=int)
    print(f"PART 1: {calc_fuel()} ")
    print(f"PART 2: {calc_fuel(part1=False)} ")