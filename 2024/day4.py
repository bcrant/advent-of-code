from pprint import pp


YEAR, DAY = 2024, 4


def part1(items):
    # 1. Initialize a counter
    cnt = 0
    # 2. Create vertical-down slice
    v_downs = []
    # v_ups = [v_down.reverse() for v_down in v_downs]
    h_rights = []
    for row_idx, row in enumerate(items):
        h_rights.append([i for i in row])
        for col_idx, col in enumerate(row):
            v_downs.append(col)
    print(f'v_downs {type(v_downs)}:')
    pp(v_downs)
    print(f'h_rights {type(h_rights)}:')
    pp(h_rights)
    # 3. Reverse vertical-down slices for vertical-up
    # 4. Create horizontal-right, down, left, right, diagonal left, diagonal right slices
    # 3. Count all occurrences of "xmas" in each slice
    # 4. Return 
    return


def part2(items):
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
