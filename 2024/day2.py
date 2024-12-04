from pprint import pp
from typing import List


YEAR, DAY = 2024, 2


def part1(items):
    items = read_input(YEAR, DAY)
    items = [
        list(map(int, i.split()))
        for i in items
    ]
    pp(items)

    cnt_safe = 0
    for item in items:
        # 1. Determine if all increasing or all decreasing
        asc = sorted(item)
        dsc = sorted(item, reverse=True)
        is_increasing = True if asc == item else False
        print(f'{item} -> asc: {asc} || is_increasing: {is_increasing}')
        is_decreasing = True if dsc == item else False
        print(f'{item} -> dsc: {dsc} || is_decreasing: {is_decreasing}')
        is_linear = any((is_increasing, is_decreasing))
        if not is_linear:
            print("Neither increasing nor decreasing!")
            continue

        # 2. Determine if difference between adjacent levels is <= 3 and >= 1
        idx_a = 0
        in_range = True
        for lvl_b in item[1:]:
            lvl_a = item[idx_a]
            diff = abs(lvl_a - lvl_b)
            _in_range = True if diff >= 1 and diff <= 3 else False
            if not _in_range:
                print(f'Unsafe!! lvl_a: {lvl_a} lvl_b: {lvl_b} diff: {diff} --> in_range: {in_range}')
                in_range = False
                break
            idx_a += 1
        
        if is_linear and in_range:
            cnt_safe += 1

    return cnt_safe


def part2(items):
    items = read_input(YEAR, DAY)
    pp(items)
    return


def read_input(year: int, day: int) -> List[str]:
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
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected


def test2():
    items = [
        [""],
        [""],
    ]
    expected = 0
    result = part1(items)
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected


def test3():
    items = [
        [""],
        [""],
    ]
    expected = 0
    result = part1(items)
    print(f'expected: {expected}')
    print(f'result  : {result}')
    return result == expected


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"test1 return: {test1()}")
    # print(f"test2 return: {test2()}")
    # print(f"test3 return: {test3()}")
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
