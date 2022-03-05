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

rulesdict[8] = ([42], [42, 8])
rulesdict[11] = ([42, 31], [42, 11, 31])

def index(string, substring):
    if substring in string: return string.index(substring)
    return -1
    
def matches_rule(string, r):
    if string == "": return 0
    rule = rulesdict[r]
    if isinstance(rule, str):
        if string[0] == rule:
            return 1
        else:
            return -1
    for order in rule:
        amtmatched = 0
        for ruleindex in order:
            result = matches_rule(string[amtmatched:], ruleindex)
            if result == -1 or amtmatched > len(string):
                amtmatched = -1
                break
            amtmatched += result
        if amtmatched != -1: return amtmatched
    return -1
        

c = 0
for line in lines:
    if matches_rule(line, 0) >= len(line):
        c += 1
        print(line)
print(c)