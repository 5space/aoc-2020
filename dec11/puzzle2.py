with open("dec11/input.txt") as file:
    lines = file.read().splitlines()

grid = [list(l) for l in lines]

h = len(grid)
w = len(grid[0])


def raytrace(x, y, direction):
    x += direction[0]
    y += direction[1]
    while 0 <= x <= w-1 and 0 <= y <= h-1:
        if grid[y][x] == "#": return True
        if grid[y][x] == "L": return False
        x += direction[0]
        y += direction[1]
    return False


def iterate():
    global grid
    grid2 = [g[:] for g in grid]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x1 in range(w):
        for y1 in range(h):
            neighbors = sum(1 for d in directions if raytrace(x1, y1, d)) 
            if grid[y1][x1] == "L" and neighbors == 0:
                grid2[y1][x1] = "#"
            elif grid[y1][x1] == "#" and neighbors >= 5:
                grid2[y1][x1] = "L"
    grid = grid2

gridold = []
while gridold != grid:
    gridold = grid
    iterate()

print(sum(a.count("#") for a in grid))
