import itertools
from collections import defaultdict

with open("dec24/input.txt") as file:
    lines = file.read().splitlines()

neighbors = {
    "e": lambda x, y: (x+1, y),
    "w": lambda x, y: (x-1, y),
    "nw": lambda x, y: (x, y-1),
    "ne": lambda x, y: (x+1, y-1),
    "sw": lambda x, y: (x-1, y+1),
    "se": lambda x, y: (x, y+1)
}

flipped = set()
def flip(instr):
    coords = (0, 0)
    for i in instr:
        coords = neighbors[i](*coords)
    if coords in flipped:
        flipped.remove(coords)
    else:
        flipped.add(coords)

for line in lines:
    string = line
    instr = []
    while string != "":
        if string[0] in ("e", "w"):
            instr.append(string[0])
            string = string[1:]
        else:
            instr.append(string[:2])
            string = string[2:]
    flip(instr)

print(len(flipped))

def all_neighbors(x, y):
    return [n(x, y) for n in neighbors.values()]

def iterate():
    neighbor_accum = defaultdict(int)
    for active in flipped:
        for neighbor in all_neighbors(*active):
            if neighbor not in neighbor_accum:
                neighbor_accum[neighbor] = 1
            else:
                neighbor_accum[neighbor] += 1
    for i in set(neighbor_accum.keys()).union(flipped):
        if i in flipped and neighbor_accum[i] not in (1, 2):
            flipped.remove(i)
        elif i not in flipped and neighbor_accum[i] == 2:
            flipped.add(i)

for _ in range(1):
    iterate()
print(len(flipped))
print(flipped)