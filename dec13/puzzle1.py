with open("dec13/input.txt") as file:
    lines = file.read().splitlines()

ts = int(lines[0])
others = [int(k) for k in lines[1].split(",") if k != "x"]

print(others)

et = 1000000
eb = 0

for bus in others:
    t = -ts % bus
    if t < et:
        et = t
        eb = bus

print(et*eb)