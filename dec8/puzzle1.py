def part1():
    with open("dec8/input.txt") as file:
        lines = file.read().strip().split("\n")
    lines = [tuple(line.split(" ", 1)) for line in lines]
    acc = 0
    pointer = 0
    already_run = set()
    while pointer not in already_run:
        already_run.add(pointer)
        arg, offset = lines[pointer]
        offset = int(offset)
        if arg == "acc": acc += offset
        elif arg == "jmp": pointer += offset - 1
        pointer += 1
    return acc