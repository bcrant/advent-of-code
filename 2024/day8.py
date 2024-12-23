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
from collections import defaultdict
from pprint import pp
from typing import Tuple


YEAR, DAY = 2024, 8

AN = "#"

def part1(items):
    pp(items)
    # Boundaries
    boundaries = (len(items[0]), len(items))

    # Find all unique characters
    antennas = [c for c in set(''.join(items)) if c != "."]
    
    # Find all occurrences of the unique characters
    locations = {k: [] for k in antennas}
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == ".":
                continue
            locations[val].append((x, y))

    # Determine all pairs and distance between pairs
    pair_antinodes = set()
    for k, v in locations.items():
        pairs = list(itertools.combinations(v, r=2))
        for pair in pairs:
            antinodes = get_antinodes(pair)
            for antinode in antinodes:
                in_bounds = is_within_bounds(antinode, boundaries)
                if not in_bounds:
                    continue
                pair_antinodes.add(antinode)

    return len(pair_antinodes)


def part2(items):
    pp(items)
    # Boundaries
    boundaries = (len(items[0]), len(items))

    # Find all unique characters
    antennas = [c for c in set(''.join(items)) if c != "."]
    
    # Find all occurrences of the unique characters
    locations = {k: [] for k in antennas}
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == ".":
                continue
            locations[val].append((x, y))

    # Determine all pairs and distance between pairs
    antenna_locations = locations.values()
    antenna_pairs = []
    for antenna_location in antenna_locations:
        antenna_pairs.extend(list(itertools.combinations(antenna_location, r=2)))

    pair_antinodes = set()
    for pair in antenna_pairs:
        print()
        print(f'pair {type(pair)}: {pair}')
        _pair = pair
        p1, p2 = _pair
        s1 = get_slope(p1, p2)
        s2 = get_reverse_slope(s1)
        in_bound = True
        while in_bound:
            p1, p2 = _pair
            a1 = move(p1, s1)
            a2 = move(p1, s2)
            a3 = move(p2, s1)
            a4 = move(p2, s2)
            for antinode in [a1, a2, a3, a4]:
                if antinode in [p1, p2]:
                    continue
                if is_within_bounds(antinode, boundaries):
                    pair_antinodes.add(antinode)
                else:
                    in_bound = False
                print(f'antinode {type(antinode)}: {antinode}')
                _pair = antinode


            # antinodes = get_antinodes(pair)
            # while True:
            #     in_bounds = is_within_bounds(antinodes, boundaries)
            #     print(f'pair: {pair} antinodes: {antinodes}')
            #     for antinode in antinodes:
            #         True
            #     in_bounds = is_within_bounds(antinode, boundaries)
            #     if not in_bounds:
            #         continue
            #     pair_antinodes.add(antinode)

    return len(pair_antinodes)


def get_antinodes(pair: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[int, int]:
    p1, p2 = pair
    s1 = get_slope(p1, p2)
    s2 = get_reverse_slope(s1)
    a1 = move(p1, s1)
    a2 = move(p1, s2)
    a3 = move(p2, s1)
    a4 = move(p2, s2)
    antinodes = [
        antinode
        for antinode in [a1, a2, a3, a4]
        if antinode not in [p1, p2]
    ]
    return antinodes


def get_slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return (x, y)


def get_reverse_slope(slope: Tuple[int, int]) -> Tuple[int, int]:
    x, y = slope
    x = x * -1 if x > 0 else abs(x)
    y = y * -1 if y > 0 else abs(x)
    return (x, y)


def is_within_bounds(pair: Tuple[int, int], boundaries: Tuple[int, int]) -> bool:
    px, py = pair
    xb, yb = boundaries
    in_bounds = True
    if any((p < 0) for p in (px, py)):
        in_bounds = False
    if px >= xb:
        in_bounds = False
    if py >= yb:
        in_bounds = False
    return in_bounds


def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
