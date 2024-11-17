from math import ceil
from pprint import pp
from timeit import timeit
from typing import List, Tuple


year, day = 2019, 3


MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}
CENTRAL_PORT_CHAR = "o"
CROSSED_WIRE_CHAR = "X"
UP_DOWN_CHAR = "┃"
UP_DOWN_CHAR2 = "│"
LEFT_RIGHT_CHAR = "━"
LEFT_RIGHT_CHAR2 = "─"
COMMON_CHARS = {
    "START": CENTRAL_PORT_CHAR,
    "CROSS": CROSSED_WIRE_CHAR,
}
W1_CHARS = {
    "U": UP_DOWN_CHAR,
    "D": UP_DOWN_CHAR,
    "R": LEFT_RIGHT_CHAR,
    "L": LEFT_RIGHT_CHAR,
}
W2_CHARS = {
    "U": UP_DOWN_CHAR2,
    "D": UP_DOWN_CHAR2,
    "R": LEFT_RIGHT_CHAR2,
    "L": LEFT_RIGHT_CHAR2,
}


def part1(items: list) -> int:
    print()
    w1, w2 = items
    # grid = create_grid(w1, w2)
    # grid = create_grid2(w1, w2)
    grid = None
    # position central port in lower left corner of grid
    # p1 = ceil(len(grid) / 2)
    # start_point = (p1, len(grid)-p1)
    # start_point = (1, -2)
    start_point = (0, 0)
    print(f'start_point {type(start_point)}: {start_point}')
    point = start_point
    # grid = plot(grid, point, "START", 0)
    wires = {1: [], 2: []}
    w1_path = {}
    w2_path = {}

    # Plot wires on grid
    for idx, w in enumerate((w1, w2)):
        wire_id = idx + 1
        print(f'wire_id {type(wire_id)}: {wire_id}')
        for instruction in w:
            direction, repeat = instruction[0], instruction[1:]
            for _ in range(0, int(repeat)):
                point = move(point, direction)
                # grid = plot(grid, point, direction, wire_id)
                wires[wire_id].append(point)
                if wire_id == 1:
                    w1_path[point] = True
                elif wire_id == 2:
                    w2_path[point] = True
        point = start_point
    
    # Plot start point and wire crossings on grid
    print("Finding wire cross points...")

    #
    # Performance testing different data structures
    #

    # dict_time = timeit(
    #     stmt='''[
    #         p
    #         for p in w1_path.keys()
    #         if w2_path.get(p)
    #         and p != start_point
    #     ]''', 
    #     globals={'w1_path': w1_path, 'w2_path': w2_path, 'start_point': start_point},
    #     number=1000
    # )
    # list_time = timeit(
    # 
    #     stmt='''[
    #         p 
    #         for p in wires[1]
    #         if p in wires[2]
    #         and p != start_point
    #     ]''', 
    #     globals={'wires': wires, 'start_point': start_point},
    #     number=1000
    # )
    # set_time = timeit(
    #     stmt='''[
    #         p 
    #         for p in set(wires[1])
    #         if p in set(wires[2])
    #         and p != start_point
    #     ]''', 
    #     globals={'wires': wires, 'start_point': start_point},
    #     number=1000
    # )
    # print(f'dict_time {type(dict_time)}: {dict_time}')
    # print(f'list_time {type(list_time)}: {list_time}')
    # print(f'set_time {type(set_time)}: {set_time}')

    wire_cross_points = [
        p
        for p in w1_path.keys()
        if w2_path.get(p)
        and p != start_point
    ]

    # Plot start point and wire crossings on grid
    # grid = plot(grid, start_point, "START", 0)
    # for p in wire_cross_points:
    #     grid = plot(grid, p, "CROSS", 0)
    # pp(grid)


    print(f'wire_cross_points {type(wire_cross_points)}: {wire_cross_points}')
    manhattan_distances = [
        get_manhattan_distance(start_point, p)
        for p in wire_cross_points
    ]
    print(f'manhattan_distances {type(manhattan_distances)}: {manhattan_distances}')
    smallest_distance = min(manhattan_distances)
    print(f'smallest_distance {type(smallest_distance)}: {smallest_distance}')
    return smallest_distance


def create_grid(w1, w2) -> List[str]:
    m1 = max([int(n[1:]) for n in w1])
    m2 = max([int(n[1:]) for n in w2])
    print(f"max move size: {max(m1, m2)}")
    wh = (ceil(max(m1, m2) / 100.00) * 100) * 3
    print(f'wh {type(wh)}: {wh}')
    row = ".".join(["" for _ in range(0, wh+1)])
    arr = [row for _ in range(0, wh+1)]
    return arr

def create_grid2(w1, w2) -> List[str]:
    # m1 = sum((int(n[1:]) for n in w1))
    # m2 = sum((int(n[1:]) for n in w2))
    # print(f'm1 {type(m1)}: {m1}')
    # print(f'm2 {type(m2)}: {m2}')
    # wh = (ceil(max(m1, m2) / 100.00) * 100) * 2
    wh = 10_000
    print(f'wh {type(wh)}: {wh}')
    row = ".".join(["" for _ in range(0, wh+1)])
    arr = [row for _ in range(0, wh+1)]
    return arr


def get_manhattan_distance(start_point: Tuple[int, int], cross_point: Tuple[int, int]) -> Tuple[int, int]:
    # print()
    # print(f'start_point: {start_point}')
    # print(f'cross_point: {cross_point}')
    x = abs(cross_point[0] - start_point[0])
    y = abs(cross_point[1] - start_point[1])
    diff = (x, y)
    # print(f'diff.......: {diff} -> {sum(diff)}')
    return sum(diff)

def move(point: Tuple[int, int], direction: str) -> Tuple[int, int]:
    """Apply a move in one direction"""
    # print(f'point {type(point)}: {point}')
    directive = MOVES[direction]
    result = tuple((x + y for x, y in zip(point, directive)))
    return result


def plot(grid:  List[str], point: Tuple[int, int], direction: str, wire: int) -> List[str]:
    try:
        line = list(grid[point[1]])
    except IndexError as e:
        print(e)
        print(f'point {type(point)}: {point}')

    if direction not in W1_CHARS.keys():
        line[point[0]] = COMMON_CHARS[direction]
        grid[point[1]] = "".join(line)
        return grid
    if wire == 1:
        line[point[0]] = W1_CHARS[direction]
    elif wire == 2:
        line[point[0]] = W2_CHARS[direction]
    grid[point[1]] = "".join(line)
    return grid


def part2(items: list) -> int:
    # pp(items)

    return


def test1():
    items = [
        ["R8","U5","L5","D3"],
        ["U7","R6","D4","L4"],
    ]
    expected = 6
    result = part1(items)
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected


def test2():
    items = [
        ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
        ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
    ]
    expected = 159
    result = part1(items)
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected


def test3():
    items = [
        ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
        ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
    ]
    expected = 135
    result = part1(items)
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected



def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [i.split(",") for i in f.read().splitlines()]
        return items


if __name__ == "__main__":
    input = read_input(year, day)
    # print(f"test1 return: {test1()}")
    # print(f"test2 return: {test2()}")
    # print(f"test3 return: {test3()}")
    print(f"part1 answer: {part1(input)}")
    # print(f"part2 answer: {part2(input)}")
