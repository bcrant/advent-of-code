from collections import defaultdict
from copy import deepcopy
from pprint import pp
from typing import List, Tuple


YEAR, DAY = 2024, 6

MOVE_E = MOVE_EAST = (1, 0)
MOVE_N = MOVE_NORTH = (0, -1)
MOVE_S = MOVE_SOUTH = (0, 1)
MOVE_W = MOVE_WEST = (-1, 0)
MOVES = {
    ">": MOVE_E,
    "^": MOVE_N,
    "v": MOVE_S,
    "<": MOVE_W,
}
TURNS = {
    ">": "v",
    "^": ">",
    "<": "^",
    "v": "<",
}


def part1(items):
    pp(items)
    min_size = min(len(items), len(items[0]))
    position = search_grid(items, TURNS.keys())[0]
    x, y = position
    direction = items[y][x]
    start_val = direction
    positions = []
    while True:
        # print(f"pos={position} dir={direction}")
        positions.append(position)
        directive = MOVES[direction]
        i, j = next_position = move(position, directive)

        if i < 0 or j < 0 or i > min_size or j > min_size:
            print(f"Guard has exited map at: items[{j}][{i}]")
            break

        try:
            next_obstacle = items[j][i]
        except IndexError:
            print(f"Guard has exited map at: items[{j}][{i}]")
            break

        if next_obstacle == "." or next_obstacle == start_val:
            position = next_position
            continue
        elif next_obstacle == "#":
            direction = TURNS[direction]

    # pp(positions)
    ans = len(set(positions))
    return ans


def part2(items):
    # pp(items)
    for i in items: print("".join(i))
    print()

    backup_items = deepcopy(items)

    min_size = min(len(items), len(items[0]))
    position = search_grid(items, TURNS.keys())[0]
    x, y = position
    direction = items[y][x]
    start_pos = position
    start_val = direction
    items[y][x] = "."
    visited = set()
    turns = []
    while True:
        # print(f"pos={position} dir={direction}")
        visited.add((position, direction))
        directive = MOVES[direction]
        i, j = next_position = move(position, directive)
        if i < 0 or j < 0 or i >= min_size or j >= min_size:
            print(f"Guard has exited map at: (x={i}, y={j})")
            break
        
        next_obstacle = items[j][i]
        if next_obstacle == ".":
            position = next_position
        elif next_obstacle == "#":
            direction = TURNS[direction]
            turns.append(position)

    # PART 2
    for idx, visit in enumerate(visited):
        (position, direction) = visit
        directive = MOVES[direction]
        i, j = move(position, directive)
        if i < 0 or j < 0 or i >= min_size or j >= min_size:
            print(f"Guard has exited map at: (x={i}, y={j})")
            break


    plot_moves(visited, turns, start_pos, start_val)
    ans = len(set(visited))
    return ans






def search_grid(grid: list, search_keys: List[str]) -> List[Tuple[int, int]]:
    matches = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val in search_keys:
                matches.append((x, y))
    if not matches:
        raise ValueError(f"No matches found in grid for: {search_keys}")
    return matches


def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def plot_moves(positions, turns, start_pos, start_val) -> None:
    travelled = deepcopy(items)
    for position, direction in positions:
        x, y = position
        if direction in ("v", "^"):
            travelled[y][x] = "|"
        elif direction in ("<", ">"):
            travelled[y][x] = "-"
        if position == start_pos:
            travelled[y][x] = start_val

    for turn in turns:
        x, y = turn
        travelled[y][x] = "+"

    # print()
    # print(f'positions {type(positions)}')
    for p in positions: print(p)

    print()
    travelled = ["".join(i) for i in travelled]
    print(f'travelled {type(travelled)}')
    for t in travelled: print(t)


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [[*i] for i in f.read().splitlines()]
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
