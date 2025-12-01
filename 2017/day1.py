from pprint import pp


YEAR, DAY = 2017, 1


def part1(items: list):
    items.append(items[0])
    cnt = 0
    j = 0
    k = 1
    while k < len(items):
        a = items[j]
        b = items[k]
        if a == b:
            cnt += a
        j += 1
        k += 1
    return cnt


def part2(items: list):
    _len = len(items)
    _nxt = int(_len/2)
    items.extend(items)
    cnt = 0
    for j in range(0, _len+1):
        k = int(j+_nxt)
        a = items[j]
        b = items[k]
        if a == b:
            cnt += a
    return cnt


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = list(map(int, f.read().strip()))
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
