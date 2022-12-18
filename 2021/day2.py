import pprint

y, d = 2021, 2


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [line.split() for line in f.read().splitlines()]
    depth = horizontal = 0
    for item in items:
        cmd = item[0]
        val = int(item[1])
        if cmd == "forward":
            horizontal += val
        elif cmd == "down":
            depth += val
        elif cmd == "up":
            depth -= val
        else:
            print("im a little teapot")
    return horizontal * depth


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [line.split() for line in f.read().splitlines()]
    aim = depth = horizontal = 0
    for item in items:
        cmd = item[0]
        val = int(item[1])
        if cmd == "forward":
            horizontal += val
            depth += aim * val
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
    return horizontal * depth


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
