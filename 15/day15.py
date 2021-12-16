#! /usr/bin/env python3
import numpy as np


def minimise_risk(matrix):
    y, x = matrix.shape
    min_cost = np.zeros((y, x), dtype=int)

    for i in range(y):
        for j in range(x):
            if i == 0 and j == 0:
                min_cost[i][j] = 0
            else:
                min_cost[i][j] = matrix[i][j]
            if i == 0 and j > 0:
                min_cost[0][j] += min_cost[0][j - 1]
            elif j == 0 and i > 0:
                min_cost[i][0] += min_cost[i - 1][0]
            elif i > 0 and j > 0:
                min_cost[i][j] += min(min_cost[i - 1][j], min_cost[i][j - 1])
    return min_cost[y - 1][x - 1]


def make_n_n(matrix, n=5):
    arrays = list()
    new_matrix = None
    for ni in range(n):
        if ni == 0:
            arrays.append(matrix)
        else:
            del arrays[1:]
            arrays[0] += 1
            arrays[0][arrays[0] > 9] = 1
        for nj in range(1, n):
            if ni == 0 and nj == 0:
                pass
            else:
                new_arr = arrays[-1].copy() + 1
                new_arr[new_arr >= 10] = 1
                arrays.append(new_arr)

        if ni == 0:
            new_matrix = np.concatenate(arrays, axis=1)
        else:
            tmp_matrix = np.concatenate(arrays, axis=1)
            new_matrix = np.concatenate((new_matrix, tmp_matrix), axis=0)

    return new_matrix


if __name__ == "__main__":
    cavern = np.genfromtxt("data.txt", delimiter=1, dtype=int)
    print(f"PART 1: {minimise_risk(cavern)}")
    bigger = make_n_n(cavern, n=5)
    print(f"PART 2: {minimise_risk(bigger)}")
    # Returns 2789 - which is not right!!?? wtf
    # The right answer is 2778 (checked with code from bast).
