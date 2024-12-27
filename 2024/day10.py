from collections import defaultdict, deque
from pprint import pp
from typing import List, Tuple


YEAR, DAY = 2024, 10

START = '0'
END = '9'

MOVE_E = MOVE_EAST = (1, 0)
MOVE_N = MOVE_NORTH = (0, -1)
MOVE_S = MOVE_SOUTH = (0, 1)
MOVE_W = MOVE_WEST = (-1, 0)
MOVES = {
    "E": MOVE_E,
    "N": MOVE_N,
    "S": MOVE_S,
    "W": MOVE_W,
}


def part1(items):
    pp(items)
    start_positions: List[int, int] = []
    end_positions: List[int, int]   = []
    for y, row in enumerate(items):
        for x, val in enumerate(row):
            if val == START:
                start_positions.append((x, y))
            elif val == END:
                end_positions.append((x, y))

    cnt = 0
    trails = defaultdict(dict)
    for start_pos in start_positions:
        curr_pos = start_pos
        trail = []
        while True:
            valid_moves = get_valid_adjacent_moves(items, curr_pos)

            # Base case: Ran out of moves without reaching target
            if not valid_moves:
                break

            for valid_move in valid_moves:
                print(f'valid_move {type(valid_move)}: {valid_move}')

                # Base case: Reached target
                if valid_move in end_positions:
                    trails[curr_pos][valid_move]
                    cnt += 1
                    continue

                trails[curr_pos][valid_move] = {}
                curr_pos = valid_move
            
            break
    print()
    print(f'start_positions : {start_positions}')
    print(f'end_positions   : {end_positions}')
    print()

    print()
    print('Trails...')
    pp(trails)
    print()

    # return len(all_trails)


def part2(items):
    pp(items)
    return


# def get_valid_adjacent_moves(grid: list[list[str]], curr_pos: Tuple[int, int]) -> list:
#     x, y = curr_pos
#     elevation = int(grid[y][x])
#     adjacent = get_adjacent_moves(items, curr_pos)
#     valid_moves = [
#         next_pos
#         for _direction, next_pos, next_val in adjacent
#         if next_val == elevation + 1
#     ]
#     return valid_moves


def get_valid_adjacent_moves(grid: list[list[str]], curr_pos: Tuple[int, int]) -> list:
    x, y = curr_pos
    elevation = int(grid[y][x])
    adjacent = get_adjacent_moves(items, curr_pos)
    valid_moves = [
        next_pos
        for _, next_pos, next_val in adjacent
        if next_val == elevation + 1
    ]
    return valid_moves

def get_adjacent_moves(grid: list[list[str]], curr_pos: Tuple[int, int]) -> list:
    boundaries = (len(grid[0]), len(grid))
    adjacent = []
    for direction, directive in MOVES.items():
        next_pos = move(curr_pos, directive)
        if is_within_bounds(next_pos, boundaries):
            x, y = next_pos
            adjacent.append((direction, next_pos, int(grid[y][x])))
    return adjacent


def is_within_bounds(pos: Tuple[int, int], boundaries: Tuple[int, int]) -> bool:
    px, py = pos
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
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
