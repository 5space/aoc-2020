def part1():

    with open("dec9/input.txt") as file:
        lines = file.read().strip().split("\n")

    def sum_set(arr):
        a = set()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a.add(arr[i] + arr[j])
        return a

    arr = list(map(int, lines))

    for n in range(25, len(arr)):
        if arr[n] not in sum_set(arr[n-25:n]):
            return arr[n]