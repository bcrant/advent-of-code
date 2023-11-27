import math
import pprint


year, day = 2020, 3


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    # Make wider
    max_y = len(items)
    max_x = max_y * len(items[0])
    items = [i * max_x for i in items]

    x = [i for i in range(3, max_x, 3)]
    points = [(x[i], i + 1) for i in range(max_y)][0 : len(items) - 1]

    cnt = 0
    for point in points:
        _x, _y = point
        if items[_y][_x] == "#":
            print(f"_x {_x} _y {_y}")
            cnt += 1
    return cnt


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    # Make wider
    max_y = len(items)
    max_x = max_y * len(items[0])
    items = [i * max_x for i in items]

    # Test many slopes
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    totals = []
    for slope in slopes:
        slope_x, slope_y = slope
        x = [i for i in range(slope_x, max_x, slope_x)][0 : max_y - 1]
        y = [i for i in range(slope_y, max_x, slope_y)][0 : max_y - 1]
        points = [(xx, yy) for xx, yy in zip(x, y)]
        cnt = 0
        for point in points:
            _x, _y = point
            if _y >= len(items):
                break
            if items[_y][_x] == "#":
                cnt += 1
        totals.append(cnt)
    return math.prod(totals)


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
