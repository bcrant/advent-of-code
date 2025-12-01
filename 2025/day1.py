from pprint import pp


YEAR, DAY = 2025, 1


def part1(items):
    cnt_z = 0
    pos = 50
    for item in items:
        direction, turn = item[0], int(item[1:])
        if direction == "L":
            _, pos = divmod(pos-turn, 100)
        if direction == "R":
            _, pos = divmod(pos+turn, 100)
        if pos == 0:
            cnt_z += 1
    return cnt_z


def part2(items):
    cnt_z = 0
    pos = 50
    for item in items:
        direction, turn = item[0], int(item[1:])
        for i in range(turn):
            if direction == "L":
                pos = (pos - 1 + 100) % 100
            if direction == "R":
                pos = (pos + 1 ) % 100
            if pos == 0:
                cnt_z += 1
    return cnt_z


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
