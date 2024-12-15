from copy import deepcopy
from pprint import pp
from typing import Tuple


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
    print(f"min_size: {min_size}")

    position = find_guard(items)
    x, y = position
    direction = items[y][x]
    start_val = direction
    positions = [position]
    while True:
        print(f"pos={position} dir={direction}")
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
    pp(items)
    min_size = min(len(items), len(items[0]))
    print(f"min_size: {min_size}")

    position = find_guard(items)
    x, y = position
    direction = items[y][x]
    start_val = direction
    positions = [position]
    while True:
        print(f"pos={position} dir={direction}")
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

    travelled = deepcopy(items)
    for position in positions:
        x, y = position
        travelled[y][x] = "X"

    # pp(positions)
    pp(travelled)
    ans = len(set(positions))
    return ans


def find_guard(grid: list) -> Tuple[int, int]:
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val in TURNS.keys():
                return (x, y)
    raise ValueError("No guard found!")


def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [[*i] for i in f.read().splitlines()]
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
