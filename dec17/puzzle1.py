import itertools
from collections import defaultdict

with open("dec17/input.txt") as file:
    lines = file.read().splitlines()

actives = set()
for x in range(len(lines[0])):
    for y in range(len(lines)):
        if lines[y][x] == "#": actives.add((x, y, 0))

def all_neighbors(x, y, z):
    return [(x+dx, y+dy, z+dz) for dx, dy, dz in itertools.product([-1, 0, 1], repeat=3) if (dx or dy or dz)]

def display():
    minx, maxx = min(x for x, _, _ in actives), max(x for x, _, _ in actives)
    miny, maxy = min(y for _, y, _ in actives), max(y for _, y, _ in actives)
    minz, maxz = min(z for _, _, z in actives), max(z for _, _, z in actives)
    for z in range(minz-1, maxz+2):
        print("\n".join("".join({True: "#", False: "."}[(x, y, z) in actives] for x in range(minx-1, maxx+2)) for y in range(miny-1, maxy+2)))
        print()
    print(minx, maxx, miny, maxy, minz, maxz)

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
