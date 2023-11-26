import pprint


y, d = 2020, 2


def part1():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [i.replace(":", "").split(" ") for i in f.read().splitlines()]
    pprint.pprint(items)

    valid = 0
    for item in items:
        _min, _max = [int(i) for i in item[0].split("-")]
        _key = item[1]
        _pw = item[2]
        cnt = _pw.count(_key)
        if cnt >= _min and cnt <= _max:
            valid += 1
    return valid


def part2():
    with open(f"{y}/data/day{d}_input.txt", "r") as f:
        items = [i.replace(":", "").split(" ") for i in f.read().splitlines()]
    pprint.pprint(items)

    valid = 0
    for item in items:
        _min, _max = [int(i) - 1 for i in item[0].split("-")]
        _key = item[1]
        _pw = item[2]
        if not (_pw[_min] == _key and _pw[_max] == _key):
            if _pw[_min] == _key or _pw[_max] == _key:
                valid += 1
    return valid


if __name__ == "__main__":
    print(f"part1 answer: {part1()}")
    print(f"part2 answer: {part2()}")
