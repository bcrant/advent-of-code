from collections import defaultdict
from pprint import pp


YEAR, DAY = 2018, 1


def part1(items):
    ans = 0
    for f in items:
        op, num = f[0], int(f[1:])
        if op == "+":
            ans += num
        elif op == "-":
            ans -= num
    return ans


def part2(items):
    ans = 0
    seen = defaultdict(int)
    reached = False
    while not reached:
        for f in items:
            op, num = f[0], int(f[1:])
            if op == "+":
                ans += num
            elif op == "-":
                ans -= num
            seen[ans] += 1
            if seen[ans] == 2:
                return ans


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
