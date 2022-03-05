def part1():
    with open("dec4/input.txt") as file:
        passports = file.read().split("\n\n")
    c = 0
    for p in passports:
        if "byr:" in p and "iyr:" in p and "eyr:" in p and "hgt:" in p and "hcl:" in p and "ecl:" in p and "pid:" in p:
            c += 1
    return c