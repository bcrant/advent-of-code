from math import floor
from pprint import pp


year, day = 2019, 1


def equation(num: str) -> int:
    return floor(int(num) / 3) - 2


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    acc = 0
    for mass in items:
        acc += equation(mass)
    return acc


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    acc = 0
    for mass in items:
        tmp = equation(mass)
        while tmp > 0:
            acc += tmp
            tmp = equation(tmp)
    return acc


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
