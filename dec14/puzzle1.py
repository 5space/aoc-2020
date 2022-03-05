with open("dec14/input.txt") as file:
    lines = file.read().splitlines()

memory = {}
for line in lines:
    if line.startswith("mask = "):
        mask = line[7:]
    else:
        index = int(line[4:line.index("]")])
        value = int(line.split(" = ")[-1])
        binaryval = bin(value)[2:].zfill(36)
        bv2 = "".join(mask[i] if mask[i] != "X" else binaryval[i] for i in range(36))
        v2 = int(bv2, 2)
        memory[index] = v2

print(sum(memory.values()))