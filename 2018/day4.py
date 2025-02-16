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

#             date_noted = item[1:11]
#             hour_noted = int(item[12:14])
#             mins_noted = int(item[15:17])
#             print(f"d={date_noted} h={hour_noted} m={mins_noted}")
#             if hour_noted != 0:
#                 print('day before', item)
#             curr_guard = int(item.split("Guard #")[1].split()[0])
#             log_shifts[date_noted] = curr_guard


# def part1(items):
#     pp(items)
#     log_shifts = {}
#     log_sleeps = {}
#     curr_guard = None
#     nap_start = None
#     nap_end = None
#     for item in items:
#         # print(f'item {type(item)}: {item}')
#         if "Guard #" in item:
#             date_noted = item[1:11]
#             hour_noted = int(item[12:14])
#             mins_noted = int(item[15:17])
#             print(f"d={date_noted} h={hour_noted} m={mins_noted}")
#             if hour_noted != 0:
#                 print('day before', item)
#             curr_guard = int(item.split("Guard #")[1].split()[0])
#             log_shifts[date_noted] = curr_guard
#             # print(f'curr_guard: {curr_guard}')
#     sorted_log_shifts = {}
#     for d in sorted(log_shifts.keys()):
#         sorted_log_shifts[d] = log_shifts[d]
#     log_shifts = sorted_log_shifts
#     pp(log_shifts)
#     return


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
