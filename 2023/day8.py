from pprint import pprint


year, day = 2023, 8


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    steps, items = items[0], items[2:]
    maps = {}
    for item in items:
        k, v = item.split(" = ")
        maps[k] = tuple(v[1:-1].split(", "))

    node = "AAA"
    cnt = 0
    while True:
        for step in steps:
            cnt += 1
            move = 0 if step == "L" else 1
            node = maps.get(node)[move]
            if node == "ZZZ":
                return cnt


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    steps, items = items[0], items[2:]
    maps = {}
    for item in items:
        k, v = item.split(" = ")
        v1, v2 = tuple(v[1:-1].split(", "))
        if k.endswith("A") or v1.endswith("Z") or v2.endswith("Z"):
            maps[k] = tuple(v[1:-1].split(", "))

    pprint(maps)

    start_nodes = [k for k in maps.keys() if k.endswith("A")]

    # while True:
    cnt = 0
    for start_node in start_nodes:
        print(f"start_nodes {type(start_nodes)}: {start_nodes}")
        for step in steps:
            cnt += 1
            move = 0 if step == "L" else 1
            node = maps.get(start_node)[move]


def part2_skip():
    """Unable to get Part 2... Copying from hyper-neutrino to continue..."""
    from math import gcd

    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        steps, _, *rest = f.read().splitlines()

    # steps, _, *rest = open(0).read().splitlines()

    network = {}

    for line in rest:
        pos, targets = line.split(" = ")
        network[pos] = targets[1:-1].split(", ")

    positions = [key for key in network if key.endswith("A")]
    cycles = []

    for current in positions:
        cycle = []

        current_steps = steps
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
                step_count += 1
                current = network[current][0 if current_steps[0] == "L" else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]

    lcm = nums.pop()

    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    print(lcm)


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
    print(f"part2 answer: {part2_skip()}")
