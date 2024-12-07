from collections import defaultdict
from pprint import pp
from typing import Tuple


YEAR, DAY = 2024, 4

MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}
MOVE_DR = MOVE_DIAGONAL_RIGHT_DOWN = (1, 1)
MOVE_DL = MOVE_DIAGONAL_LEFT_DOWN = (1, -1)

def part1(items):
    pp(items)

    # 1. Initialize a counter
    cnt = 0
    
    # 2. Create vertical-down and horiztonal-right slices
    v_downs = defaultdict(list)
    h_rights = defaultdict(list)
    d_lefts = defaultdict(list)
    d_rights = defaultdict(list)
    for row_idx, row in enumerate(items):
        h_rights[row_idx] = "".join(row)
        for col_idx, col in enumerate(row):
            v_downs[col_idx].append(col)

    # Flatten to list of strings
    v_downs = ["".join(v_down) for v_down in v_downs.values()]
    h_rights = ["".join(h_right) for h_right in h_rights.values()]

    # 3. Reverse vertical-down slices for vertical-up
    v_ups = [reverse_str(v_down) for v_down in v_downs]
    h_lefts = [reverse_str(h_right) for h_right in h_rights]

    # # Print debugging steps 1-3
    # print(f'v_downs {type(v_downs)}:')
    # pp(v_downs)
    # print(f'h_rights {type(h_rights)}:')
    # pp(h_rights)
    # print(f'v_ups {type(v_ups)}')
    # pp(v_ups)
    # print(f'h_lefts {type(h_lefts)}')
    # pp(h_lefts)

    # 4. Create horizontal-right, down, left, right, diagonal left, diagonal right slices
    n_cols, n_rows = len(items[0]), len(items)
    min_size = min(n_rows, n_cols)
    diagonal_rights = [(i, i) for i in range(min_size)]
    # diagonal_rights = [items[i][i] for i in range(min(n_rows, n_cols))]
    print(f'diagonal_rights {type(diagonal_rights)}')
    pp(diagonal_rights)

    diagonal_lefts = [(i, n_cols - 1 - i) for i in range(min_size)]
    # diagonal_lefts = [items[i][n_cols - 1 - i] for i in range(min(n_rows, n_cols))]
    print(f'diagonal_lefts {type(diagonal_lefts)}:')
    pp(diagonal_lefts)

    dr = defaultdict(list)
    dl = defaultdict(list)
    for row_idx, row in enumerate(items):
        print()
        for col_idx, col in enumerate(row):
            print()
            point = (row_idx, col_idx)
            print(f'point {type(point)}: {point}')
            _dr_point = point
            for _ in range(min_size):
                dr_point = move(_dr_point, MOVE_DR)
                dr_row_idx, dr_col_idx = dr_point
                if dr_row_idx <= min_size and dr_col_idx <= min_size:
                    dr[point].append(dr_point)
                _dr_point = dr_point

            dl_point = move(point, MOVE_DL)
            dl_row_idx, dl_col_idx = dl_point
            if 0 >= dl_row_idx <= min_size and 0 >= dl_col_idx <= min_size:
                dl[point].append(dl_point)

    print(f'dr {type(dr)}:')
    pp(dr)

    print(f'dl {type(dl)}:')
    pp(dl)


    # 3. Count all occurrences of "xmas" in each slice
    # 4. Return 
    return


def part2(items):
    return


def move(point: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    """Apply a move in one direction"""
    if direction == MOVE_DR:
        print(f'MOVE_DR: {direction}')
    if direction == MOVE_DL:
        print(f'MOVE_DL: {direction}')
    result = tuple((x + y for x, y in zip(point, direction)))
    print(f'result : {result}')
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
