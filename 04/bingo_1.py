#! /usr/bin/env python3
import numpy as np
from collections import Counter

future_draws = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,
         93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,
         38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]

drawed = list()
boards = list()
board = list()


def check_board(board, drawed):
    bingo = False
    rows, columns = board.copy(), np.transpose(board.copy())

    drawed = set(drawed)

    for i in range(len(rows)):
        if len(set(rows[i]).intersection(drawed)) == 5 or len(set(columns[i]).intersection(drawed)) == 5:
            bingo = True

    return bingo


def play_bingo(boards, future_numbers):
    winning_order = list()

    while len(boards) > 0:
        for i in future_numbers:
            drawed.append(i)

            to_remove = list()

            for j in range(len(boards)):
                board = boards[j]
                bingo = check_board(board, drawed)
                if bingo:
                    winning_order.append((board.copy(), drawed.copy()))
                    to_remove.append(j)

            boards = np.delete(boards, to_remove, 0)

    return winning_order


def score_winner_board(board, drawed):
    unmarked = list()
    for row in board:
        unmarked += list(set(row).difference(drawed))

    print(f"Final bingo number: {drawed[-1]}")
    print(f"Unmarked: {unmarked}")
    print(f"SCORE: {sum(unmarked) * drawed[-1]}")


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        for line in f:
            if len(line.split()) < 1:
                if len(board) != 0:
                    boards.append(board.copy())
                    board.clear()
                else:
                    pass
            else:
                board.append(list(map(int, line.split())))

    boards = np.array(boards)
    boards = np.delete(boards, [1,2,3], 0)
    winning_order = play_bingo(boards, future_draws)

    print("PART 1:")
    score_winner_board(winning_order[0][0], winning_order[0][1])

    print("PART 2:")
    score_winner_board(winning_order[-1][0], winning_order[-1][1])





