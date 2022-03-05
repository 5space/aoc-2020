def part2():

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
    
    def amt_in_bag(color):
        return 1 + sum(v * amt_in_bag(k) for k, v in bags[color].items())
    
    return amt_in_bag("shiny gold") - 1