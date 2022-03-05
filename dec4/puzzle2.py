def part2():
    with open("dec4/input.txt") as file:
        passports = file.read().strip().split("\n\n")
    c = 0
    for p in passports:
        if not ("byr:" in p and "iyr:" in p and "eyr:" in p and "hgt:" in p and "hcl:" in p and "ecl:" in p and "pid:" in p):
            continue
        p = p.replace("\n", " ").split(" ")
        p = [k.split(":") for k in p]
        flag = True
        for k, v in p:
            if k == "byr" and not (1920 <= int(v) <= 2002): flag = False
            if k == "iyr" and not (2010 <= int(v) <= 2020): flag = False
            if k == "eyr" and not (2020 <= int(v) <= 2030): flag = False
            if k == "hgt":
                if v[-2:] == "cm":
                    if not (150 <= int(v[:-2]) <= 193): flag = False
                elif v[-2:] == "in":
                    if not (59 <= int(v[:-2]) <= 76): flag = False
                else:
                    flag = False
            if k == "hcl":
                if v[0] != "#" or len(v) != 7 or not all(t in "0123456789abcdef" for t in v[1:]): flag = False
            if k == "ecl" and v not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): flag = False
            if k == "pid" and (len(v) != 9 or not v.isnumeric()): flag = False
        if flag:
            c += 1
    return c