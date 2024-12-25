"""
input : disk map
output: checksum (integer)

ORDER OF OPERATIONS
- Generate incremental ID per each file
- Map ID and length of file to Free Space e.g. { (id, len) : free }
- Pretty print disk map for visualization
- Dictionary keys,  
"""

import re
from pprint import pp


YEAR, DAY = 2024, 9
FREE = "."


def part1(items):
    pp(items)

    # Construct disk map
    files = {}
    _id = 0
    idx = 0
    while idx < len(items):
        file_size = items[idx]
        try:
            free_space = items[idx + 1]
        except IndexError:
            free_space = 0
        files[(_id, int(file_size))] = int(free_space)
        idx += 2
        _id += 1

    print()
    print("Files...")
    pp(files)
    print()

    disk_map = generate_disk_map(files)
    print()
    print("Disk map...")
    print(disk_map)
    print()

    # Get file_ids
    file_id_lkp = {k[0]: k for k in files.keys()}
    file_ids = list(reversed(file_id_lkp.keys()))

    total_free = disk_map.count(FREE)
    free_block = FREE * total_free

    # for _ in range(0, len(disk_map)):
    #     print(f"{_} out of {len(disk_map)}")
    #     last_int = re.search(r"\d", disk_map[::-1])
    #     last_idx = len(disk_map) - last_int.end()
    #     last_len = len(str(last_int[0]))
    #     free_idx = disk_map.index(FREE)
    #     disk_map = disk_map[0:free_idx] + str(last_int[0]) + disk_map[free_idx+last_len:]
    #     disk_map = disk_map[0:last_idx] + FREE + disk_map[last_idx+1:]
    #     # print(disk_map)
    #     # if free_block in disk_map:
    #     #     break

    for file_id in file_ids:
        _id, _len = file_id_lkp[file_id]
        for _ in range(0, _len):
            free_idx = disk_map.index(FREE)
            disk_map = (
                disk_map[0:free_idx] + str(_id) + disk_map[free_idx + len(str(_id)) :]
            )
            rm_idx = "".join(disk_map).rindex(str(_id))
            disk_map = disk_map[0:rm_idx] + FREE + disk_map[rm_idx + len(str(_id)) :]
            # print(disk_map)

        if free_block in disk_map:
            break

    with open("./2024/data/day9_output.txt", "w+") as f:
        f.write(disk_map)

    # Checksum
    checksum = 0
    for idx, _id in enumerate(disk_map):
        if _id != ".":
            checksum += idx * int(_id)
    return checksum


def generate_disk_map(files: dict) -> str:
    disk_map = ""
    for k, v in files.items():
        _id, _len = k
        free = FREE * v
        disk_map += f"{str(_id) * _len}{free}"
    return disk_map


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


"""
I implemented this two different incorrect ways.

First, I forgot to factor in the length of the ID itself, treating all
items as one character instead of one "block".

Second, I regex searched for the ID, which was really just another way
to incorrectly implement the first approach.

I'm once again using Jonathan Paulson's answer to keep moving...
"""

from collections import deque


def solve(part2, items):
    D = items
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i, c in enumerate(D):
        if i % 2 == 0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for pos, sz, file_id in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f"{FINAL[pos+i]=}"
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break

    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans


if __name__ == "__main__":
    items = read_input(YEAR, DAY)

    p1 = solve(False, items)
    p2 = solve(True, items)
    print(p1)
    print(p2)

    # print(f"part1 answer: {part1(items)}") # test answer=1928
    # 257887944877 answer too low
    # 88100595464 too low
    # 6201130364722 correct
    # print(f"part2 answer: {part2(items)}")
