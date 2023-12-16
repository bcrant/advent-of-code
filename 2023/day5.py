from collections import defaultdict
from pprint import pprint

year, day = 2023, 5


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [i for i in f.read().splitlines() if i]

    seeds = sorted(map(int, items.pop(0).strip("seeds: ").split()))
    maps = defaultdict(list)
    _map = ""
    for item in items:
        if item[0].isalpha():
            _map = item.split()[0]
        if item[0].isnumeric():
            maps[_map].append(list(map(int, item.split())))

    for _, pairs in maps.items():
        next_seeds = []
        for seed in seeds:
            for dst, src, rng in pairs:
                if src <= seed < src + rng:
                    next_seeds.append(seed - src + dst)
                    break
            else:
                next_seeds.append(seed)
        seeds = next_seeds
    return min(seeds)


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items, *blocks = f.read().split("\n\n")

    items = list(map(int, items.split(":")[1].split()))

    seeds = []
    for i in range(0, len(items), 2):
        seeds.append((items[i], items[i] + items[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        next_seeds = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    next_seeds.append((os - b + a, oe - b + a))
                    if os > s:
                        seeds.append((s, os))
                    if e > oe:
                        seeds.append((oe, e))
                    break
            else:
                next_seeds.append((s, e))
        seeds = next_seeds
    return min(seeds)[0]


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
