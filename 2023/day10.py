from pprint import pprint


year, day = 2023, 10


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    
    rows = len(items)
    print(f'rows: {rows}')
    cols = len(items[0])
    print(f'cols: {cols}')
    start = [
        (idx, row.index("S")) 
        for idx, row in enumerate(items)
        if "S" in row
    ][0]
    print(f'start: row {start[0]} col {start[1]}')
    return


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
    return


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
