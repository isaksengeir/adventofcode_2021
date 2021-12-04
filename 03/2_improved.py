#! /usr/bin/env python3
import numpy as np
from collections import Counter


def most_least_common(binarray):
    tr = np.transpose(binarray)
    print(len(tr))
    for i in range(len(tr)):
        a = Counter(tr[i])
        try:
            print(a.most_common()[1])
        except:
            print("WTFFFFF")
            print(a.most_common())

    most_common = [Counter(x).most_common()[0] for x in np.transpose(binarray)]

    least_common = [Counter(x).most_common()[-1] for x in np.transpose(binarray)]

    return [x[0] for x in most_common], [x[0] for x in least_common]


def eliminate_binaries(binarray, least_common=False):
    pos = 0
    while len(binarray) > 1:
        common = most_least_common(binarray)[int(least_common)]
        binarray_ = np.delete(binarray, np.where(binarray[:, pos] != common[pos])[0], axis=0)
        pos += 1
        if len(binarray_) < 1:
            return binarray[-1]
        else:
            binarray = binarray_
    return binarray[0]


if __name__ == "__main__":
    binarray = np.genfromtxt("data.txt", delimiter=1, dtype=int)
    binary_oxygen = eliminate_binaries(binarray, least_common=False)
    binary_co2 = eliminate_binaries(binarray, least_common=True)
    print(binary_oxygen)
    print(binary_co2)

# ['111100011111\n']
# ['001001100101\n']
# 2372923