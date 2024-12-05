from pprint import pp
from typing import List


YEAR, DAY = 2024, 2


def is_safe(level: List[int]) -> bool:
    asc = sorted(level)
    dsc = sorted(level, reverse=True)
    is_linear = True if asc == level or dsc == level else False
    in_range = True
    for i in range(0, len(level)-1):
        diff = abs(level[i]-level[i+1])
        if not 1 <= diff <= 3:
            in_range = False
    return is_linear and in_range        


def part1(items):
    items = read_input(YEAR, DAY)
    items = [
        list(map(int, i.split()))
        for i in items
    ]

    cnt_safe = 0
    for item in items:
        ok = is_safe(item)
        if ok:
            cnt_safe += 1

    return cnt_safe



def part2(items):
    items = read_input(YEAR, DAY)
    items = [
        list(map(int, i.split()))
        for i in items
    ]

    cnt_safe = 0
    for item in items:
        ok = False
        for j in range(len(item)):
            _item = item[:j] + item[j+1:]
            if is_safe(_item):
                ok = True
        if ok:
            cnt_safe += 1
    return cnt_safe


def read_input(year: int, day: int) -> List[str]:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
