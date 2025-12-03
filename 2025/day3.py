from pprint import pp



YEAR, DAY = 2025, 3


def part1(items):
    pp(items)
    cnt = 0
    banks = items
    for bank in banks:
        pairs = set()
        j = 0
        while j < len(bank)-1:
            for k in range(j+1, len(bank)):
                pair = int(bank[j]+bank[k])
                pairs.add(pair)
            j += 1
        cnt += max(pairs)
    return cnt


CACHE = {}

def part2(items):
    cnt = 0
    banks = items
    CACHE = {}
    for bank in banks:
        cnt += memoize(bank, 0, 0)
        CACHE = {}
    return cnt


def memoize(bank, i, seen):
    """
    Taken from Jonathan Paulson, reworded and commented to help my understanding of this technique.
    https://github.com/jonathanpaulson/AdventOfCode/blob/master/2025/3.py
    """
    if i == len(bank) and seen == 12:
        # base case, we have picked 12 digits
        return 0
    if i == len(bank):
        # return invalid if we reach the end and have picked less than 12 digits
        return -10 ** 20
    
    # return from cache if exists, this is how we avoid computing trillions+ of combinations
    cache_key = (i, seen)
    if cache_key in CACHE:
        return CACHE[cache_key]
    
    # compute next digit without choosing it
    ans = memoize(bank, i+1, seen)

    # take existing sequence, adds current digit, then zero fills to the right
    # to produce a 12 digit number. This works since it doesn't matter what numbers are 
    # to the right of current sequence, so long as there are 12 - i. This increases
    # the current maximum faster, allowing us to compute less combinations.
    if seen < 12:
        ans = max(
            ans,
            10 ** (11 - seen) * int(bank[i]) + memoize(bank, i+1, seen+1)
        )
    
    # memoize result in return
    CACHE[cache_key] = ans
    return ans


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    # print(f"part1 answer: {part1(items)}")
    print(f"part2 answer: {part2(items)}")
    # cnt = 0
    # banks = items
    # for bank in banks:
    #     CACHE = {}
    #     cnt += memoize(bank, 0, 0)
    # # 130504248624200
    # # 168617068915447
    # print(f'cnt {type(cnt)}: {cnt}')

