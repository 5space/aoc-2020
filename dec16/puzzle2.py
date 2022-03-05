from operator import mul
from functools import reduce
import time

time1 = time.time()

with open("dec16/input.txt") as file:
    info, myticket, nearby = file.read().split("\n\n")

def ranges(string):
    rab, rcd = string.split(" or ")
    ra, rb = rab.split("-")
    rc, rd = rcd.split("-")
    return (int(ra), int(rb), int(rc), int(rd))

is_valid = lambda n, a, b, c, d: a <= n <= b or c <= n <= d

info = {k: ranges(v) for k, v in [a.split(": ") for a in info.split("\n")]}
myticket = list(map(int, myticket.split("\n")[1].split(",")))
nearby = [list(map(int, a.split(","))) for a in nearby.split("\n")[1:]]

for n in nearby[:]:
    for i in n:
        if all(not is_valid(i, *v) for v in info.values()):
            nearby.remove(n)

allkeys = set(info.keys())
SIZE = len(allkeys)

possible = [allkeys.copy() for _ in range(SIZE)]
counter = SIZE**2

for i in range(SIZE):
    for field, ranges in info.items():
        if any(not is_valid(n[i], *ranges) for n in nearby):
            possible[i].remove(field)
            counter -= 1

while counter > SIZE:
    for i in range(SIZE):
        if len(possible[i]) == 1:
            element = next(iter(possible[i]))
            for a in range(SIZE):
                if a != i and element in possible[a]:
                    possible[a].remove(element)
                    counter -= 1

possible = [p.pop() for p in possible]
print(reduce(mul, [myticket[i] for i in range(SIZE) if "departure" in possible[i]]))
print(time.time()-time1)