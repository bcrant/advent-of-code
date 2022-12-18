""" https://adventofcode.com/2022/day/N """

import pprint


def part1():
    # Parse input
    # with open("./data/day7_example.txt", "r") as f:
    with open("./data/day7_input.txt", "r") as f:
        lines = [
            line
            for line in f.read().splitlines()
            if line != "$ ls" and line != "$ cd .."
        ]

    # Marshal input
    curr = ""
    records = {}
    for line in lines:
        if line.startswith("$ cd "):
            curr = line.rsplit(maxsplit=1)[1]
            records[curr] = {"bytes": 0, "dirs": []}
            continue
        parts = line.split()
        if parts[0][0].isnumeric():
            # This line is a file, add file size to directory total size.
            records[curr]["bytes"] += int(parts[0])
        else:
            # This line is a directory, add to list of children in parent
            records[curr]["dirs"].append(parts[1])

    for k, v in records.items():
        print(f'dir: {k} bytes: {v["bytes"]} dirs: {v["dirs"]}')
        queue = [*v["dirs"]]
        while queue:
            tmp = []
            for item in queue:
                v["bytes"] += records[item]["bytes"]
                more_dirs = records[item]["dirs"]
                if more_dirs:
                    tmp.extend(more_dirs)
                queue.remove(item)
            queue.extend(tmp)
        print()
    pprint.pprint(records)

    answer1 = sum([v["bytes"] for v in records.values() if v["bytes"] <= 100000])
    return answer1


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
