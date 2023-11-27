import pprint


year, day = 2020, 3


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    pprint.pprint(items[0:5])
    print("len items", len(items))
    # right 3 down 1
    max_y = len(items)
    max_x = max_y * len(items[0])
    x = [i for i in range(3, max_x, 3)]
    points = [(x[i], i + 1) for i in range(max_y)][0 : len(items) - 1]
    # print(f'points {type(points)}: {points}')
    pprint.pprint(points[0:5])

    # Make wider
    items = [i * max_x for i in items]
    # print(items[0:5])
    print("len(items[0])", len(items[0]))

    cnt = 0
    for point in points:
        _x, _y = point
        if items[_y][_x] == "#":
            print(f"_x {_x} _y {_y}")
            cnt += 1
    return cnt


def part2():
    pass


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
