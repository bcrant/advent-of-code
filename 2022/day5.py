""" https://adventofcode.com/2022/day/5 """

from copy import deepcopy


starting_stacks = {
    1: ["r", "n", "f", "v", "l", "j", "s", "m"],
    2: ["p", "n", "d", "z", "f", "j", "w", "h"],
    3: ["w", "r", "c", "d", "g"],
    4: ["n", "b", "s"],
    5: ["m", "z", "w", "p", "c", "b", "f", "n"],
    6: ["p", "r", "m", "w"],
    7: ["r", "t", "n", "g", "l", "s", "w"],
    8: ["q", "t", "h", "f", "n", "b", "v"],
    9: ["l", "m", "h", "z", "n", "f"],
}


def part1(moves):
    stacks = deepcopy(starting_stacks)
    for move in moves:
        num_crates, source, target = [int(i) for i in move.split(" ") if i.isnumeric()]
        crates = [stacks[source].pop() for _ in range(0, num_crates)]
        stacks[target] += crates
    return "".join([v[-1].upper() for k, v in stacks.items()])


def part2(moves):
    stacks = deepcopy(starting_stacks)
    for move in moves:
        num_crates, source, target = [int(i) for i in move.split(" ") if i.isnumeric()]
        crates = list(reversed([stacks[source].pop() for _ in range(0, num_crates)]))
        stacks[target] += crates
    return "".join([v[-1].upper() for v in stacks.values()])


if __name__ == "__main__":
    with open("./stacks/day5_input.txt", "r") as f:
        items = [line for line in f.read().splitlines() if line.startswith("move")]

    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
