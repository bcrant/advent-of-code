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

def get_adjacent_values(grid: list[list[str]], curr_pos: Tuple[int, int]) -> dict[Tuple[int, int], Union[None, str]]:
    n_cols, n_rows = len(items[0]), len(items)
    min_size = min(n_rows, n_cols)
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
                for _, values in adjacent.items():
                    if (
                        values["next_val"] == "M" 
                        and values["next_next_val"] == "A"
                        and values["next_next_next_val"] == "S"
                    ):
                        cnt += 1
    return cnt

    # # 2. Create vertical-down and horiztonal-right slices
    # v_downs = defaultdict(list)
    # h_rights = defaultdict(list)
    # for row_idx, row in enumerate(items):
    #     h_rights[row_idx] = "".join(row)
    #     for col_idx, col in enumerate(row):
    #         v_downs[col_idx].append(col)

    # # Flatten to list of strings
    # v_downs = ["".join(v_down) for v_down in v_downs.values()]
    # h_rights = ["".join(h_right) for h_right in h_rights.values()]

    # # 3. Reverse vertical-down slices for vertical-up
    # v_ups = [reverse_str(v_down) for v_down in v_downs]
    # h_lefts = [reverse_str(h_right) for h_right in h_rights]

    # # Print debugging steps 1-3
    # print(f'v_downs {type(v_downs)}:')
    # pp(v_downs)
    # print(f'h_rights {type(h_rights)}:')
    # pp(h_rights)
    # print(f'v_ups {type(v_ups)}')
    # pp(v_ups)
    # print(f'h_lefts {type(h_lefts)}')
    # pp(h_lefts)

    # # # 4. Create horizontal-right, down, left, right, diagonal left, diagonal right slices
    # n_cols, n_rows = len(items[0]), len(items)
    # min_size = min(n_rows, n_cols)
    # diagonal_rights = [(i, i) for i in range(min_size)]
    # # diagonal_rights = [items[i][i] for i in range(size)]
    # print(f'diagonal_rights {type(diagonal_rights)}')
    # pp(diagonal_rights)

    # diagonal_lefts = [(i, n_cols - 1 - i) for i in range(min_size)]
    # # diagonal_lefts = [items[i][n_cols - 1 - i] for i in range(size)]
    # print(f'diagonal_lefts {type(diagonal_lefts)}:')
    # pp(diagonal_lefts)

    # fc_drs = defaultdict(list)
    # fr_drs = defaultdict(list)
    # fc_dls = defaultdict(list)
    # fr_dls = defaultdict(list)
    # for idx in range(n_cols):
    #     fc_point = (idx, 0)
    #     fr_point = (0, idx)

    #     # First column move diagonal down right
    #     fc_dr = [move(fc_point, (i, i)) for i in range(min_size)]
    #     fc_drs[fc_point].extend(fc_dr)

    #     # First row move diagonal down right
    #     fr_dr = [move(fr_point, (i, i)) for i in range(min_size)]
    #     fr_drs[fr_point].extend(fr_dr)

    #     # # First column move diagonal down left
    #     fc_dl = [move(fc_point, (i, n_cols - 1 - i)) for i in range(min_size)]
    #     fc_dls[fc_point].extend(fc_dl)

    #     # First row move diagonal down left
    #     fr_dl = [move(fr_point, (i, n_cols - 1 - i)) for i in range(min_size)]
    #     fr_dls[fr_point].extend(fr_dl)

    # print(f"fc_drs {type(fc_drs)}")
    # pp(dict(fc_drs))

    # print(f"fr_drs {type(fr_drs)}")
    # pp(dict(fr_drs))

    # print(f"fc_dls {type(fc_dls)}")
    # pp(dict(fc_dls))

    # print(f"fr_dls {type(fr_dls)}")
    # pp(dict(fr_dls))

    # # 3. Count all occurrences of "xmas" in each slice
    # # 4. Return
    return


def part2(items):
    return


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
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
