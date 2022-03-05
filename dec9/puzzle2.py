import time

def part2():

    with open("dec9/input.txt") as file:
        lines = file.read().strip().split("\n")

    arr = list(map(int, lines))

    n = 10884537

    i1 = 0
    i2 = 2
    cum = arr[0] + arr[1]
    while True:
        if cum < n:
            cum += arr[i2]
            i2 += 1
        elif cum > n:
            cum -= arr[i1]
            i1 += 1
        else:
            sl = arr[i1:i2]
            return min(sl) + max(sl)

if __name__ == "__main__":
    t1 = time.time()
    for _ in range(1000): part2()
    print(time.time() - t1)