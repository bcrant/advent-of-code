from collections import defaultdict
from pprint import pp


y, d = 2021, 3


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = f.read().splitlines()

    cols = defaultdict(list)
    for row in items:
        for col in range(len(row)):
            cols[col].extend(row[col])

    most_common_bits = ""
    for col in cols.keys():
        cnt_zero = cols[col].count("0")
        cnt_one = cols[col].count("1")
        if cnt_one > cnt_zero:
            most_common_bits += "1"
        else:
            most_common_bits += "0"
    least_common_bits = ""
    for b in most_common_bits:
        bit = "1"
        if b == "1":
            bit = "0"
        least_common_bits += bit
    gamma = int(most_common_bits, 2)
    print("gamma: ", gamma)
    epsilon = int(least_common_bits, 2)
    print("epsilon: ", epsilon)
    return gamma * epsilon


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = f.read().splitlines()

    rows = items
    for pos in range(len(rows[0])):
        most_common_in_pos = (
            1 if sum([int(n[pos]) for n in rows]) >= (len(rows) / 2) else 0
        )
        rows = [r for r in rows if int(r[pos]) == most_common_in_pos]
    oxygen_generator_rating = int(rows[0], 2)
    print("oxygen generator rating: ", oxygen_generator_rating)

    rows = items
    for pos in range(len(rows[0])):
        least_common_in_pos = (
            1 if sum([int(n[pos]) for n in rows]) < (len(rows) / 2) else 0
        )
        tmp_rows = [r for r in rows if int(r[pos]) == least_common_in_pos]
        rows = tmp_rows if tmp_rows else rows
    co2_scrubber_rating = int(rows[0], 2)
    print("CO2 scrubber rating: ", co2_scrubber_rating)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
