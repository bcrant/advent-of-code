import math


year, day = 2020, 5


def split_node(node: list, direction: str) -> list:
    middle = math.ceil(len(node) / 2)
    if direction in "FL":  # Front / Lower / Left
        return node[0:middle]
    elif direction in "BR":  # Back / Upper / Right
        return node[middle:]


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    rows = [*range(0, 128)]
    cols = [*range(0, 8)]

    row = None
    col = None
    seat_ids = {}
    for item in items:
        _rows = rows
        _cols = cols
        _row = item[0:7]
        _col = item[7:]

        for val in _row:
            _rows = split_node(_rows, val)
            if len(_rows) == 1:
                row = _rows[0]
                break

        for val in _col:
            _cols = split_node(_cols, val)
            if len(_cols) == 1:
                col = _cols[0]
                break

        seat_id = row * 8 + col
        seat_ids[seat_id] = (row, col)

    return max(seat_ids.keys())


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    rows = [*range(0, 128)]
    cols = [*range(0, 8)]

    row = None
    col = None
    seat_ids = {}
    for item in items:
        _rows = rows
        _cols = cols
        _row = item[0:7]
        _col = item[7:]
        for val in _row:
            _rows = split_node(_rows, val)
            if len(_rows) == 1:
                row = _rows[0]
                break

        for val in _col:
            _cols = split_node(_cols, val)
            if len(_cols) == 1:
                col = _cols[0]
                break

        if row > 1 and row < 117:
            seat_id = row * 8 + col
            seat_ids[seat_id] = (row, col)

    min_seat_id = min(seat_ids.keys())
    max_seat_id = max(seat_ids.keys())
    for i in range(min_seat_id, max_seat_id + 1):
        if not i in seat_ids.keys():
            return i


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
