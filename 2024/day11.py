from pprint import pp
from typing import List


YEAR, DAY = 2024, 11


def part1(items):
    pp(items)
    stones: List[int] = items
    blinks = 6
    # blinks = 25
    for blink in range(1, blinks+1):
        print()
        print(f'Blink : {blink}')
        # _stones = []
        for idx, stone in enumerate(stones[:]):
            print(f'Stone : {stone}')
            is_even = len(str(stone)) % 2 == 0

            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            if stone == 0:
                del stones[idx]
                stones.insert(idx, 1)
                print(f"Rule 1: {stones}")

            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones... 
            #       The left half of the digits are engraved on the new left stone, 
            #       and the right half of the digits are engraved on the new right stone. 
            #       (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            elif is_even:
                mid = int(len(str(stone)) / 2)
                a, b = int(str(stone)[0:mid]), int(str(stone)[mid:])
                del stones[idx]
                stones.insert(idx, a)
                stones.insert(idx+1, b)
                print(f"Rule 2: {stones}")

            # If none of the other rules apply, the stone is replaced by a new stone...; 
            #   the old stone's number multiplied by 2024 is engraved on the new stone.
            else:
                del stones[idx]
                stones.insert(idx, stone * 2024)
                print(f"Rule 3: {stones}")
    return ' '.join((str(s) for s in stones))


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [int(i) for i in f.read().split()]
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    print(f"test1 answer: 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2")
    # print(f"part2 answer: {part2(items)}")
