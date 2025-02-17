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
    # pp(logs)

    naps = defaultdict(int)  # key=guard_id value=mins
    mins = defaultdict(dict)
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
            # Determine which guard sleeps the most
            nap_len = nap_end - nap_start
            naps[guard] += nap_len

            # Track which minutes the guards are most often asleep
            if not mins.get(guard):
                mins[guard] = defaultdict(int)
            for n in range(nap_start, nap_end):
                mins[guard][n] += 1

    # pp(naps)
    max_sleep = max(naps.values())
    max_guard = None
    for k, v in naps.items():
        if v == max_sleep:
            max_guard = k
            print(f"max sleep!: guard={k} mins={v}")

    # pp(mins)
    max_asleep = max(mins[max_guard].values())
    max_minute = None
    for k, v in mins[max_guard].items():
        if v == max_asleep:
            max_minute = k

    ans = max_guard * max_minute
    print(f"guard={max_guard} best_min={max_minute} ans={ans}")
    return ans


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
