def part2():
    with open("dec6/input.txt") as file:
        lines = file.read().strip().split("\n\n")
    c = 0
    for line in lines:
        line2 = line.replace("\n", "")
        letters = set(list(line2))
        indivs = line.split("\n")
        for letter in letters:
            if all(letter in ind for ind in indivs):
                c += 1
    return c