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
        "COLS_FROM_BOTTOM": cols_bt,
        "COLS_FROM_TOP": cols_tb,
        "ROWS_FROM_LEFT": rows_lr,
        "ROWS_FROM_RIGHT": rows_rl,
    }
    pprint.pprint(views)

    # Count the  number of trees that are visible from outside the grid
    visible = defaultdict(int)
    for row_idx, row in enumerate(items[1:-1]):
        print()
        print(f"ROW     {row_idx}  | {row}")
        for col_idx, curr in enumerate(row):
            pos = f"x{row_idx}y{col_idx}"
            print(f"CURR {pos}  | {' '.join(seq)} < {curr}")
            # LEFT TO RIGHT
            seq = row[0:col_idx] or row[0]
            is_visible = all(n < curr for n in seq)
            if not visible[pos]:
                visible[pos] = 1 if is_visible else 0
    pprint.pprint(visible)
    inner_trees = sum(visible.values())
    print(f"Inner trees: {inner_trees}")
    print(f"Outer trees: {outer_trees}")
    cnt_visible = inner_trees + outer_trees
    print(f"Visible: {cnt_visible}")
            # curr_visible = False
            # print(f"x{row_idx}y{col_idx} | {curr}")
            # seq = row[row_idx][0:col_idx]
            # print(f"curr {curr} seq {seq}")

                    # is_visible = curr < items[row_idx][col_idx - 1]
                    # print(f"curr {curr} < item {items[row_idx][col_idx - 1]}: ", is_visible)
                    # print(f"Visible from {view.rsplit('_')[-1]}: {is_visible}")
                    # if curr > items[row_idx][col_idx + 1]:
                    # print(items[row_idx][col_idx])
                    # print(f"Visible from {view.rsplit('_')[-1]}: ")
                    # for n in items[row_idx]:
                    #     # if n >
                    #     # items[row_idx] > items
                    #     print(idx, height)
                    #     # This excludes the perimeter values from being counted
                    #     if height > heights[0]:
                    #         visible[view].append((idx, height))


    # visible = defaultdict(list)
    # for view, height_records in views.items():
    #     for heights in height_records:
    #         print(view, heights)
    #         for idx, height in enumerate(heights):
    #             print(idx, height)
    #             # This excludes the perimeter values from being counted
    #             if height > heights[0]:
    #                 visible[view].append((idx, height))
    # pprint.pprint(visible)


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
