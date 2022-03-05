with open("dec10/input.txt") as file:
    lines = file.read().splitlines()

lines = sorted(list(map(int, lines)))
a = [1]+[0]*lines[-1]
for i in lines:a[i]=a[i-3]+a[i-2]+a[i-1]
print(a[-1])