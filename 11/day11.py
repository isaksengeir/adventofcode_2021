#! /usr/bin/env python3
import numpy as np
global array
flash_count = 0


def nbrs(matrix, x, y, i, j):
    pos = matrix[i][j].copy()
    nb = list()
    for k in range(i-1, i+2):
        if 0 <= k <= y-1:
            for l in range(j-1, j+2):
                if 0 <= l <= x-1 and (k, l) != (i, j):
                    nb.append((k, l))
    return nb


def flash_your_neighbour(flashed, levelup):
    global flash_count
    new_flashers = list()
    for ij in levelup:
        if ij not in flashed:
            array[ij[0]][ij[1]] += 1
            if array[ij[0]][ij[1]] == 10:
                new_flashers.append(ij)

    return new_flashers


def make_flash(rows, columns):
    global flash_count
    flashed = list()
    rows = list(rows)
    columns = list(columns)
    local_count = 0
    while len(rows) > 0:
        i, j = rows.pop(0), columns.pop(0)
        array[i][j] = 0
        flash_count += 1
        flashed.append((i, j))
        nb = nbrs(array, y, x, i, j)
        local_count += 1
        new_flashes = flash_your_neighbour(flashed=flashed, levelup=nb)
        rows += [_[0] for _ in new_flashes]
        columns += [_[1] for _ in new_flashes]
        flashed += new_flashes
    return local_count


if __name__ == "__main__":
    array = np.genfromtxt("data.txt", delimiter=1, dtype=int)
    y, x = array.shape
    d = 0

    while True:
        d += 1
        array += 1
        r, c = np.where(array == 10)[0:2]
        lc = make_flash(r, c)
        if d == 100:
            print(f"part 1: {flash_count} flashes after {d} days")
        if lc == 100:
            break
    print(f"part 2: {d} days before all octopuses flash during same day!")
