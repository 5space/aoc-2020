import networkx as nx
import matplotlib.pyplot as plt

with open("dec20/input.txt") as file:
    tiles = file.read().split("\n\n")

all_tiles = {}
for tile in tiles:
    values = tile.split("\n")
    value = values[0]
    rest = values[1:]
    all_tiles[int(value[5:-1])] = rest

def borders(tile):
    a = []
    b1 = tile[0].replace("#", "1").replace(".", "0")
    a.append("".join(min(b1, b1[::-1])))
    b2 = tile[-1].replace("#", "1").replace(".", "0")
    a.append("".join(min(b2, b2[::-1])))
    b3 = "".join(t[0] for t in tile).replace("#", "1").replace(".", "0")
    a.append("".join(min(b3, b3[::-1])))
    b4 = "".join(t[-1] for t in tile).replace("#", "1").replace(".", "0")
    a.append("".join(min(b4, b4[::-1])))
    return a

unique_borders = set()
for k, tile in all_tiles.items():
    unique_borders = unique_borders.union(set(borders(tile)))

print(len(unique_borders))
score = {k: 0 for k in all_tiles.keys()}
all_with_border = {}
for b in unique_borders:
    all_with_border[b] = [k for k in all_tiles.keys() if b in borders(all_tiles[k])]
    for k in all_tiles.keys():
        if b in borders(all_tiles[k]) and sum(1 for k in all_tiles.keys() if b in borders(all_tiles[k])) == 1:
            score[k] += 1

amt = 1
for k in all_tiles.keys():
    if score[k] == 2: print(k)

g = nx.Graph()