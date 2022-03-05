file = open("dec7/input.txt").read().splitlines()

a = {}
for x in file:
    z = x.split("contain")
    a[z[0].replace(" ", "")[:-1]] = map(lambda k: k[:-1] if k[-1] == "s" else k, z[1].replace(".", "").replace(" ","").split(","))


def contains(bag):
    total = 0
    w = list(a[bag])
    if w == ["nootherbag"]:
        return 1
    for y in w:
        total += int(y[0]) * contains(y[1:])
    total += 1
    return total


print(contains("shinygoldbag") - 1)