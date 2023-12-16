from math import prod
from pprint import pprint


year, day = 2023, 6


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [i.split(":")[1].strip().split() for i in f.read().splitlines()]
    times, distances = items
    times, distances = map(int, times), map(int, distances)
    races = list(zip(times, distances))

    win_cnts = []
    for t, d in races:
        win_cnt = 0
        for hold_time in range(1, t, 1):
            run_time = t - hold_time
            run_dist = hold_time * run_time
            if run_dist > d:
                win_cnt += 1
        win_cnts.append(win_cnt)
    return prod(win_cnts)


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [
            int("".join(i.split(":")[1].strip().split())) for i in f.read().splitlines()
        ]
    win_cnt = 0
    t, d = items
    for hold_time in range(1, t, 1):
        run_time = t - hold_time
        run_dist = hold_time * run_time
        if run_dist > d:
            win_cnt += 1
    return win_cnt


if __name__ == "__main__":
    # print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
