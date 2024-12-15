from pprint import pp
from typing import List


YEAR, DAY = 2024, 5


def part1(rules: List[List[int]], updates: List[List[int]]) -> int:
    bad_updates_idx = []
    for i, update in enumerate(updates):
        for rule in rules:
            # Ignore rules for pages not in update
            if not all(((_ in update) for _ in rule)):
                continue

            # Fail if y comes before x
            x, y = rule
            if update.index(x) > update.index(y):
                bad_updates_idx.append(i)
                break

    good_updates_idx = [i for i in range(0, len(updates)) if i not in bad_updates_idx]
    good_updates = [updates[i] for i in good_updates_idx]
    ans = sum([gu[len(gu) // 2] for gu in good_updates])
    return ans


def part2(rules: List[List[int]], updates: List[List[int]]) -> int:
    bad_updates_idx = []
    for i, update in enumerate(updates):
        for rule in rules:
            # Ignore rules for pages not in update
            if not all(((_ in update) for _ in rule)):
                continue

            # Fail if y comes before x
            x, y = rule
            if update.index(x) > update.index(y):
                bad_updates_idx.append(i)
                break

    bad_updates = [updates[i] for i in bad_updates_idx]
    good_updates = []

    # TODO(brian): what is an elegant way to do this
    # recursion until no more changes take place?
    for _ in range(0, 5):
        good_updates = reorder(bad_updates, good_updates, rules)

    ans = sum([gu[len(gu) // 2] for gu in good_updates])
    return ans


def reorder(bad_updates: list, good_updates: list, rules: list) -> list:
    good_updates = []
    for bu in bad_updates:
        gu = bu
        for rule in rules:
            # Ignore rules for pages not in update
            if not all(((_ in gu) for _ in rule)):
                continue

            # Swap if y comes before x
            x, y = rule
            a = gu.index(x)
            b = gu.index(y)
            if a > b:
                gu[a], gu[b] = gu[b], gu[a]
        good_updates.append(gu)
    return good_updates


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    items = read_input(YEAR, DAY)
    idx = items.index("")
    items.pop(idx)
    rules = items[0:idx]
    rules = [list(map(int, [r for r in rule.split("|")])) for rule in rules]
    updates = items[idx:]
    updates = [list(map(int, [u for u in update.split(",")])) for update in updates]

    # print()
    # print("Page Ordering Rules")
    # pp(rules)
    # print()
    # print("Updates")
    # pp(updates)

    # print(f"part1 answer: {part1(rules, updates)}")
    print(f"part2 answer: {part2(rules, updates)}")
