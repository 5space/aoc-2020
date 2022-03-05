with open("dec22/input.txt") as file:
    player1, player2 = file.read().split("\n\n")

p1 = list(map(int, player1.split("\n")[1:]))
p2 = list(map(int, player2.split("\n")[1:]))

global_memory = {}
amt = 0
def simulate(p1, p2):
    global amt
    o1, o2 = tuple(p1), tuple(p2)
    if (o1, o2) in global_memory:
        return global_memory[o1, o2]
    memory = set()
    numloops = 0
    while len(p1) > 0 and len(p2) > 0:
        amt += 1
        # if numloops >= 1000:
        #     depth -= 1
        #     return 0, 0
        numloops += 1
        if (tuple(p1), tuple(p2)) in memory:
            return 0, 0
        memory.add((tuple(p1), tuple(p2)))
        a, b = p1.pop(0), p2.pop(0)
        if len(p1) >= a and len(p2) >= b:
            w, _ = simulate(p1[:a], p2[:b])
        else:
            w = a < b
        
        if not w:
            p1 += [a, b]
        else:
            p2 += [b, a]
        
    if len(p1) == 0:
        k = (1, sum((len(p2)-i)*p2[i] for i in range(len(p2))))
    else:
        k = (0, sum((len(p1)-i)*p1[i] for i in range(len(p1))))
    global_memory[o1, o2] = k
    return k

print(simulate(p1[:], p2[:]))
print(amt)