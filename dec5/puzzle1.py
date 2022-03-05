def part1():
    with open("dec5/input.txt") as file:
        lines = file.readlines()
    return max(int(L.replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2) for L in lines)