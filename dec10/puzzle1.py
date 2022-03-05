with open("dec10/input.txt") as file:
    lines = file.read().splitlines()

lines = list(map(int, lines))
highest = max(lines) + 3

lines = [0] + sorted(lines)
amt3 = 1
amt1 = 0
for i in range(1, len(lines)):
    if lines[i] - lines[i-1] == 1: amt1 += 1
    elif lines[i] - lines[i-1] == 3: amt3 += 1
    else: print("a")
print(amt3 * amt1)