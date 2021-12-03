#! /usr/bin/env python3

def translate_bin_counter(bin_counter):
    most_common = ""
    less_common = ""

    for counter in bin_counter:
        if counter["0"] > counter["1"]:
            most_common += "0"
            less_common += "1"
        else:
            most_common += "1"
            less_common += "0"
    return most_common, less_common


input_data = "data.txt"
bin_counter = list()

with open(input_data, "r") as f:
    for line in f:
        binlist = list(line.strip("\n"))
        while len(bin_counter) != len(binlist):
            bin_counter.append({"0": 0, "1": 0})
        for i in range(len(binlist)):
            bin_counter[i][binlist[i]] += 1

gamma, epsilon = translate_bin_counter(bin_counter)
print(int(gamma, 2) * int(epsilon, 2))