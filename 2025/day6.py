import math


IS_TEST = False
YEAR, DAY = 2025, 6


def part1(items):
    items = [str(i).split() for i in items]
    cnt = 0
    for x in range(0, len(items[0])):
        op = items[-1][x]
        cols = [
            int(items[y][x])
            for y in range(0, len(items[0:-1]))
        ]
        cnt += math.prod(cols) if op == "*" else sum(cols)
    return cnt


def part2(items):
    """Instead of attempting to rjust() or ljust() based on least significant
    or most significant number, I simply split on columns containing only
    whitespace, the definied delimiter, and used ordinal positions to group."""
    split_on = []
    for x in range(0, len(items[0])):
        vals = set(items[y][x] for y in range(0, len(items)))
        if vals == set(' '):
            split_on.append(x)
    split_on.append(len(items[0]))
    
    cols = []
    last = 0
    for x in split_on:
        col = [items[y][last:x] for y in range(0, len(items))]
        cols.append(col)
        last = x+1

    cnt = 0
    for col in cols:
        op = str(col[-1]).strip()
        nums = []
        for x in range(0, len(col[0])):
            vals = [
                col[y][x]
                for y in range(0, len(col[0:-1]))
                if col[y][x] != " "
            ]
            nums.append(int("".join(vals)))

        cnt += math.prod(nums) if op == "*" else sum(nums)
    return cnt

def read_input(year: int, day: int) -> list:
    file_suffix = "input_test" if IS_TEST else "input" 
    with open(f"{year}/data/day{day}_{file_suffix}.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
