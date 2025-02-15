import re
from pprint import pp


YEAR, DAY = 2019, 4


def part1(items: str):
    pp(items)
    _min, _max = (strip_non_digits(s) for s in items.split("-"))

    cnt = 0
    for num in range(_min, _max):
        adj = [(a, b) for a, b in zip(str(num)[0:-1], str(num)[1::])]

        # all numbers equal or increasing left to right
        case1 = [int(a) <= int(b) for a, b in adj]

        # at least one pair of equal adjacent values
        case2 = [int(a) == int(b) for a, b in adj]

        if all(case1) and any(case2):
            print("valid", num)
            cnt += 1

    return cnt


def part2(items):
    pp(items)
    _min, _max = (strip_non_digits(s) for s in items.split("-"))

    valid = []
    for num in range(_min, _max):
        adj = [(a, b) for a, b in zip(str(num)[0:-1], str(num)[1::])]

        # all numbers equal or increasing left to right
        case1 = [int(a) <= int(b) for a, b in adj]
        if not all(case1):
            continue

        # at least one pair of equal adjacent values
        case2 = [int(a) == int(b) for a, b in adj]
        if not any(case2):
            continue

        # at least one pair of equal adjacent values that is NOT part of a larger group
        uniqs = set((s for s in str(num)))
        counts = {uniq: str(num).count(uniq) for uniq in uniqs}
        if any((n >= 3) for n in counts.values()) and 2 not in counts.values():
            continue

        valid.append(num)

    return len(valid)


def read_input(year: int, day: int) -> str:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


def strip_non_digits(s: str) -> int:
    return int(re.sub(r"\D", "", s))


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
