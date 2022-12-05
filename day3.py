""" https://adventofcode.com/2022/day/3 """


def part1():
    with open("./data/day3_input.txt", "r") as f:
        items = f.read().splitlines()
    priority_score = 0
    for item in items:
        # split items by compartment (in half)
        idx = len(item) // 2
        one, two = item[0:idx], item[idx:]
        # find items in both compartments
        common = set(one) & set(two)
        # calculate priority of item in both compartments
        priority_score += get_priority(common.pop())
    return priority_score


def part2():
    with open("./data/day3_input.txt", "r") as f:
        items = f.read().splitlines()
    priority_score = 0
    groups = list(zip(*(iter(items),) * 3))
    for group in groups:
        a, b, c = [set(i) for i in group]
        common = a & b & c
        priority_score += get_priority(common.pop())
    return priority_score


def get_priority(item: str) -> int:
    return ord(item.lower()) - 70 if item.isupper() else 96


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
