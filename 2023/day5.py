from collections import defaultdict
from pprint import pprint

year, day = 2023, 5


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    seeds = sorted(map(int, items.pop(0).strip("seeds: ").split()))

    maps = defaultdict(list)
    _map = ""
    for item in items:
        if not item:
            continue
        if item[0].isalpha():
            _map = item.split()[0]
        if item[0].isnumeric():
            maps[_map].append(list(map(int, item.split())))
    # pprint(maps)

    map_ranges = {}
    for k, vals in maps.items():
        destinations = []
        sources = []
        for val in vals:
            dst, src, rng = val
            destinations.append((dst, dst+rng))
            sources.append((src, src+rng))
        map_ranges[k] = sorted(list(zip(sources, destinations)))
    # pprint(map_ranges)

    seed_maps = {}
    for seed in seeds:
        print(f'seed {type(seed)}: {seed}')
        _seed = seed
        seed_maps[seed] = None
        for k, vals in map_ranges.items():
            print()
            print(k)
            for val in vals:
                src_min, src_max = val[0]
                dst_min, dst_max = val[1]
                if _seed >= src_min and _seed <= src_max:
                    print('seed >= src_min and seed <= src_max')
                    print(f'src_min {type(src_min)}: {src_min}')
                    print(f'src_max {type(src_max)}: {src_max}')
                    print(f'dst_min {type(dst_min)}: {dst_min}')
                    print(f'dst_max {type(dst_max)}: {dst_max}')
                    diff = dst_min - src_min
                    _seed += diff
                    # seed_maps[seed][k] = _seed
                    if k == 'humidity-to-location':
                        seed_maps[seed] = _seed
    return min(seed_maps.values())


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
