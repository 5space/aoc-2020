def part2():
    with open("dec1/input.txt") as file:
        numbers = list(map(int, file.readlines()))
    for i in numbers:
        for j in range((2020-i)//2 + 1):
            if j in numbers and 2020-i-j in numbers:
                return i * j * (2020-i-j)