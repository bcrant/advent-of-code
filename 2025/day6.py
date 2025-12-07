import math
from pprint import pp


IS_TEST = True
YEAR, DAY = 2025, 6


def part1(items):
    cnt = 0
    for x in range(0, len(items[0])):
        col_cnt = 0
        col_op = items[-1][x]
        cols = [
            int(items[y][x])
            for y in range(0, len(items[0:-1]))
        ]
        # print(f'cols {type(cols)}: {cols}')
        # print(f'col_op {type(col_op)}: {col_op}')
        if col_op == "*":
            col_cnt = math.prod(cols)
        elif col_op == "+":
            col_cnt = sum(cols)
        # print(f'col_cnt {type(col_cnt)}: {col_cnt}')
        cnt += col_cnt
    return cnt


def part2(items):
    cnt = 0
    for x in range(0, len(items[0])):
        col_cnt = 0
        col_op = items[-1][x]
        cols = [
            int(items[y][x])
            for y in range(0, len(items[0:-1]))
        ]
        print(f'cols {type(cols)}: {cols}')

        max_digits = len(str(max(cols)))
        cols = [
            str(col).ljust(max_digits, "0")
            for col in cols
        ]
        print(f'cols {type(cols)}: {cols}')

        cols = [
            col[xx]
            for xx in range(0, len(cols[0]))
        ]

        for x in range(0, max_digits):
            if col_op == "*":
                col_cnt = math.prod(cols)
            elif col_op == "+":
                col_cnt = sum(cols)
            # print(f'col_cnt {type(col_cnt)}: {col_cnt}')
            cnt += col_cnt


def read_input(year: int, day: int) -> list:
    file_suffix = "input_test" if IS_TEST else "input" 
    with open(f"{year}/data/day{day}_{file_suffix}.txt", "r") as f:
        items = [i.split() for i in f.read().splitlines()]
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
