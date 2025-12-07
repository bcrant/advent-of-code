from pprint import pp


IS_TEST = False
YEAR, DAY = 2025, 5


def part1(items):
    # pp(items)
    fresh_id_ranges, inventory_ids = str(items).strip().split('\n\n')
    fresh_id_ranges = [i.split("-") for i in fresh_id_ranges.split('\n')]
    fresh_ids = set()
    for x, y in fresh_id_ranges:
        for i in range(int(x), int(y)+1):
            fresh_ids.add(str(i))    
    inventory_ids = set(inventory_ids.split('\n'))
    return len(inventory_ids.intersection(fresh_ids))


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    file_suffix = "input_test" if IS_TEST else "input" 
    with open(f"{year}/data/day{day}_{file_suffix}.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
