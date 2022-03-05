def part2():
    with open("dec2/input.txt") as file:
        inputs = file.readlines()
    c = 0
    for i in inputs:
        bounds, letter, password = i.strip().split(" ")
        xmin, xmax = bounds.split("-")
        xmin, xmax = int(xmin), int(xmax)
        if (password[xmin-1] == letter[0]) ^ (password[xmax-1] == letter[0]): c += 1
    return c