with open("dec21/input.txt") as file:
    lines = file.read().splitlines()

recipes = []
for line in lines:
    ingreds, aller = line[:-1].split(" (contains ")
    aller = aller.split(", ")
    ingreds = ingreds.split(" ")
    recipes.append((aller, ingreds))

unique_ingreds = set(i for _, ingreds in recipes for i in ingreds)
unique_allergens = set(i for allergens, _ in recipes for i in allergens)

can_contain = {i: list(unique_allergens) for i in unique_ingreds}

for a in unique_allergens:
    for ra, ri in recipes:
        if a not in ra:
            for i in ri:
                if a in can_contain[i]:
                    can_contain[i].remove(a)

print(can_contain)