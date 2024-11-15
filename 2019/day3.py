from math import ceil
from pprint import pp
from typing import List, Tuple


year, day = 2019, 3


CENTRAL_PORT = "o"
CROSSED_WIRE = "X"
MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}


def part1(items: list) -> int:
    w1, w2 = items
    grid = create_grid(w1, w2)
    wire1_path = []
    for instruction in w1:
        direction, repeat = instruction[0], instruction[1:] 
    start1 = w1[0]
    print(f'start1 {type(start1)}: {start1}')
    start2 = w2[0]
    print(f'start2 {type(start2)}: {start2}')
    
    return


def create_grid(w1, w2) -> List[str]:
    m1 = max([int(n[1:]) for n in w1])
    m2 = max([int(n[1:]) for n in w2])
    wh = (ceil(max(m1, m2) / 100.00) * 100) * 2
    row = ".".join(["" for _ in range(0, wh+1)])
    arr = [row for _ in range(0, wh+1)]
    return arr

def move(self, point: Tuple[int, int], direction: str) -> Tuple[int, int]:
    """Apply a move in one direction"""
    directive = MOVES[direction]
    result = tuple((x + y for x, y in zip(point, directive)))
    return result


def part2(items: list) -> int:
    # pp(items)

    return


def test1():
    items = [
        ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
        ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
    ]
    expected = 159
    result = part1(items)
    assert result == expected


def test2():
    items = [
        ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
        ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
    ]
    expected = 135
    result = part2(items)
    assert result == expected


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [i.split(",") for i in f.read().splitlines()]
        return items


if __name__ == "__main__":
    input = read_input(year, day)
    # print(f"part1 answer: {part1(input)}")
    # print(f"part2 answer: {part2(input)}")
    print(f"test1 assert: {test1()}")
    # print(f"test2 assert: {test2()}")
