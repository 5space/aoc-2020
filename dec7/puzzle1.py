def part1():
    import re
    with open("dec7/input.txt") as file:
        lines = file.read().strip().split("\n")
    bags = {}
    for line in lines:
        outercolor, b = line.split(" bags contain ")
        bags[outercolor] = {}
        if "no other" in b:
            continue
        b2 = re.findall(r"\d\s\w+\s\w+", b)
        for n in b2:
            num, color = n.split(" ", 1)
            bags[outercolor][color] = int(num)
    bags_that_work = set([b for b in bags.keys() if "shiny gold" in bags[b].keys()])
    last_len = 0
    this_len = 1
    while last_len != this_len:
        last_len = this_len
        for bag in bags.keys():
            if any(b in bags_that_work for b in bags[bag].keys()):
                bags_that_work.add(bag)
        this_len = len(bags_that_work)
    return len(bags_that_work)