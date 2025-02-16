import re
from collections import Counter
from pprint import pp


YEAR, DAY = 2018, 3


class Claim:
    """
    #123 @ 3,2: 5x4
    ID=123 | 3 from left, 2 from top | 5 wide, 4 height
    """
    def __init__(self, raw: str):
        self.raw = raw
        self.id = int(raw.split(' @ ')[0][1:])
        self.x = int(raw.split('@ ')[1].split(',')[0])
        self.y = int(raw.split(',')[1].split(':')[0])
        self.w = int(raw.split(': ')[1].split('x')[0])
        self.h = int(raw.split('x')[1])

    def __str__(self):
        return f"id={self.id}\tx={self.x}\ty={self.y}\tw={self.w}\th={self.h}"

# def part1(items):
#     grid = ["."*1200 for _ in range(0, 1200)]
#     for item in items:
#         c = Claim(item)
#         for yy in range(c.y, c.y+c.h):
#             for xx in range(c.x, c.x+c.w):
#                 # print(f"xx={xx} yy={yy}")
#                 char = 'X' if grid[yy][xx] == '#' else '#'
#                 grid[yy] = grid[yy][0:xx] + char + grid[yy][xx+1:]
#     ans = 0
#     for line in grid:
#         ans += line.count('X')
#     pp(grid)
#     return ans



def part1(items):
    claims = [[*map(int, re.findall(r'\d+', l))] for l in items if l]
    squares = lambda c: ((i, j) for i in range(c[1], c[1]+c[3])
                                for j in range(c[2], c[2]+c[4]))
    fabric = Counter(s for c in claims for s in squares(c))

    part1 = sum(1 for v in fabric.values() if v > 1)
    return part1


def part2(items):
    claims = [[*map(int, re.findall(r'\d+', l))] for l in items if l]
    squares = lambda c: ((i, j) for i in range(c[1], c[1]+c[3])
                                for j in range(c[2], c[2]+c[4]))
    fabric = Counter(s for c in claims for s in squares(c))
    part2 = next(c[0] for c in claims if all(fabric[s] == 1 for s in squares(c)))
    return part2


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
