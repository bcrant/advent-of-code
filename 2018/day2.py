from pprint import pp


YEAR, DAY = 2018, 2


def part1(items):
    # case1: cnt contains two of any letter
    case1 = 0
    for item in items:
        uniqs = set((item))
        counts = {uniq: item.count(uniq) for uniq in uniqs}
        if 2 in counts.values():
            case1 += 1

    # case2: cnt contains three of any letter
    case2 = 0
    for item in items:
        uniqs = set((item))
        counts = {uniq: item.count(uniq) for uniq in uniqs}
        if 3 in counts.values():
            case2 += 1

    ans = case1 * case2
    return ans


def part2(items):
    items = [[i for i in item] for item in items]

    for j, a in enumerate(items):
        for k, b in enumerate(items):
            if len(a) != len(b):
                raise ValueError
            if j == k:
                continue
            diff = 0
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                ans = ""
                for n1, n2 in zip(a, b):
                    if n1 != n2:
                        continue
                    ans += n1
                return ans


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
