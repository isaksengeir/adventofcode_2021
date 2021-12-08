#! /usr/bin/env python3
import numpy as np
from collections import defaultdict

# abcdefg
# Unique
# 1: 2 digits (0010010) cf
# 7: 3 digits (1010010) acf
# 4: 4 digits (0111010) bcdf
# 8: 7 digits (1111111) abcdefg

# 0: 6 digits (1110111) abcefg
# 6: 6 digits (1101111) abdefg
# 9: 6 ditits (1111011) abcdfg

# 2: 5 digits (1101011) acdeg
# 3: 5 digits (1011011) acdfg
# 5: 5 digits (1011011) abdfg

global unique_counter
global unique_translator
global code_sum


def find_index(plist, p):
    p = sorted(p)
    for i in range(len(plist)):
        if p == sorted(plist[i]):
            return i
    return False


def decode_mess(pattern, output):
    seq_nr = defaultdict()
    nr_seq = defaultdict()
    to_decode = defaultdict(lambda: list())

    # 1 7 4 8
    for c in pattern.split():
        if len(c) in unique_translator.keys():

            seq_nr[''.join(sorted(c))] = unique_translator[len(c)]
            nr_seq[unique_translator[len(c)]] = ''.join(sorted(c))

        else:
            to_decode[len(c)].append("".join(sorted(c)))


    # 3
    for j in range(len(to_decode[5])):
        if len(set(nr_seq[7]) & set(to_decode[5][j])) == 3:
            nr_seq[3] = "".join(sorted(to_decode[5][j]))
            seq_nr["".join(sorted(to_decode[5][j]))] = 3
    del to_decode[5][find_index(to_decode[5], nr_seq[3])]

    # 9
    nr_seq[9] = "".join(sorted(set(nr_seq[3]) | set(nr_seq[4])))
    seq_nr["".join(sorted(set(nr_seq[3]) | set(nr_seq[4])))] = 9
    del to_decode[6][find_index(to_decode[6], nr_seq[9])]

    # 6 and 0 -> compare with 7
    print(set(nr_seq[7]) & set(to_decode[6][1]))

    if len(set(nr_seq[7]) & set(to_decode[6][0])) == 3:
        nr_seq[0] = "".join(sorted(to_decode[6][0]))
        nr_seq[6] = "".join(sorted(to_decode[6][1]))
        seq_nr["".join(sorted(to_decode[6][0]))] = 0
        seq_nr["".join(sorted(to_decode[6][1]))] = 6

    else:
        nr_seq[0] = "".join(sorted(to_decode[6][1]))
        nr_seq[6] = "".join(sorted(to_decode[6][0]))
        seq_nr["".join(sorted(to_decode[6][1]))] = 0
        seq_nr["".join(sorted(to_decode[6][0]))] = 6

    # 2 and 5 --> compare to 4
    if len(set(nr_seq[4]) & set(to_decode[5][0])) == 3:
        nr_seq[5] = "".join(sorted(to_decode[5][0]))
        nr_seq[2] = "".join(sorted(to_decode[5][1]))
        seq_nr["".join(sorted(to_decode[5][0]))] = 5
        seq_nr["".join(sorted(to_decode[5][1]))] = 2
    else:
        nr_seq[5] = "".join(sorted(to_decode[5][1]))
        nr_seq[2] = "".join(sorted(to_decode[5][0]))
        seq_nr["".join(sorted(to_decode[5][1]))] = 5
        seq_nr["".join(sorted(to_decode[5][0]))] = 2

    code = ""
    for p in output.split():
        p = "".join(sorted(p))
        if int(len(p)) in [2, 3, 4, 7]:
            unique_counter[len(p)] += 1
        code += str(seq_nr[p])
    return int(code)


if __name__ == "__main__":
    unique_counter = defaultdict(lambda: 0)
    unique_translator = {2: 1, 3: 7, 4: 4, 7: 8}
    code_sum = 0
    with open("data.txt") as n:
        for line in n:
            code_sum += decode_mess(line.split('|')[0], line.split('|')[1])

    print(f"PART 1: {sum([x for x in unique_counter.values()])}")
    print(f"PART 2: {code_sum}")