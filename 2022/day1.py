""" https://adventofcode.com/2022/day/1 """

from collections import defaultdict


def part1():
    with open("data/day1_input.txt", "r") as f:
        items = f.read().splitlines()
    dd = defaultdict(list)
    total_calories = {}
    elf_num = 1
    for item in items:
        if item != "":
            dd[elf_num].append(int(item))
        else:
            total_calories[elf_num] = sum(dd[elf_num])
            elf_num += 1
    max_cals = (0, 0)
    for k, v in total_calories.items():
        if v > max_cals[1]:
            max_cals = (k, v)
            print(f"elf {k} with {v} calories")
    print(f"The elf with the most calories is: {max_cals}")
    return total_calories


def part2():
    calories_by_elf = part1()
    top_three = sum(list(reversed(sorted([i for i in calories_by_elf.values()])))[0:3])
    print(
        f"The three elves carrying the most calories have a total of {top_three} calories"
    )
    return top_three


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
