from pprint import pp
from typing import List


YEAR, DAY = 2024, 2


def part1(items):
    items = read_input(YEAR, DAY)
    items = [
        list(map(int, i.split()))
        for i in items
    ]

    cnt_safe = 0
    for item in items:
        # 1. Determine if all increasing or all decreasing
        asc = sorted(item)
        dsc = sorted(item, reverse=True)
        is_increasing = True if asc == item else False
        is_decreasing = True if dsc == item else False
        is_linear = any((is_increasing, is_decreasing))
        if not is_linear:
            continue

        # 2. Determine if difference between adjacent levels is <= 3 and >= 1
        idx_a = 0
        in_range = True
        for lvl_b in item[1:]:
            lvl_a = item[idx_a]
            diff = abs(lvl_a - lvl_b)
            _in_range = True if diff >= 1 and diff <= 3 else False
            if not _in_range:
                in_range = False
                break
            idx_a += 1
        
        if is_linear and in_range:
            cnt_safe += 1

    return cnt_safe


def part2(items):
    items = read_input(YEAR, DAY)
    items = [
        list(map(int, i.split()))
        for i in items
    ]

    cnt_safe = 0
    for item in items:
        print()
        print(f'item                : {item}')
        asc = sorted(item)
        dsc = sorted(item, reverse=True)
        is_increasing = True if asc == item else False
        is_decreasing = True if dsc == item else False
        is_linear = any((is_increasing, is_decreasing))

        cnt_levels = len(item)
        cnt_in_range = 0
        cnt_is_increasing = len(item) - 1 if is_increasing else 0
        cnt_is_decreasing = len(item) - 1 if is_decreasing else 0
        cnt_is_equal = 0
        pos_unsafe_levels = []
        idx_a = 0
        for idx_b, lvl_b in enumerate(item[1:]):
            lvl_a = item[idx_a]

            # 1. Determine if all increasing or all decreasing
            if not is_linear:
                cnt_is_increasing += 1 if lvl_a < lvl_b else 0
                cnt_is_decreasing += 1 if lvl_a > lvl_b else 0
            
            is_equal = 1 if lvl_a == lvl_b else 0
            if is_equal:
                pos_unsafe_levels.append(idx_b+1)
                cnt_is_equal += is_equal

            # 2. Determine if difference between adjacent levels is <= 3 and >= 1
            diff = abs(lvl_a - lvl_b)
            in_range = 1 if diff >= 1 and diff <= 3 else 0
            cnt_in_range += in_range
            if not in_range:
                pos_unsafe_levels.append(idx_b+1)
            
            idx_a += 1

        print(f'cnt_levels          : {cnt_levels}')
        print(f'cnt_in_range        : {cnt_in_range}')
        print(f'cnt_is_increasing   : {cnt_is_increasing}')
        print(f'cnt_is_decreasing   : {cnt_is_decreasing}')
        print(f'cnt_is_equal        : {cnt_is_equal}')
        print(f'pos_unsafe_levels   : {pos_unsafe_levels}')
        
        uniq_unsafe_levels = [] if not pos_unsafe_levels else list(set((pos_unsafe_levels)))
        print(f'uniq_unsafe_levels  : {uniq_unsafe_levels}')


        safe_in_range = True if cnt_in_range >= cnt_levels - 1 else False
        print(f'safe_in_range {type(safe_in_range)}: {safe_in_range}')

        safe_is_linear = True if (
            cnt_is_decreasing >= cnt_levels - 1
            or cnt_is_increasing >= cnt_levels - 1
        ) else False
        print(f'safe_is_linear {type(safe_is_linear)}: {safe_is_linear}')

        if (
            len(uniq_unsafe_levels) < 2
            # (safe_is_linear and safe_in_range) and len(uniq_unsafe_levels) < 2
            # or
            # ((safe_is_linear or safe_in_range) and len(uniq_unsafe_levels) < 2)
        ):
            cnt_safe += 1

    return cnt_safe


def read_input(year: int, day: int) -> List[str]:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
