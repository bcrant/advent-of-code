""" https://adventofcode.com/2022/day/7 """

from collections import defaultdict


def main() -> dict:
    with open("data/day7_input.txt", "r") as f:
        lines = [line for line in f.read().splitlines()]

    path_sizes = defaultdict(int)
    path = []
    for line in lines:
        if line == "$ cd ..":
            path.pop()
            continue
        else:
            parts = line.split()
            if parts[1] == "cd":
                # This line is a directory; add to list of children in parent
                path.append(parts[2])
            elif parts[0] == "dir" or parts[1] == "ls":
                continue
            else:
                # This line is a file; add size to directory total size and all parents
                for i in range(1, len(path) + 1):
                    path_sizes["/".join(path[:i])] += int(parts[0])
    return path_sizes


def part1(path_sizes: dict):
    return sum([v for v in path_sizes.values() if v <= 100000])


def part2(path_sizes: dict):
    total_space = 70000000
    min_space = 30000000
    used_space = path_sizes["/"]  # size of root dir
    free_space = total_space - used_space
    for size in sorted(path_sizes.values()):
        if free_space + size >= min_space:
            return size


if __name__ == "__main__":
    data = main()
    print(f"part1 answer: {part1(data)}")
    print(f"part2 answer: {part2(data)}")
