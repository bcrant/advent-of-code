""" https://adventofcode.com/2021/day/1 """


def part1():
    with open("2021/data/day1_input.txt", "r") as f:
        items = [int(line) for line in f.read().splitlines()]
    cnt = 0
    for idx in range(1, len(items)):
        if items[idx] > items[idx - 1]:
            cnt += 1
    return cnt


def part2():
    with open("2021/data/day1_input.txt", "r") as f:
        items = [int(line) for line in f.read().splitlines()]
    cnt = 0
    prev_window = 0
    for idx in range(2, len(items)):
        window = sum(items[idx - 3 : idx])
        if prev_window < window:
            cnt += 1
        prev_window = window
    return cnt


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
