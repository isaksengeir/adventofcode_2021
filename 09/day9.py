#! /usr/bin/env python3

import numpy as np
global basin_list


def nbrs(matrix, x, y, i, j):
    pos = matrix[i][j].copy()
    min = True
    for k in range(i-1, i+2):
        if 0 <= k <= y-1:
            for l in range(j-1, j+2):
                if 0 <= l <= x-1:
                    if (k, l) != (i, j) and (k == i or l == j):
                        if matrix[k][l] <= pos:
                            return False
    return min


def get_cross(matrix, x, y, i, j):
    nb = list()
    if i-1 >= 0:
        nb.append((i-1, j, matrix[i-1][j]))
    if i+1 <= y-1:
        nb.append((i+1, j, matrix[i+1][j]))
    if j-1 >= 0:
        nb.append((i, j-1, matrix[i][j-1]))
    if j+1 <= x-1:
        nb.append((i, j+1, matrix[i][j+1]))
    return nb


def filter_incr(val, flist):
    filtered = list()
    for i in flist:
        if i[-1] > val and i[-1] != 9:
            filtered.append(i)
    return filtered


def basins(matrix, x, y, i, j):
    current_value = matrix[i][j]
    basin = list()
    basin.append((i, j))
    nb = filter_incr(current_value, get_cross(matrix, x, y, i, j))

    while len(nb) > 0:
        i, j, tmp_val = nb[0][0], nb[0][1], nb[0][2]
        nb += filter_incr(tmp_val, get_cross(matrix, x, y, i, j))
        basin.append((i, j))
        nb.pop(0)

    return len(set(basin))


def find_minmas(matrix):
    y, x = matrix.shape
    mins = list()
    for i in range(y):
        for j in range(x):
            if nbrs(matrix, x, y, i, j):
                mins.append(matrix[i][j])
                basin_list.append(basins(matrix, x, y, i, j))
    return mins


def prod_basins():
    a = sorted(basin_list)
    return a[-1]*a[-2]*a[-3]


if __name__ == "__main__":
    basin_list = list()
    heatmap = np.genfromtxt("data.txt", delimiter=1, dtype=int)
    mins = find_minmas(heatmap)
    print(f"PART 1: {sum([x+1 for x in mins])}")
    print(f"PART 2: {prod_basins()}")




