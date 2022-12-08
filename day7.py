""" https://adventofcode.com/2022/day/7 """

import pprint
from collections import defaultdict


def part1():
    with open("./data/day7_input.txt", "r") as f:
        items = f.read().splitlines()

    dirs = defaultdict(list)
    lines = [
        item
        for item in items
        if item != "$ ls" and item != "$ cd .."
    ]
    dir_cmd = "$ cd "
    curr_dir = ""
    for line in lines:
        if dir_cmd in line:
            curr_dir = line.strip(dir_cmd)
        else:
            meta, name = line.split(' ')
            dirs[curr_dir].append((meta, name))
    pprint.pprint(dirs)

    dir_sizes = {}
    for dir_name, children in dirs.items():
        file_size = 0
        for child in children:
            if child[0] != "dir":
                file_size += int(child[0])
        dir_sizes[dir_name] = file_size
    pprint.pprint(dir_sizes)
    print('max ', max(dir_sizes.values()))
    return


def part2():
    with open("./data/day7_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    # print(f"part2 answer: {part2()}")
