def part1():
    with open("dec2/input.txt") as file:
        inputs = file.readlines()
    c = 0
    for i in inputs:
        bounds, letter, password = i.split(" ")
        xmin, xmax = bounds.split("-")
        if int(xmin) <= password.count(letter[0]) <= int(xmax): c += 1
    return c