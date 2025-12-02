from pprint import pp


YEAR, DAY = 2025, 2


def part1(items):
    pp(items)
    cnt = 0
    for item in items:
        # exclude odd
        if (len(item) % 2) == 1:
            continue
        a = item[0:int(len(item)/2)]
        b = item[int(len(item)/2):]
        if a == b:
            cnt += int(item)
    return cnt


def part2(items):
    pp(items)
    cnt = 0
    for item in items:        
        for k in range(2, len(item)+1):
            pattern = item[:len(item)//k]
            if item == pattern*k:
                cnt += int(item)
                break
    return cnt


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().split(",")
    ids = []
    for item in items:
        if "-" in item:
            a, b = item.split("-")
            for _ in range(int(a), int(b)+1):
                ids.append(str(_))
        else:
            ids.append(item)
    return ids


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")