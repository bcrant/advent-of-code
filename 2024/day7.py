import itertools
import math
from pprint import pp
from typing import Dict, List


YEAR, DAY = 2024, 7


def part1(items: Dict[int, List[int]]):
    ans = 0
    for k, v in items.items():
        add_pos = ["+" for _ in range(len(v))]
        mul_pos = ["*" for _ in range(len(v))]
        print(f'add_pos {type(add_pos)}: {add_pos}')
        print(f'mul_pos {type(mul_pos)}: {mul_pos}')

        combos = list(itertools.product(add_pos, mul_pos))
        pp(combos)

        # Try adding all
        if sum(v) == k:
            ans += k
        # Try multiplying all
        if math.prod(v) == k:
            ans += k
        # Try permutations of adding * multiplying
        
        series = sum(v)
    return ans


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        items = [item.split(": ") for item in items]
        items = {int(k): list(map(int, v.split())) for k, v in items}
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
