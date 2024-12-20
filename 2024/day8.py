from pprint import pp


YEAR, DAY = 2024, 8

AN = "#"

def part1(items):
    # Any lower/uppercase character or digit is an antenna
    # Find pairs of antennas that are on the same line in any direction
    # Determine if pairs are on a line
    # Determine distance between antennas
    #
    # ORDER OF OPERATIONS
    # - Brute force
    #   - Find all unique characters
    #   - Find all occurrences of the unique characters
    #
    # CAVEATS
    # - Antinodes only count if they are inside the boundary of the map
    # - Antinodes can occur at the same location as an antenna
    pp(items)
    return


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
