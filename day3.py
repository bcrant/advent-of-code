def load_data():
    with open('./data/day3_input.txt', 'r') as f:
        return f.read().splitlines()


def part1():
    items = load_data()
    priority_score = 0
    for item in items:
        # split items by compartment (in half)
        idx = (len(item)//2)
        one, two = item[0:idx], item[idx:]
        # find items in both compartments
        common = set(one) & set(two)
        # calculate priority of item in both compartments
        priority_score += get_priority(common.pop())
    return priority_score


def part2():
    items = load_data()
    priority_score = 0
    groups = list(zip(*(iter(items),) * 3))
    for group in groups:
        a, b, c = [set(i) for i in group]
        common = a & b & c
        priority_score += get_priority(common.pop())
    return priority_score


def get_priority(item: str) -> int:
    key_set = 96
    if item.isupper():
        key_set = 70
    return ord(item.lower()) - key_set


if __name__ == '__main__':
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
