""" https://adventofcode.com/2022/day/6 """


def main(stream: str, seq_length: int):
    start, end = 0, seq_length
    while True:
        seq = stream[start:end]
        if len(seq) == len(set(seq)):
            print(f"Found {seq_length} unique at position {end}! {seq}")
            return end
        else:
            start += 1
            end += 1


if __name__ == "__main__":
    with open("./data/day6_input.txt", "r") as f:
        data = f.read()
    print(f"part1 answer: {main(data, 4)}")
    print(f"part2 answer: {main(data, 14)}")
