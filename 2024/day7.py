import itertools
from datetime import datetime
from pprint import pp
from typing import Dict, List


YEAR, DAY = 2024, 7
ADD = "+"
CAT = "||"
MUL = "*"


def part1(items: Dict[int, List[int]]):
    ops = [ADD, MUL]
    ans = 0
    for k, v in items.items():
        repeat = len(v) - 1
        combos = list(itertools.product(ops, repeat=repeat))
        for combo in combos:
            op = []
            for i in range(len(v)):
                op.append(v[i])
                try:
                    op.append(combo[i])
                except IndexError:
                    pass

            while len(op) >= 3:
                result = calc(op[0:3])
                op = [result, *op[3:]]
                print(f"op: {op}")

            _sum = int(op[0])
            if _sum != int(k):
                continue
            ans += int(k)
            break
    return ans


def part2(items):
    ops = [ADD, CAT, MUL]
    ans = 0
    for k, v in items.items():
        print(f'{datetime.now()} ans={ans} next_input={v}')
        repeat = len(v) - 1
        combos = list(itertools.product(ops, repeat=repeat))
        for combo in combos:
            op = []
            for i in range(len(v)):
                op.append(v[i])
                try:
                    op.append(combo[i])
                except IndexError:
                    pass

            while len(op) >= 3:
                result = calc(op[0:3])
                op = [result, *op[3:]]
                # print(f"op: {op}")

            _sum = int(op[0])
            if _sum != int(k):
                continue
            ans += int(k)
            break
    return ans


def calc(s: list) -> int:
    a, op, b = int(s[0]), s[1], int(s[2])
    if op == ADD:
        return a + b
    elif op == CAT:
        return int(f"{a}{b}")
    elif op == MUL:
        return a * b

def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        items = [item.split(": ") for item in items]
        items = {int(k): list(map(int, v.split())) for k, v in items}
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")  # 3749
    print(f"part2 answer: {part2(items)}")
