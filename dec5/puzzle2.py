def part2():
    with open("dec5/input.txt") as file:
        lines = file.read().strip().split("\n")
    all_seats = set()
    for line in lines:
        id = int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)
        all_seats.add(id)
    for n in range(1 << 10):
        if n not in all_seats and n+1 in all_seats and n-1 in all_seats:
            return n