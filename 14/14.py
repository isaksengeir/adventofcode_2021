#! /usr/bin/env python3
from collections import defaultdict
from copy import deepcopy


def read_input(inp):
    rules = defaultdict()
    seed = None
    with open(inp, "r") as f:
        for line in f:
            if "->" not in line and len(line) > 2:
                seed = list(line.strip("\n"))
            elif "->" in line:
                rules[line.split("->")[0].strip()] = line.split("->")[1].strip("\n").strip()
    return rules, seed


def grow_n_steps2(seed, rules,n):
    letter_counter = defaultdict(lambda: 0)
    poly_pairs = defaultdict(lambda: 0)
    for i in range(len(seed)):
        a = seed[i]
        letter_counter[a] += 1
        if i < (len(seed) - 1) :
            b = seed[i + 1]
            poly_pairs[f"{a}{b}"] += 1

    for i in range(n):
        old_poly = deepcopy(poly_pairs)
        for pair in old_poly.keys():
            p1, p2 = f"{pair[0]}{rules[pair]}", f"{rules[pair]}{pair[1]}"
            letter_counter[rules[pair]] += old_poly[pair]
            poly_pairs[p1] += old_poly[pair]
            poly_pairs[p2] += old_poly[pair]
            poly_pairs[pair] -= old_poly[pair]
    return max(letter_counter.values()) - min(letter_counter.values())


if __name__ == "__main__":
    rules, seed = read_input("data.txt")
    print(f"PART 1: {grow_n_steps2(seed=seed, rules=rules, n=10)}")
    print(f"PART 1: {grow_n_steps2(seed=seed, rules=rules, n=40)}")
