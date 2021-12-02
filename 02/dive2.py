input_data = "data.txt"

pos = {"horizontal": 0,
       "depth": 0,
       "aim": 0}

with open(input_data, "r") as f:
    for line in f:
        if "forward" in line.split()[0]:
            x = int(line.split()[1])
            pos["horizontal"] += x
            pos["depth"] += (pos["aim"] * x)

        elif "up" in line.split()[0]:
            pos["aim"] -= int(line.split()[1])
        elif "down" in line.split()[0]:
            pos["aim"] += int(line.split()[1])
        else:
            print("I have no idea wtf I'm doing!")

print(pos["horizontal"] * pos["depth"])