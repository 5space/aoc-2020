def part2():
    with open("dec3/input.txt") as file:
        lines = [f.strip() for f in file.readlines()]
    w = len(lines[0])
    h = len(lines)
    def amt(dx, dy):
        return sum(1 for c in range(h//dy) if lines[dy*c][(dx*c) % w] == "#")
    return amt(1, 1) * amt(3, 1) * amt(5, 1) * amt(7, 1) * amt(1, 2)