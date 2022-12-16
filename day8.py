""" https://adventofcode.com/2022/day/8 """

import pprint
from collections import defaultdict


def part1():
    with open("./data/day8_example.txt", "r") as f:
        items = [x for x in f.read().splitlines()]
    for item in items:
        print(item)

    rows = len(items)
    cols = len(items[0])
    outer_trees = rows + rows + cols + cols - 4
    print(f"Trees visible from perimeter: {outer_trees}")

    # ROWS
    rows_lr = items
    rows_rl = ["".join([*reversed(row)]) for row in items]

    # COLS
    cols_tb = []
    cols_bt = []
    for col_idx in range(len(items[0])):
        col = [row[col_idx] for row_idx, row in enumerate(items)]
        cols_bt.append("".join([*reversed(col)]))
        cols_tb.append("".join([*col]))

    views = {
        # "COLS_FROM_BOTTOM": cols_bt,
        # "COLS_FROM_TOP": cols_tb,
        "ROWS_FROM_LEFT": rows_lr,
        "ROWS_FROM_RIGHT": rows_rl,
    }
    pprint.pprint(views)

    # Count the  number of trees that are visible from outside the grid
    visible = defaultdict(int)
    for row_idx, row in enumerate(items):
        print()
        print(f"ROW     {row_idx}  | {row}")
        for col_idx, curr in enumerate(row):
            pos = f"x{row_idx}y{col_idx}"
            for view, trees in views.items():
                print(f"VIEW {view} | {trees}")
                left_seq = trees[row_idx][0:col_idx] or trees[row_idx][col_idx]
                right_seq = trees[row_idx][col_idx:] or trees[row_idx][col_idx]

                left_visible = all(n < curr for n in left_seq)
                print(f"CURR {pos}  | {' '.join(left_seq)} < {curr}")
                print(f"left visible: {left_visible}")
                right_visible = all(n > curr for n in right_seq)
                print(f"CURR {pos}  | {' '.join(right_seq)} > {curr}")
                print(f"right visible: {right_visible}")
                is_visible = 1 if left_visible or right_visible else 0
                print(f"is visible: {bool(is_visible)}")

                if not visible[pos]:
                    visible[pos] = 1 if is_visible else 0
    pprint.pprint(visible)

    inner_visible = {}
    for k, v in visible.items():
        if not any(outer in k for outer in ("x0", "x4", "y0", "y4")):
            inner_visible[k] = v
    pprint.pprint(inner_visible)

    inner_trees = sum(inner_visible.values())
    print(f"Inner trees: {inner_trees}")
    print(f"Outer trees: {outer_trees}")
    cnt_visible = inner_trees + outer_trees
    print(f"Visible: {cnt_visible}")


# # LEFT TO RIGHT
# seq = row[0:col_idx] or row[0]
# print(f"seq: {seq}")
# is_visible = all(n < curr for n in seq)
# # print(f"CURR {pos}  | {' '.join(seq)} < {curr}")
# if not visible[pos]:
#     visible[pos] = 1 if is_visible else 0


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")


    # # ROWS
    # rows_lr = items
    # rows_rl = [[*reversed(row)] for row in items]
    #
    # # COLS
    # cols_tb = []
    # cols_bt = []
    # for col_idx in range(len(items[0])):
    #     col = [row[col_idx] for row_idx, row in enumerate(items)]
    #     cols_tb.append(col)
    #     cols_bt.append([*reversed(col)])
    #
    # views = {
    #     "COLS_FROM_BOTTOM": cols_bt,
    #     "COLS_FROM_TOP": cols_tb,
    #     "ROWS_FROM_LEFT": rows_lr,
    #     "ROWS_FROM_RIGHT": rows_rl,
    # }
    # pprint.pprint(views)
    #
    # visible = defaultdict(int)
    # for view, height_records in views.items():
    #     print(view)
    #     for heights in height_records:
    #         for height in heights:
    #             if height > heights[0]:
    #                 visible[view] += 1
    # pprint.pprint(visible)
