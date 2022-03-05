lines = [2, 0, 1, 7, 4, 14, 18]

last_seen = [0]*30000000
for i, v in enumerate(lines):
    last_seen[v] = i

next_value = 0
time = len(lines)

while time < 29999999:
    if next_value in last_seen:
        value = time - last_seen[next_value]
    else:
        value = 0
    last_seen[next_value] = time
    time += 1
    next_value = value

print(next_value)