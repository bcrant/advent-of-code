

IS_TEST = False
YEAR, DAY = 2025, 5


def part1(items):
    # pp(items)
    fresh_id_ranges, inventory_ids = str(items).strip().split('\n\n')
    fresh_id_ranges = [list(map(int, i.split("-"))) for i in fresh_id_ranges.split('\n')]
    inventory_ids = set(int(i) for i in inventory_ids.split('\n'))
    cnt = 0
    for iid in inventory_ids:
        seen = set()
        for x, y in fresh_id_ranges:
            if iid not in seen and iid >= x and iid <= y:
                seen.add(iid)
                cnt += 1
    return cnt


def part2(items):
    """You can avoid counting the duplicates caused by overlapping ranges by sorting
    the ranges and incrementing the lower bound and counting ids in range."""
    fresh_id_ranges, _ = str(items).strip().split('\n\n')
    fresh_id_ranges = sorted([list(map(int, i.split("-"))) for i in fresh_id_ranges.split('\n')])
    cnt = 0
    curr = -1
    for x, y in fresh_id_ranges:
        if curr >= x:
            x = curr + 1
        if x <= y:
            cnt += y - x + 1
            curr = max(curr, y)
    return cnt


def read_input(year: int, day: int) -> list:
    file_suffix = "input_test" if IS_TEST else "input" 
    with open(f"{year}/data/day{day}_{file_suffix}.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
