import time

total = 0
for day in range(1, 26):
    try:
        p1 = __import__(f"dec{day}.puzzle1").puzzle1.part1
        p2 = __import__(f"dec{day}.puzzle2").puzzle2.part2
        t1 = time.time()
        for _ in range(100): p1()
        diff = 10*(time.time() - t1)
        print(f"Puzzle {day}.1\t{p1()}\t{round(diff, 5)}ms")
        total += diff

        t1 = time.time()
        for _ in range(100): p2()
        diff = 10*(time.time() - t1)
        print(f"Puzzle {day}.2\t{p2()}\t{round(diff, 5)}ms")
        total += diff
    except ModuleNotFoundError:
        break

print(f"Execution took {round(total, 5)}ms")
