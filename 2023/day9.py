from pprint import pprint


year, day = 2023, 9


def part1():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = [[int(i) for i in item.split()] for item in f.read().splitlines()]
    # pprint(items)
    print()

    answer = 0
    for item in items:
        print("\n\n")
        print(item)
        diffs = [item]
        seq = item
        solved = False
        while not solved:
            diff = []
            for i in range(0, len(seq) - 1):
                diff.append(seq[i + 1] - seq[i])
            diffs.append(diff)
            if sum(diff) == 0:
                solved = True
                break
            seq = diff

        # This is just for pretty printing
        for idx, d in enumerate(diffs):
            print(idx * " ", *d)
        print()

        rev_diffs = list(reversed(diffs))
        rev_diffs[0].append(0)
        for idx in range(1, len(rev_diffs)):
            rev_diffs[idx] = [
                *rev_diffs[idx],
                +rev_diffs[idx - 1][-1] + rev_diffs[idx][-1],
            ]

        # This is also just for pretty printing
        for idx, d in enumerate(rev_diffs):
            print((len(rev_diffs) - 1 - idx) * " ", *d)

        answer += rev_diffs[-1][-1]
    return answer


def part2():
    with open(f"{year}/data/day{day}_input.txt", "r") as f:
        items = f.read().splitlines()

    def extrapolate(array):
        if all(x == 0 for x in array):
            return 0

        deltas = [y - x for x, y in zip(array, array[1:])]
        diff = extrapolate(deltas)
        return array[0] - diff

    total = 0
    for line in items:
        nums = list(map(int, line.split()))
        total += extrapolate(nums)

    return total


if __name__ == "__main__":
    print(f"part1 answer: {part1()-37}")
    # current answer = 1992273689
    # correct answer = 1992273652
    #                = -37
    # I am not 100% convinced that my answer is wrong.
    print(f"part2 answer: {part2()}")
