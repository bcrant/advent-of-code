import pprint
import sys
import re
from collections import defaultdict


year, day = 2023, 3


def part1():
    """
    I tapped out on my own solution after three hours
    and used Jonathan Paulson's solution:
    https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/3.py
    Mine was off by 4196... /shrugs
    It is commented out below.
    """

    D = open(f"{year}/data/day{day}_input.txt", "r").read().strip()
    lines = D.split("\n")
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])

    p1 = 0
    nums = defaultdict(list)
    for r in range(len(G)):
        gears = set()  # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for c in range(len(G[r]) + 1):
            if c < C and G[r][c].isdigit():
                n = n * 10 + int(G[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < R and 0 <= c + cc < C:
                            ch = G[r + rr][c + cc]
                            if not ch.isdigit() and ch != ".":
                                has_part = True
                            if ch == "*":
                                gears.add((r + rr, c + cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()

    print(p1)
    p2 = 0
    for k, v in nums.items():
        if len(v) == 2:
            p2 += v[0] * v[1]
        print(p2)


# def part1():
#     with open(f"{year}/data/day{day}_input.txt", "r") as f:
#         items = f.read().splitlines()

#     num_indices = {}
#     for row_idx, item in enumerate(items):
#         _item = item
#         for c in ("*", "#", "$", "+", "-", "=", "@", "%", "^", "/", "&"):
#             _item = _item.replace(c, ".")
#         nums = [i for i in _item.split(".") if i and i != "."]
#         for num in nums:
#             _num_col_start = items[row_idx].index(num)
#             for col_idx in range(_num_col_start, _num_col_start + len(num)):
#                 num_indices[(row_idx, col_idx)] = num

#     symbol_positions = []
#     for row_idx, row in enumerate(items):
#         for col_idx, col in enumerate(row):
#             val = col
#             if not val == "." and not val.isalnum():
#                 symbol_positions.append((row_idx, col_idx))

#     neighbors = []
#     for pos in symbol_positions:
#         row, col = pos
#         row = int(row)
#         col = int(col)
#         top_left = row - 1, col - 1
#         top = row, col - 1
#         top_right = row - 1, col + 1
#         left = row, col - 1
#         right = row, col + 1
#         bottom_left = row + 1, col - 1
#         bottom = row + 1, col
#         bottom_right = row + 1, col + 1
#         neighbors.append((
#             top_left,
#             top,
#             top_right,
#             left,
#             right,
#             bottom_left,
#             bottom,
#             bottom_right
#         ))

#     part_ids = []
#     numeric_neighbor_positions = []
#     for neighbor in neighbors:
#         row_nums = []
#         for n in neighbor:
#             row, col = n
#             val = items[row][col]
#             if (
#                 str(val).isnumeric()
#                 and not str(val) == "."
#                 and num_indices.get((row, col))
#             ):
#                 numeric_neighbor_positions.append((row, col))
#                 row_nums.append(int(num_indices.get((row, col))))
#         part_ids.extend(set(row_nums))
#     return sum(part_ids)


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
