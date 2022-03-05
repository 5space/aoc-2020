def part2():
    with open("dec8/input.txt") as file:
        lines = file.read().strip().split("\n")
    lines = [tuple(line.split(" ", 1)) for line in lines]
    def test(lines):
        acc = 0
        pointer = 0
        already_run = set()
        terminated = False
        while pointer not in already_run:
            if pointer >= len(lines):
                terminated = True
                break
            already_run.add(pointer)
            arg, offset = lines[pointer]
            offset = int(offset)
            if arg == "acc": acc += offset
            elif arg == "jmp": pointer += offset - 1
            pointer += 1
        return (terminated, acc)
    for i in range(len(lines)):
        lines2 = lines[:]
        if lines2[i][0] == "nop":
            lines2[i] = ("jmp", lines2[i][1])
        elif lines2[i][0] == "jmp":
            lines2[i] = ("nop", lines2[i][1])
        term, acc = test(lines2)
        if term:
            return acc