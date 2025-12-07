from pprint import pp

IS_TEST = False
YEAR, DAY = 2025, 4


def part1(items):
    pp(items)
    cnt = 0
    _items = []
    for y in range(0, len(items)):
        row = []
        for x in range(0, len(items[0])):
            curr_pos = (x, y)
            curr_val = items[y][x]
            if curr_val != "@":
                row.append(".")
                continue
            adjacent = get_adjacent_values(curr_pos, items)
            # print(f'curr_pos={curr_pos} curr_val={curr_val} adj_cnt={adjacent.count("@")} adj={adjacent}')
            if curr_val == "@" and adjacent.count("@") < 4:
                cnt += 1
                row.append("X")
            else:
                row.append(".")
        _items.append("".join(row))
    pp(_items)
    return cnt


def part2(items, cnt=0, last_cnt=0):
    pp(items)

    # base case
    if cnt > 0 and cnt == last_cnt:
        return cnt

    _cnt = cnt
    _items = []
    for y in range(0, len(items)):
        row = []
        for x in range(0, len(items[0])):
            curr_pos = (x, y)
            curr_val = items[y][x]
            if curr_val != "@":
                row.append(curr_val)
                continue
            adjacent = get_adjacent_values(curr_pos, items)
            # print(f'curr_pos={curr_pos} curr_val={curr_val} adj_cnt={adjacent.count("@")} adj={adjacent}')
            if curr_val == "@" and adjacent.count("@") < 4:
                _cnt += 1
                row.append("x")
            else:
                row.append(curr_val)
        _items.append("".join(row))
    return part2(_items, _cnt, cnt)


def get_adjacent_values(curr_pos: tuple[int, int], data: list[str], diagonals: bool = True):
    # Boundaries
    xb = len(data[0])
    yb = len(data)

    # Cardinal
    MOVE_E = (1, 0)
    MOVE_N = (0, -1)
    MOVE_S = (0, 1)
    MOVE_W = (-1, 0)
    MOVES = {
        "E": MOVE_E,
        "N": MOVE_N,
        "S": MOVE_S,
        "W": MOVE_W,
    }

    # Diagonal
    MOVE_NE = (1, -1)
    MOVE_NW = (-1, -1)
    MOVE_SE = (1, 1)
    MOVE_SW = (-1, 1)
    D_MOVES = {
        "NE": MOVE_NE,
        "NW": MOVE_NW,
        "SE": MOVE_SE,
        "SW": MOVE_SW,
    }

    if diagonals:
        MOVES = {
            **MOVES,
            **D_MOVES,
        }

    values = []
    for move_pos in MOVES.values():
        x, y = move(curr_pos, move_pos)
        if x != abs(x) or y != abs(y) or x > xb or y > yb:
            continue
        # print(f'curr={curr_pos} move={move_pos} next={next_pos}')
        try:
            values.append(data[y][x])
        except IndexError:
            continue
    return values


def move(point: tuple[int, int], direction: tuple[int, int]) -> tuple[int, int]:
    """Apply a move in one direction"""
    result = tuple((x + y for x, y in zip(point, direction)))
    return result


def read_input(year: int, day: int) -> list:
    file_suffix = "input_test" if IS_TEST else "input" 
    with open(f"{year}/data/day{day}_{file_suffix}.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
