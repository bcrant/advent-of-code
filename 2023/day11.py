import itertools
from pprint import pp


year, day = 2023, 11


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    # 1. Handle expansion. Rows containing only space (periods) and no galaxies (pound sign) should be duplicated.
    # 2. Enumerate all galaxies, identify pairs only once.
    # 3. Determine shortest path between galaxy pairs, using only up/down/left/right

    # 1. Handle expansion. Rows containing only space (periods) and no galaxies (pound sign) should be duplicated.
    rows = items.copy()
    for row_idx, row in enumerate(items):
        if "#" not in row:
            rows.insert(row_idx, row)

    # 2. Enumerate all galaxies, identify pairs only once.
    galaxy_cnt = 1
    galaxy_map = {}
    for row_idx, row in enumerate(rows):
        for col_idx, col in enumerate(row):
            if col == "#":
                galaxy_map[galaxy_cnt] = (row_idx, col_idx)
                galaxy_cnt += 1

    print("Previewing galaxy map...")
    pp(dict(list(galaxy_map.items())[0:5]))

    pairs = list(itertools.combinations(list(galaxy_map.keys()), 2))
    print("Previewing galaxy pairs...")
    pp(pairs[0:5])

    # 3. Determine shortest path between galaxy pairs, using only up/down/left/right
    # TODO(brian)
    return


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
