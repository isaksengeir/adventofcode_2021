
dat = "../submarine_data.txt"

prev = None
incr = 0
mes = 0

with open(dat) as f:
    for line in f:
        mes += 1
        val = float(line.split()[0])

        if prev:
            print(val, prev)
            if val > prev:
                incr += 1
            prev = val
        else:
            prev = val

print(mes, incr)
