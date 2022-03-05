import re
import time

t1 = time.time()

with open("dec19/input.txt") as file:
    lines1, lines2 = file.read().split("\n\n")

rules, lines = lines1.splitlines(), lines2.splitlines()

rulesdict = {}
for r in rules:
    num, a = r.split(": ")
    if a[0] == '"':
        rulesdict[int(num)] = a[1:-1]
    else:
        a2 = a.split(" | ")
        rulesdict[int(num)] = tuple(list(map(int, p.split(" "))) for p in a2)

rulesdict[11] = tuple([42] * n + [31] * n for n in range(1, 5))

depth = 0
def matches_rule(r):
    global depth
    depth += 1
    if depth > 20: return ""

    rule = rulesdict[r]
    if isinstance(rule, str): value = rule
    else: value =  "(" + "|".join(k for order in rule if (k := "".join(matches_rule(ruleindex) for ruleindex in order)) != "") + ")"

    depth -= 1
    if value == "()" or value == "(|)": return ""
    return value

regex = f"^{matches_rule(42)}+{matches_rule(11)}$"

print(time.time() - t1)

c = 0
for line in lines:
    match = re.findall(regex, line)
    if any(m[0] == line for m in match):
        c += 1
# print(regex)
print(c)
print(time.time() - t1)