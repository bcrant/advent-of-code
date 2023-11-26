from pprint import pp

y, d = 2021, 5


def part1():
    # with open(f"{y}/data/day{d}_input.txt", "r") as f:
    with open(f"{y}/data/day{d}_example.txt", "r") as f:
        items = f.read().splitlines()

    coordinates = [item.replace(" -> ", ",").split(",") for item in items]
    coordinates = [tuple(map(int, c)) for c in coordinates]

    min_x = max_x = min_y = max_y = 0
    lines = []
    for coordinate in coordinates:
        print(coordinate)
        x1, y1, x2, y2 = coordinate
        if x1 == x2 or y1 == y2:
            x1, x2 = min((x1, x2)), max((x1, x2))
            y1, y2 = min((y1, y2)), max((y1, y2))
            xrange = list(range(x1, x2 + 1))
            yrange = list(range(y1, y2 + 1))
            print(f"xrange {type(xrange)} {xrange}")
            print(f"yrange {type(yrange)} {yrange}")

            if len(xrange) == len(yrange):
                continue
            elif len(xrange) < len(yrange):
                xrange = [xrange[0] for _idx, _val in enumerate(yrange)]
            elif len(xrange) > len(yrange):
                yrange = [yrange[0] for _idx, _val in enumerate(xrange)]
            line = list(zip(xrange, yrange))
            lines.append(line)

        # Fetch plot size
        if x2 > max_x:
            max_x = x2
        if y2 > max_y:
            max_y = y2
    plot = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for line in lines:
        for points in line:
            xp, yp = points[0], points[1]
            if plot[yp][xp] == ".":
                plot[yp][xp] = 0
            if isinstance(plot[yp][xp], int):
                plot[yp][xp] += 1

    flattened_card = [
        item
        for sublist in plot
        for item in sublist
        if isinstance(item, int) and item >= 2
    ]

    return len(flattened_card)


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        # with open(f"{y}/data/day{d}_example.txt", "r") as f:
        items = f.read().splitlines()

    coordinates = [item.replace(" -> ", ",").split(",") for item in items]
    coordinates = [tuple(map(int, c)) for c in coordinates]
    pp(coordinates)

    min_x = max_x = min_y = max_y = 0
    lines = []
    for coordinate in coordinates:
        print()
        print(coordinate)
        x1, y1, x2, y2 = coordinate
        print(f"({x1}, {y1}) -> ({x2}, {y2})")
        x1, x2 = min((x1, x2)), max((x1, x2))
        y1, y2 = min((y1, y2)), max((y1, y2))
        xrange = list(range(x1, x2 + 1))
        yrange = list(range(y1, y2 + 1))
        print(f"xrange {type(xrange)} {xrange}")
        print(f"yrange {type(yrange)} {yrange}")
        if len(xrange) == len(yrange):
            pass
        elif len(xrange) < len(yrange):
            xrange = [xrange[0] for _idx, _val in enumerate(yrange)]
        elif len(xrange) > len(yrange):
            yrange = [yrange[0] for _idx, _val in enumerate(xrange)]
        else:
            print("YOOOOOO")
        line = list(zip(xrange, yrange))
        print(f"line {type(line)} {line}")
        lines.append(line)
        # Fetch plot size
        if x2 > max_x:
            max_x = x2
        if y2 > max_y:
            max_y = y2

    plot = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for line in lines:
        for points in line:
            xp, yp = points[0], points[1]
            if plot[yp][xp] == ".":
                plot[yp][xp] = 1
            else:
                plot[yp][xp] += 1

    pretty_plot = []
    for lines in plot:
        line = []
        for point in lines:
            if point == ".":
                line.append(0)
            else:
                line.append(point)
        pretty_plot.append(line)
    pp(pretty_plot)

    flattened_card = [
        item
        for sublist in plot
        for item in sublist
        if isinstance(item, int) and item >= 2
    ]
    # pp(flattened_card)

    return len(flattened_card)


if __name__ == "__main__":
    # print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
