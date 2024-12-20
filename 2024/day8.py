"""
ORDER OF OPERATIONS
- Find all unique characters
- Find all occurrences of the unique characters
- Determine all pairs and distance between pairs
- Use distance between pairs to generate antinode locations.
- If antinode in map boundary, add one to accumulator.

CAVEATS
- Antinodes only count if they are inside the boundary of the map
- Antinodes can occur at the same location as an antenna
"""

import itertools
from pprint import pp
from typing import Tuple


YEAR, DAY = 2024, 8

AN = "#"

def part1(items):
    pp(items)
    # Find all unique characters
    antennas = [c for c in set(''.join(items)) if c != "."]
    print(f'antennas: {antennas}')
    
    # Find all occurrences of the unique characters
    locations = {k: [] for k in antennas}
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == ".":
                continue
            locations[val].append((x, y))
    pp(locations)

    # Determine all pairs and distance between pairs
    combos = {}
    for k, v in locations.items():
        combos[k] = list(itertools.combinations(v, r=2))
    pp(combos)
    return


def part2(items):
    pp(items)
    return


def get_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    x = abs(p2[0] - p1[0])
    y = abs(p2[1] - p2[1])
    return (x, y)


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)} (test_answer=14)")
    # print(f"part2 answer: {part2(items)}")
