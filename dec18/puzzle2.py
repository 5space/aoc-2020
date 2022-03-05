import time

t1 = time.time()

print(
    sum(
        eval(
            __import__("re").sub(r"(\d)",r"M(\1)",l).replace("*","&"),
            {"M":type("M",
                      (object,),
                      {"__init__":lambda s,n:setattr(s,"n",n),
                       "__new__":lambda c,n:setattr(c,"n",n) or super(type(c),c).__new__(c),
                       "__and__":lambda s,v:type(s)(s.n*v.n),
                       "__add__":lambda s,v:type(s)(s.n+v.n),"n":0
                      })
            }
        ).n for l in open("dec18/input.txt")
    )
)

print(time.time() - t1)

import re

class N:
    def __init__(self, n): self.n = n
    def __and__(self, v): return N(self.n * v.n)
    def __add__(self, v): return N(self.n + v.n)

with open("dec18/input.txt") as file:
    lines = file.read().splitlines()

print(sum(eval(re.sub(r"(\d)", r"N(\1)", line).replace("*", "&")).n for line in lines))

# class N: __init__, __and__, __add__ = lambda self, n: setattr(self, "n", n), lambda self, v: N(self.n * v.n), lambda self, v: N(self.n + v.n)
# print(sum(eval(__import__("re").sub(r"(\d)", r"N(\1)", line).replace("*", "&")).n for line in open("dec18/input.txt")))
