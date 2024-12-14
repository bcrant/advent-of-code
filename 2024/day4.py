from collections import defaultdict
from pprint import pp
from typing import Tuple, Union


YEAR, DAY = 2024, 4

MOVE_E = MOVE_EAST = (1, 0)
MOVE_N = MOVE_NORTH = (0, -1)
MOVE_S = MOVE_SOUTH = (0, 1)
MOVE_W = MOVE_WEST = (-1, 0)
MOVE_NE = MOVE_NORTH_EAST = (1, -1)
MOVE_NW = MOVE_NORTH_WEST = (-1, -1)
MOVE_SE = MOVE_SOUTH_EAST = (1, 1)
MOVE_SW = MOVE_SOUTH_WEST = (-1, 1)
MOVES = {
    "E": MOVE_E,
    "N": MOVE_N,
    "S": MOVE_S,
    "W": MOVE_W,
    "NE": MOVE_NE,
    "NW": MOVE_NW,
    "SE": MOVE_SE,
    "SW": MOVE_SW
}
OPPOSITE_DIRECTIONS = {
    "NE": "SW",
    "NW": "SE",
    "SW": "NE",
    "SE": "NW",
}
OPPOSITE_CHARACTER = {
    "M": "S",
    "S": "M",
}

def get_adjacent_values(grid: list[list[str]], curr_pos: Tuple[int, int]) -> dict[Tuple[int, int], Union[None, str]]:
    adjacent = {}
    for direction, directive in MOVES.items():
        next_pos = move(curr_pos, directive)
        if is_negative(next_pos):
            continue
        next_val = get_value_if_exists(grid, next_pos)
        next_next_pos = move(next_pos, directive)
        if is_negative(next_next_pos):
            continue
        next_next_val = get_value_if_exists(grid, next_next_pos)
        next_next_next_pos = move(next_next_pos, directive)
        if is_negative(next_next_next_pos):
            continue
        next_next_next_val = get_value_if_exists(grid, next_next_next_pos)
        adjacent[next_pos] = {
            "direction": direction, 
            "next_pos": next_pos, 
            "next_val": next_val, 
            "next_next_pos": next_next_pos,
            "next_next_val": next_next_val,
            "next_next_next_pos": next_next_next_pos,
            "next_next_next_val": next_next_next_val,
        }
    return adjacent


def is_negative(coords: Tuple[int, int]) -> bool:
    x, y = coords
    if x < 0 or y < 0:
        return True
    return False

def get_value_if_exists(grid: list[list[str]], coords: Tuple[int, int]) -> Union[None, Tuple[int, int]]:
    x, y = coords
    try:
        return grid[y][x]
    except IndexError:
        return None


def part1(items):
    items = [[i for i in it] for it in items]
    pp(items)

    # 1. Initialize a counter
    cnt = 0

    # 2.
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            curr_pos = (x, y)
            curr_val = val
            if curr_val == "X":
                adjacent = get_adjacent_values(items, curr_pos)
                for _, v in adjacent.items():
                    if (
                        v["next_val"] == "M" 
                        and v["next_next_val"] == "A"
                        and v["next_next_next_val"] == "S"
                    ):
                        cnt += 1
    return cnt


def get_immediate_adjacent_values(grid: list[list[str]], curr_pos: Tuple[int, int]) -> dict[Tuple[int, int], Union[None, str]]:
    adjacent = {}
    for direction, directive in MOVES.items():
        next_pos = move(curr_pos, directive)
        if is_negative(next_pos):
            continue
        next_val = get_value_if_exists(grid, next_pos)
        adjacent[next_pos] = {
            "direction": direction, 
            "next_pos": next_pos, 
            "next_val": next_val,
        }
    return adjacent


def part2(items):
    items = [[i for i in it] for it in items]
    pp(items)

    # 1. Initialize a counter
    cnt = 0

    # 2.
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            curr_pos = (x, y)
            curr_val = val
            if curr_val == "A":
                adjacent = get_immediate_adjacent_values(items, curr_pos)
                pp(adjacent)
                for _, v in adjacent.items():
                    direction = v["direction"]
                    value = v["next_val"]
                    is_opposite = is_opposite_valid(direction, value)
                    if (
                        True 
                        and ((v["direction"] == "NE" and v["next_val"] == "M") and (v["direction"] == "SW" and v["next_val"] == "S"))
                        and ((v["direction"] == "NW" and v["next_val"] == "M") and (v["direction"] == "SE" and v["next_val"] == "S"))
                    ):
                        cnt += 1
    return cnt


OPPOSITE_DIRECTIONS = {
    "NE": "SW",
    "NW": "SE",
    "SW": "NE",
    "SE": "NW",
}
OPPOSITE_CHARACTER = {
    "M": "S",
    "S": "M",
}
def is_opposite_valid(d: str, v: str) -> bool:
    opposite_v = OPPOSITE_DIRECTIONS

def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def reverse_str(text: str) -> str:
    return text[::-1]


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
