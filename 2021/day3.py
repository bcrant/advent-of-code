import pprint


y, d = 2021, 3


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = f.read().splitlines()
    pprint.pprint(items)
    return


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
