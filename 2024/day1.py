from pprint import pp

YEAR, DAY = 2024, 1


def part1(items):
    l = [int(i.split()[0]) for i in items]
    r = [int(i.split()[1]) for i in items]
    diff = 0
    while l and r:
        min_l_idx = l.index(min(l))
        min_r_idx = r.index(min(r))
        min_l = l[min_l_idx]
        min_r = r[min_r_idx]
        diff += abs(min_l - min_r)
        l.pop(min_l_idx)
        r.pop(min_r_idx)
    return diff


def part2(items):
    items = read_input(YEAR, DAY)
    l = [int(i.split()[0]) for i in items]
    r = [int(i.split()[1]) for i in items]
    score = 0
    for n in l:
        cnt = r.count(n)
        score += n * cnt
    return score


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    pp(items)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
