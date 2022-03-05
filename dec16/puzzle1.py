with open("dec16/input.txt") as file:
    info, myticket, nearbytickets = file.read().split("\n\n")

def is_valid(num, ranges):
    rab, rcd = ranges.split(" or ")
    ra, rb = rab.split("-")
    rc, rd = rcd.split("-")
    ra, rb, rc, rd = int(ra), int(rb), int(rc), int(rd)
    return ra <= num <= rb or rc <= num <= rd

info = {k: v for k, v in [a.split(": ") for a in info.split("\n")]}

nearby = [list(map(int, a.split(","))) for a in nearbytickets.split("\n")[1:]]
c = 0
for n in nearby:
    for i in n:
        if all(not is_valid(i, v) for v in info.values()):
            c += i
print(c)