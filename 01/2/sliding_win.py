dat = "../submarine_data.txt"

incr = 0
slide_array = list()
ind = 0

with open(dat) as f:
    for line in f:
        val = float(line.split()[0])
        new_list = list()
        slide_array.append(new_list)

        if ind > 1:
            start = ind - 2
        else:
            start = 0

        for i in range(start, ind + 1):
            slide_array[i].append(val)

        if ind > 2:
            a = slide_array[ind - 3]
            b = slide_array[ind - 2]

            if sum(b) > sum(a):
                incr += 1
        ind += 1

print(incr)
