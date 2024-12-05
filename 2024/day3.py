import operator
import re
from functools import reduce
from itertools import chain

YEAR, DAY = 2024, 3


def part1(items: str):
    muls = items.replace('mul(', '\nmul(').split('\n')
    muls = [re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', mul) for mul in muls]
    muls = list(chain.from_iterable(muls))
    muls = [mul.replace("mul(", "").replace(")", "").split(",") for mul in muls]
    muls = [reduce(operator.mul, list(map(int, mul))) for mul in muls]
    return sum(muls)


def part2(items: str):
    muls = "".join([
        mul.split("don't()")[0]
        for mul in items.split("do()")
    ])
    return part1(muls)


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
