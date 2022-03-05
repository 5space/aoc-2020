import itertools
from collections import defaultdict

with open("dec17/input.txt") as file:
    lines = file.read().splitlines()

actives = set()
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[y][x] == "#": actives.add((x, y, 0, 0))

def all_neighbors(x, y, z, w):
    return [(x+dx, y+dy, z+dz, w+dw) for dx, dy, dz, dw in itertools.product([-1, 0, 1], repeat=4) if (dx or dy or dz or dw)]

def iterate():
    neighbor_accum = defaultdict(int)
    for active in actives:
        for neighbor in all_neighbors(*active):
            if neighbor not in neighbor_accum:
                neighbor_accum[neighbor] = 1
            else:
                neighbor_accum[neighbor] += 1
    for i in set(neighbor_accum.keys()).union(actives):
        if i in actives and neighbor_accum[i] not in (2, 3):
            actives.remove(i)
        elif i not in actives and neighbor_accum[i] == 3:
            actives.add(i)

for _ in range(6):
    iterate()
    print(len(actives))
