""" https://adventofcode.com/2022/day/8 """

import pprint
from collections import defaultdict


def part1():
    with open("./data/day8_example.txt", "r") as f:
        items = [list(map(int, x)) for x in f.read().splitlines()]
    pprint.pprint(items)

    rows = len(items)
    cols = len(items[0])
    outer_trees = rows + rows + cols + cols - 4
    print(f"Trees visible from perimeter: {outer_trees}")

    # ROWS
    rows_lr = items
    rows_rl = [[*reversed(row)] for row in items]

    # COLS
    cols_tb = []
    cols_bt = []
    for col_idx in range(len(items[0])):
        col = [row[col_idx] for row_idx, row in enumerate(items)]
        cols_tb.append(col)
        cols_bt.append([*reversed(col)])

    views = {
        "COLS_FROM_BOTTOM": cols_bt,
        "COLS_FROM_TOP": cols_tb,
        "ROWS_FROM_LEFT": rows_lr,
        "ROWS_FROM_RIGHT": rows_rl,
    }
    pprint.pprint(views)

    visible = defaultdict(int)
    for view, height_records in views.items():
        print(view)
        for heights in height_records:
            for height in heights:
                if height > heights[0]:
                    visible[view] += 1
    pprint.pprint(visible)


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
