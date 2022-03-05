def part1():
    with open("dec3/input.txt") as file:
        lines = [f.strip() for f in file.readlines()]
    w = len(lines[0])
    h = len(lines)
    return sum(1 for y in range(h) if lines[y][(3*y) % w] == "#")