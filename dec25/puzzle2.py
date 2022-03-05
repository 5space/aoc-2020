cp = 6929599
dp = 2448427

val = 1
for e in range(20201227):
    val = (val * 7) % 20201227
    if val == cp:
        print(e)
        break

print(e)
print(pow(dp, e, 20201227))