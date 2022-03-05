import itertools

with open("dec14/input.txt") as file:
    lines = file.read().splitlines()

def vary_x(string):
    combos = itertools.product([True, False], repeat=string.count("X"))
    indices = [i for i in range(36) if string[i] == "X"]

    result = []
    for combo in combos:
        arr = list(string)
        for i, pos in enumerate(indices):
            if combo[i]: arr[pos] = "1"
            else: arr[pos] = "0"
        result.append(int("".join(arr), 2))
    return result

memory = {}
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        index = int(line[4:line.index("]")])
        value = int(line.split(" = ")[-1])
        binaryindex = bin(index)[2:].zfill(36)
        bi2 = "".join(mask[i] if mask[i] != "0" else binaryindex[i] for i in range(36))
        for index in vary_x(bi2):
            memory[index] = value
        # memory[index] = value * 2**(bi2.count("X"))
        

print(sum(memory.values()))