with open("dec22/input.txt") as file:
    player1, player2 = file.read().split("\n\n")

p1 = list(map(int, player1.split("\n")[1:]))
p2 = list(map(int, player2.split("\n")[1:]))

def simulate(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        a, b = p1.pop(0), p2.pop(0)
        if a > b:
            p1 += [a, b]
        else:
            p2 += [b, a]
    if len(p1) == 0:
        c = p2
    else:
        c = p1
    return sum((len(c)-i)*c[i] for i in range(len(c)))

print(simulate(p1[:], p2[:]))