def part1():
    with open("dec1/input.txt") as file:
        numbers = list(map(int, file.readlines()))
    for n in numbers:
        if 2020-n in numbers:
            return n * (2020-n)