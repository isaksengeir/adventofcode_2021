#! /usr/bin/env python3
import numpy as np
from collections import Counter

if __name__ == "__main__":
    binarray = np.genfromtxt("data.txt", delimiter=1, dtype=int)
    most_common = map(str, [Counter(x).most_common()[0][0] for x in np.transpose(binarray)])
    least_common = map(str, [Counter(x).most_common()[-1][0] for x in np.transpose(binarray)])
    print(int(''.join(most_common), 2) * int(''.join(least_common), 2))