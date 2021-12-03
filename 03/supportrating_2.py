#! /usr/bin/env python3

def count_bins(binary_data):
    bin_counter = list()
    for line in binary_data:
        binlist = list(line.strip("\n"))
        while len(bin_counter) != len(binlist):
            bin_counter.append({"0": 0, "1": 0})
        for i in range(len(binlist)):
            bin_counter[i][binlist[i]] += 1
    return bin_counter


def translate_bin_counter(bin_counter):
    most_common = ""
    less_common = ""
    for counter in bin_counter:
        if counter["0"] > counter["1"]:
            most_common += "0"
            less_common += "1"
        elif counter["0"] <= counter["1"]:
            most_common += "1"
            less_common += "0"
    return most_common, less_common


def filter_bin_pos(binary, position, binarylist):
    new_list = list()
    keeper = binary[position]
    for bin in binarylist:
        if keeper == bin[position]:
            new_list.append(bin)
    return new_list


def eliminate_binaries(binary_list, least_common=False):
    pos = 0
    while len(binary_list) > 1:
        bin_counter = count_bins(binary_list)
        common = translate_bin_counter(bin_counter)[int(least_common)]
        binary_list = filter_bin_pos(common, pos, binary_list)
        pos += 1
    return binary_list


input_data = "data.txt"
binary_list = open(input_data, "r").readlines()

binary_oxygen = eliminate_binaries(binary_list, least_common=False)
binary_co2 = eliminate_binaries(binary_list, least_common=True)

print(int(binary_oxygen[0], 2) * int(binary_co2[0], 2))
