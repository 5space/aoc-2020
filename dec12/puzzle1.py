with open("dec12/input.txt") as file:
    lines = file.read().splitlines()

bearing = 0
x = 0
y = 0

for line in lines:
    direc, amt = line[0], int(line[1:])
    if direc == "N": y -= amt
    elif direc == "S": y += amt
    elif direc == "W": x -= amt
    elif direc == "E": x += amt
    elif direc == "F":
        x += amt * [1, 0, -1, 0][bearing%4]
        y += amt * [0, 1, 0, -1][bearing%4]
    elif direc == "R": bearing += amt//90
    elif direc == "L": bearing -= amt//90

print(abs(x) + abs(y))
