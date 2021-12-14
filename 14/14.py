#! /usr/bin/env python3
import numpy as np
from collections import defaultdict

def read_input(inp):
    rules = defaultdict()
    seed = None
    with open(inp, "r") as f:
        for line in f:
            if "->" not in line and len(line) > 2:
                seed = list(line.strip("\n"))
            elif "->" in line:
                rules[line.split("->")[0]] = ...


if __name__ == "__main__":
    pass