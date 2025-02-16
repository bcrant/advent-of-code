from collections import defaultdict
from pprint import pp


YEAR, DAY = 2018, 4


def part1(items):
    tmp = {}
    for item in items:
        dt = item[1:17]
        tmp[dt] = item

    logs = {}
    for d in sorted(tmp.keys()):
        logs[d] = tmp[d]
    pp(logs)

    naps = defaultdict(int) # key=guard_id value=mins
    guard = None
    nap_start = None
    nap_end = None
    for dt, msg in logs.items():
        if "Guard #" in msg:
            guard = int(msg.split("Guard #")[1].split()[0])

        elif "falls asleep" in msg:
            nap_start = int(msg[15:17])
        
        elif "wakes up" in msg:
            nap_end = int(msg[15:17])
        
        if nap_start and nap_end:
            nap_len = nap_end - nap_start
            naps[guard] += nap_len
    pp(naps)


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
