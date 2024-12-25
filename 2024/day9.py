"""
input: disk map
output: checksum (integer)

ORDER OF OPERATIONS
- Generate incremental ID per each file
- Map ID and length of file to Free Space e.g. { (id, len) : free }
- Pretty print disk map for visualization
- Dictionary keys,  
"""

from collections import namedtuple
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

    disk_map = generate_disk_map(files)

    # Get file_ids
    file_id_lkp = {k[0]: k for k in files.keys()}
    file_ids = list(reversed(file_id_lkp.keys()))

    total_free = disk_map.count(".")
    free_block = FREE * disk_map.count(".")

    # Recursively move from end to empty space
    # - get count of free space
    # - create string of free space
    # - while string of free space not in disk map, do...
    # - get index of first free space
    # - get index of last file_id (integer)
    # - pop file_id
    # - insert file_id

    dm = [str(i) for i in disk_map]
    print(''.join(dm))

    for file_id in file_ids:
        _id, _len = file_id_lkp[file_id]
        for _ in range(0, _len):
            free_idx = dm.index(FREE)
            # Does this insert overwrite or insert?
            dm[free_idx] = str(_id)
            dm.append(FREE)
            print(''.join(dm))

            rm_idx = ''.join(dm).rfind(str(_id))
            if rm_idx > len(dm):
                print(f'rm_idx {type(rm_idx)}: {rm_idx}')
                continue
            else:
                dm.pop(rm_idx)

    # Checksum
    checksum = 0
    for idx, _id in enumerate(dm):
        if _id != ".":
            checksum += idx * int(_id)
    return checksum


def generate_disk_map(files: dict) -> str:
    disk_map = ""
    for k, v in files.items():
        _id, _len = k
        free = FREE * v
        disk_map += f"{str(_id) * _len}{free}"
    print()
    print(f"disk_map:")
    print(disk_map)
    return disk_map


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}") # test answer=1928
    # print(f"part2 answer: {part2(items)}")
