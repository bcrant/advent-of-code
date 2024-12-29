from collections import defaultdict
from functools import cache
from pprint import pp
from typing import List


YEAR, DAY = 2024, 11


def part1(items):
    stones: List[int] = items
    blinks = 25
    for blink in range(1, blinks + 1):
        _stones = []
        for stone in stones:
            is_even = len(str(stone)) % 2 == 0

            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            if stone == 0:
                _stones.append(1)

            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones...
            #       The left half of the digits are engraved on the new left stone,
            #       and the right half of the digits are engraved on the new right stone.
            #       (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            elif is_even:
                mid = int(len(str(stone)) / 2)
                a, b = int(str(stone)[0:mid]), int(str(stone)[mid:])
                _stones.extend([a, b])

            # If none of the other rules apply, the stone is replaced by a new stone...
            #       the old stone's number multiplied by 2024 is engraved on the new stone.
            else:
                _stones.append(stone * 2024)
        stones = _stones
    return len(stones)


def part2(items):
    stones: List[int] = items
    blinks = 75
    return sum(blink(stone, blinks) for stone in stones)


@cache
def blink(stone: int, num_blinks: int) -> list[int]:
    if num_blinks == 0:
        return 1

    if stone == 0:
        return blink(1, num_blinks - 1)

    is_even = len(str(stone)) % 2 == 0
    if is_even:
        mid = int(len(str(stone)) / 2)
        a, b = int(str(stone)[0:mid]), int(str(stone)[mid:])
        return blink(a, num_blinks - 1) + blink(b, num_blinks - 1)

    else:
        return blink(stone * 2024, num_blinks - 1)


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [int(i) for i in f.read().split()]
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
