import itertools
from pprint import pp


YEAR, DAY = 2025, 3


def part1(items):
    pp(items)
    cnt = 0
    banks = items
    for bank in banks:
        print(f'bank {type(bank)}: {bank}')
        pairs = set()
        j = 0
        while j < len(bank)-1:
            for k in range(j+1, len(bank)):
                pair = int(bank[j]+bank[k])
                pairs.add(pair)
            j += 1
        max_jolts = max(pairs)
        print(f'pairs {type(pairs)}: {pairs}')
        print(f'max_j {type(max_jolts)}: {max_jolts}')
        cnt += max(pairs)
    return cnt


def part2(items):
    cnt = 0
    banks = items
    tiny_banks = []
    for bank in banks:
        # Remove smallest number until only 12 items remain to reduce combinatorics
        for i in range(1, 10):
            _bank = ''.join([_ for _ in bank if int(_) != i])
            if len(_bank) >= 12:
                bank = _bank
            else:
                tiny_banks.append(bank)
                break

    for bank in tiny_banks:
        print(f'bank {len(bank)}: {bank}')
        curr_max = 0
        for combo in itertools.combinations(bank, 12):
            next_max = int(''.join(combo))
            if next_max > curr_max:
                curr_max = next_max
                print(f'next_max: {next_max}')
        cnt += curr_max
    return cnt


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
