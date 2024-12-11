from pprint import pp


YEAR, DAY = 2024, 1


def part1(items):
    items = read_input(YEAR, DAY)
    pp(items)
    return


def part2(items):
    items = read_input(YEAR, DAY)
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


def test1():
    items = [
        [""],
        [""],
    ]
    expected = 0
    result = part1(items)
    print(f"expected: {expected}")
    print(f"result  : {result}")
    return result == expected


def test2():
    items = [
        [""],
        [""],
    ]
    expected = 0
    result = part1(items)
    print(f"expected: {expected}")
    print(f"result  : {result}")
    return result == expected


def test3():
    items = [
        [""],
        [""],
    ]
    expected = 0
    result = part1(items)
    print(f"expected: {expected}")
    print(f"result  : {result}")
    return result == expected


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"test1 return: {test1()}")
    # print(f"test2 return: {test2()}")
    # print(f"test3 return: {test3()}")
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
