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
MOVE_DL = MOVE_DIAGONAL_LEFT_DOWN = (-1, -1)

def part1(items):
    items = [[i for i in it] for it in items]
    pp(items)


    # 1. Initialize a counter
    cnt = 0
    
    # 2. Create vertical-down and horiztonal-right slices
    v_downs = defaultdict(list)
    h_rights = defaultdict(list)
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

    # # 4. Create horizontal-right, down, left, right, diagonal left, diagonal right slices
    n_cols, n_rows = len(items[0]), len(items)
    min_size = min(n_rows, n_cols)
    # diagonal_rights = [(i, i) for i in range(min_size)]
    # # diagonal_rights = [items[i][i] for i in range(size)]
    # print(f'diagonal_rights {type(diagonal_rights)}')
    # pp(diagonal_rights)

    # diagonal_lefts = [(i, n_cols - 1 - i) for i in range(min_size)]
    # # diagonal_lefts = [items[i][n_cols - 1 - i] for i in range(size)]
    # print(f'diagonal_lefts {type(diagonal_lefts)}:')
    # pp(diagonal_lefts) 

    fc_drs = defaultdict(list)
    fr_drs = defaultdict(list)
    fc_dls = defaultdict(list)
    fr_dls = defaultdict(list)
    for idx in range(n_cols):
        fc_point = (idx, 0)
        fr_point = (0, idx)

        # First column move diagonal down right
        fc_dr = [move(fc_point, (i, i)) for i in range(min_size)]
        fc_drs[fc_point].extend(fc_dr)

        # First row move diagonal down right
        fr_dr = [move(fr_point, (i, i)) for i in range(min_size)]
        fr_drs[fr_point].extend(fr_dr)

        # # First column move diagonal down left
        fc_dl = [move(fc_point, (i, n_cols - 1 - i)) for i in range(min_size)]
        fc_dls[fc_point].extend(fc_dl)

        # First row move diagonal down left
        fr_dl = [move(fr_point, (i, n_cols - 1 - i)) for i in range(min_size)]
        fr_dls[fr_point].extend(fr_dl)


    print(f'fc_drs {type(fc_drs)}')
    pp(dict(fc_drs))

    print(f'fr_drs {type(fr_drs)}')
    pp(dict(fr_drs))
    
    print(f'fc_dls {type(fc_dls)}')
    pp(dict(fc_dls))
    
    print(f'fr_dls {type(fr_dls)}')
    pp(dict(fr_dls))

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
