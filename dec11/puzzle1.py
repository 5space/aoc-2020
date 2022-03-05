with open("dec11/input.txt") as file:
    lines = file.read().splitlines()

grid = [list(l) for l in lines]

h = len(grid)
w = len(grid[0])

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def all_neighbors(x, y):
    k = []
    if x > 0:
        k.append((x-1, y))
        if y > 0:
            k.append((x-1, y-1))
        if y < h-1:
            k.append((x-1, y+1))
    if x < w-1:
        k.append((x+1, y))
        if y > 0:
            k.append((x+1, y-1))
        if y < h-1:
            k.append((x+1, y+1))
    if y > 0:
        k.append((x, y-1))
    if y < h-1:
        k.append((x, y+1))
    return k

print(all_neighbors(0, 0))


def iterate():
    global grid
    grid2 = [g[:] for g in grid]
    for x1 in range(w):
        for y1 in range(h):
            neighbors = sum(1 for a in all_neighbors(x1, y1) if grid[a[1]][a[0]] == "#") 
            if grid[y1][x1] == "L" and neighbors == 0:
                grid2[y1][x1] = "#"
            elif grid[y1][x1] == "#" and neighbors >= 4:
                grid2[y1][x1] = "L"
    grid = grid2

gridold = []
while gridold != grid:
    gridold = grid
    iterate()

print(sum(a.count("#") for a in grid))
# print(grid)
