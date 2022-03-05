with open("dec12/input.txt") as file:
    lines = file.read().splitlines()

wx = 10
wy = -1

sx = 0
sy = 0

for line in lines:
    direc, amt = line[0], int(line[1:])
    if direc == "N": wy -= amt
    elif direc == "S": wy += amt
    elif direc == "W": wx -= amt
    elif direc == "E": wx += amt
    elif direc == "F":
        sx += wx * amt
        sy += wy * amt
    elif direc == "R":
        wx, wy = [(wx, wy), (-wy, wx), (-wx, -wy), (wy, -wx)][amt//90]
    elif direc == "L":
        wx, wy = [(wx, wy), (-wy, wx), (-wx, -wy), (wy, -wx)][-amt//90]

print(abs(sx) + abs(sy))
