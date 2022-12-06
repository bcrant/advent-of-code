""" https://adventofcode.com/2022/day/5 """

from copy import deepcopy


starting_data = {
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


def part1():
    """
    Crates:

    [m] [h]         [n]
    [s] [w]         [f]     [w] [v]
    [j] [j]         [b]     [s] [b] [f]
    [l] [f] [g]     [c]     [l] [n] [n]
    [v] [z] [d]     [p] [w] [g] [f] [z]
    [f] [d] [c] [s] [w] [m] [n] [h] [h]
    [n] [n] [r] [b] [z] [r] [t] [t] [m]
    [r] [p] [w] [n] [m] [p] [r] [q] [l]
     1   2   3   4   5   6   7   8   9
    """
    data = deepcopy(starting_data)
    with open("./data/day5_input.txt", "r") as f:
        items = [line for line in f.read().splitlines() if line.startswith("move")]
    for item in items:
        num_crates, source, target = [int(i) for i in item.split(" ") if i.isnumeric()]
        crates_to_move = [data[source].pop() for _ in range(0, num_crates)]
        data[target] += crates_to_move
    return "".join([v[-1].upper() for k, v in data.items()])


def part2():
    data = deepcopy(starting_data)
    with open("./data/day5_input.txt", "r") as f:
        items = [line for line in f.read().splitlines() if line.startswith("move")]
    for item in items:
        num_crates, source, target = [int(i) for i in item.split(" ") if i.isnumeric()]
        crates_to_move = list(
            reversed([data[source].pop() for _ in range(0, num_crates)])
        )
        data[target] += crates_to_move
    return "".join([v[-1].upper() for k, v in data.items()])


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
