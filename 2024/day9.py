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


def part1(items):
    pp(items)

    # Construct disk map
    files = {}
    _id = 0
    idx = 0
    while idx < len(items):
        file_size = items[idx]
        try:
            free_space = items[idx+1]
        except IndexError:
            free_space = 0
        files[(_id, int(file_size))] = int(free_space)
        idx += 2
        _id += 1
    print_disk_map(files)

    # Get file_ids
    file_ids = [k[0] for k in files.keys()]
    print(f'file_ids {type(file_ids)}: {file_ids}')

    # Recursively move from end to empty space
    
    return

def print_disk_map(files: dict) -> None:
    disk_map = ''
    for k, v in files.items():
        _id, _len = k
        free = "." * v
        disk_map += f"{str(_id) * _len}{free}"
    print()
    print(f'disk_map:')
    print(disk_map)


def part2(items):
    pp(items)
    return


def read_input(year: int, day: int) -> list:
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read()
        return items


if __name__ == "__main__":
    items = read_input(YEAR, DAY)
    print(f"part1 answer: {part1(items)}")
    # print(f"part2 answer: {part2(items)}")
