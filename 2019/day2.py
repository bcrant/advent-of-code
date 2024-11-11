from copy import deepcopy
from itertools import batched
from pprint import pp


year, day = 2019, 2


def opcode1(n1, n2) -> int:
    return int(n1) + int(n2)


def opcode2(n1, n2) -> int:
    return int(n1) * int(n2)


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
    items = list(map(int, items.split(",")))

    # before running the program, replace position 1 with
    # the value 12 and replace position 2 with the value 2
    items[1] = 12
    items[2] = 2

    pos = 0
    while True:
        op = items[pos : pos + 4]
        opcode, n1, n2, idx = op
        n1 = items[n1]
        n2 = items[n2]
        if opcode == 1:
            output = opcode1(n1, n2)
        if opcode == 2:
            output = opcode2(n1, n2)
        if opcode == 99:
            break

        # print(f'op: {str(items[pos]):<18s}{str((items[pos], items[pos+1], items[pos+2], items[pos+3])):<24s} {str(output):<8s}')
        items[idx] = output
        pos += 4

    # Pretty print: split inputs into batches of opcodes
    # (opcode, input1_index, input2_index, output_index)
    ops = [list(op) for op in batched(items, 4)]
    pp(ops)
    return items[0]


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        data = f.read()
    initial_items = list(map(int, data.split(",")))

    answer = None
    for noun in range(0, 100):
        for verb in range(0, 100):
            items = deepcopy(initial_items)
            # before running the program, replace position 1 with
            # the value 12 and replace position 2 with the value 2
            items[1] = noun
            items[2] = verb
            pos = 0
            while True:
                op = items[pos : pos + 4]
                opcode, n1, n2, idx = op
                n1 = items[n1]
                n2 = items[n2]
                if opcode == 1:
                    output = opcode1(n1, n2)
                if opcode == 2:
                    output = opcode2(n1, n2)
                if opcode == 99:
                    break

                # print(f'op: {str(items[pos]):<18s}{str((items[pos], items[pos+1], items[pos+2], items[pos+3])):<24s} {str(output):<8s}')
                items[idx] = output
                if items[0] == 19_690_720:
                    answer = 100 * noun + verb
                    print(
                        f"success! 100 * noun + verb = 100 * {noun} * {verb} = {answer}"
                    )
                    break
                pos += 4

    # Pretty print: split inputs into batches of opcodes
    # (opcode, input1_index, input2_index, output_index)
    ops = [list(op) for op in batched(items, 4)]
    pp(ops)
    return answer


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
