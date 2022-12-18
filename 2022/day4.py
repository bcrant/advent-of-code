""" https://adventofcode.com/2022/day/4 """


def part1():
    with open(f"../data/day4_input.txt", "r") as f:
        items = f.read().splitlines()
    count = 0
    for item in items:
        min1, max1, min2, max2 = [int(i) for i in item.replace(",", "-").split("-")]
        a = set(tuple(range(min1, max1 + 1)))
        b = set(tuple(range(min2, max2 + 1)))
        if a.issubset(b) or b.issubset(a):
            count += 1
    return count


def part2():
    with open(f"../data/day4_input.txt", "r") as f:
        items = f.read().splitlines()
    count = 0
    for item in items:
        min1, max1, min2, max2 = [int(i) for i in item.replace(",", "-").split("-")]
        a = tuple(range(min1, max1 + 1))
        b = tuple(range(min2, max2 + 1))
        if any(n in b for n in a) or any(n in a for n in b):
            count += 1
    return count


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
