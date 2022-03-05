import re

class N:
    def __init__(self, n): self.n = n
    def __add__(self, v): return N(self.n + v.n)
    def __sub__(self, v): return N(self.n * v.n)

with open("dec18/input.txt") as file:
    lines = file.read().splitlines()

print(sum(eval(re.sub(r"(\d)", r"N(\1)", line).replace("*", "-")).n for line in lines))

