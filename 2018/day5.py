import sys
from multiprocessing import Pool
from pprint import pp

sys.setrecursionlimit(0x100000)


YEAR, DAY = 2018, 5


def part1(items: str):
    for j, a in enumerate(items[:-1]):
        k, b = j + 1, items[j + 1]
        if a.lower() == b.lower() and (
            (a.islower() and b.isupper()) or (a.isupper() and b.islower())
        ):
            return part1("".join((items[0:j], items[k + 1 :])))
    ans = len(items)
    return ans


def part2(items: str):
    results = {}
    uniqs = set(items.lower())
    rm_items = []
    for uniq in uniqs:
        rm_items.append(
            "".join([i for i in items if i not in (uniq.lower(), uniq.upper())])
        )

    with Pool() as p:
        results[uniq] = p.map(part1, rm_items)

    min_polymers = min(results.values())
    return min_polymers


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    test1_in = "dabAcCaCBAcCcaDA"
    test1_ans = "dabCBAcaDA"
    ans = part1(test1_in)
    assert ans == len(test1_ans)

    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
