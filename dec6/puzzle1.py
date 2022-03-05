def part1():
    with open("dec6/input.txt") as file:
        lines = file.read().strip().split("\n\n")
    return sum(len(set(L.replace("\n", ""))) for L in lines)